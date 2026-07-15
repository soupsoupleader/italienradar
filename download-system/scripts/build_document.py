#!/usr/bin/env python3
"""Deterministic, offline IMR HTML bundle builder using only the Python stdlib."""
from __future__ import annotations

import argparse
import copy
import hashlib
import html
import json
import os
import re
import shutil
import subprocess
import sys
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urlparse

ROOT = Path(__file__).resolve().parents[2]
COMPONENT_DIR = ROOT / "download-system" / "components"
FONT_DIR = ROOT / "download-system" / "assets" / "fonts" / "source-sans-3"
MANIFEST_PATH = ROOT / "download-system" / "manifests" / "component-library.json"
SCHEMA_PATH = ROOT / "download-system" / "manifests" / "document-input-schema.json"
TOKENS_PATH = ROOT / "download-system" / "tokens" / "design-tokens.json"
BUILD_SYSTEM_PATH = ROOT / "download-system" / "manifests" / "build-system.json"
TEMPLATE_PATH = ROOT / "download-system" / "templates" / "master-template.html"
TEXT_SUFFIXES = {".html", ".css", ".json", ".py", ".ps1", ".md", ".txt"}

class BuildFailure(Exception):
    def __init__(self, code: str, message: str):
        super().__init__(f"{code}: {message}")
        self.code = code

class Node:
    def __init__(self, tag=None, attrs=None, parent=None, text=None):
        self.tag, self.attrs, self.parent, self.children, self.text = tag, attrs or [], parent, [], text
    def attr(self, name):
        for key, value in self.attrs:
            if key == name:
                return value or ""
        return None
    def set_attr(self, name, value):
        for i, (key, _) in enumerate(self.attrs):
            if key == name:
                self.attrs[i] = (key, value)
                return
        self.attrs.append((name, value))
    def remove_attr(self, name):
        self.attrs = [(k, v) for k, v in self.attrs if k != name]

class TreeParser(HTMLParser):
    void = {"meta", "link", "img", "br", "hr", "input"}
    def __init__(self):
        super().__init__(convert_charrefs=False); self.root = Node("root"); self.current = self.root
    def handle_starttag(self, tag, attrs):
        node = Node(tag, list(attrs), self.current); self.current.children.append(node)
        if tag not in self.void: self.current = node
    def handle_startendtag(self, tag, attrs): self.handle_starttag(tag, attrs); self.current = self.current.parent if self.current.tag == tag else self.current
    def handle_endtag(self, tag):
        node = self.current
        while node is not self.root:
            if node.tag == tag: self.current = node.parent; return
            node = node.parent
    def handle_data(self, data): self.current.children.append(Node(parent=self.current, text=data))
    def handle_entityref(self, name): self.handle_data(f"&{name};")
    def handle_charref(self, name): self.handle_data(f"&#{name};")
    def handle_comment(self, data): self.current.children.append(Node("!comment", parent=self.current, text=data))

def parse_fragment(source: str) -> Node:
    parser = TreeParser(); parser.feed(source); return parser.root

def clone(node): return copy.deepcopy(node)

def text_content(node):
    return node.text if node.tag is None else "".join(text_content(c) for c in node.children)

def canonical_source_bytes(path: Path) -> bytes:
    raw = path.read_bytes()
    if path.suffix.lower() not in TEXT_SUFFIXES:
        return raw
    text = raw.decode("utf-8-sig")
    return text.replace("\r\n", "\n").replace("\r", "\n").encode("utf-8")

def canonical_source_hash(path: Path) -> str:
    h = hashlib.sha256()
    h.update(canonical_source_bytes(path))
    return h.hexdigest().upper()

def raw_sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""): h.update(chunk)
    return h.hexdigest().upper()

def copy_canonical_source(source: Path, destination: Path) -> None:
    destination.parent.mkdir(parents=True, exist_ok=True)
    if source.suffix.lower() in TEXT_SUFFIXES:
        destination.write_bytes(canonical_source_bytes(source))
    else:
        shutil.copyfile(source, destination)

def write_utf8_lf(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_bytes(text.replace("\r\n", "\n").replace("\r", "\n").encode("utf-8"))

def resolve_source_commit() -> str:
    try:
        proc = subprocess.run(["git", "rev-parse", "HEAD"], cwd=ROOT, capture_output=True, text=True, timeout=10)
    except Exception as exc:
        raise BuildFailure("P0_SOURCE_COMMIT_UNAVAILABLE", str(exc))
    commit = (proc.stdout or "").strip()
    if proc.returncode != 0 or not re.fullmatch(r"[0-9a-f]{40}", commit):
        raise BuildFailure("P0_SOURCE_COMMIT_UNAVAILABLE", "git rev-parse HEAD did not return one commit")
    return commit

def canonical(value):
    return json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(",", ":"))

def get_path(data, path):
    value = data
    for part in path.split(".") if path else []:
        if isinstance(value, dict) and part in value: value = value[part]
        else: raise BuildFailure("P0_UNRESOLVED_SLOT", f"unresolved slot {path}")
    return value

def walk(node):
    yield node
    for child in node.children: yield from walk(child)

def parse_json(path):
    try: return json.loads(canonical_source_bytes(path).decode("utf-8"))
    except Exception as exc: raise BuildFailure("P0_INVALID_JSON", f"{path}: {exc}")

def forbidden_value(value):
    if isinstance(value, dict): return any(forbidden_value(k) or forbidden_value(v) for k, v in value.items())
    if isinstance(value, list): return any(forbidden_value(v) for v in value)
    if isinstance(value, str): return bool(re.search(r"<\s*[A-Za-z]|file:|javascript:|data:text|C:\\|OneDrive|AppData|\.tmp[/\\]|api[_-]?key|password", value, re.I))
    return False

def validate_url(value):
    if not isinstance(value, str) or any(x in value for x in ("?", "&", "=", "%")) and "#" not in value:
        raise BuildFailure("P0_UNSAFE_URL", "invalid or tracking URL")
    parsed = urlparse(value)
    if value.startswith("#"):
        if not re.fullmatch(r"#[A-Za-z0-9_-]+", value): raise BuildFailure("P0_INVALID_REFERENCE", value)
    elif parsed.scheme != "https" or not parsed.netloc:
        raise BuildFailure("P0_UNSAFE_URL", value)

def serialize(node):
    if node.tag is None: return html.escape(node.text or "", quote=False)
    if node.tag == "!comment": return f"<!--{node.text or ''}-->"
    attrs = "".join(f' {k}="{html.escape(v or "", quote=True)}"' for k, v in node.attrs)
    if node.tag in TreeParser.void: return f"<{node.tag}{attrs}>"
    return f"<{node.tag}{attrs}>" + "".join(serialize(c) for c in node.children) + f"</{node.tag}>"

def find_nodes(root, predicate): return [n for n in walk(root) if n.tag and predicate(n)]

def replace_text(node, value):
    node.children = [Node(parent=node, text=str(value))]

def resolve_slot(path, data, contexts):
    if path in contexts: return contexts[path]
    first = path.split(".", 1)[0]
    if first in contexts:
        return get_path(contexts[first], path.split(".", 1)[1] if "." in path else "")
    return get_path(data, path)

def process_repeats(node, data, contexts):
    for current in list(walk(node)):
        repeat = current.attr("data-repeat") if current.tag else None
        if not repeat: continue
        values = resolve_slot(repeat, data, contexts)
        if not isinstance(values, list): raise BuildFailure("P0_INVALID_TYPE", f"repeat {repeat} must be array")
        template = next((c for c in current.children if c.tag and not c.tag.startswith("!")), None)
        if template is None: raise BuildFailure("P0_UNRESOLVED_SLOT", f"repeat template {repeat}")
        generated = []
        item_name = current.attr("data-repeat-item") or "item"
        for value in values:
            item = clone(template); item.parent = current
            process_node(item, data, {**contexts, item_name: value})
            generated.append(item)
        current.children = generated
        current.remove_attr("data-repeat"); current.remove_attr("data-repeat-item")

def process_node(node, data, contexts):
    if node.tag is None: return
    bind = node.attr("data-bind-text")
    if bind:
        value = resolve_slot(bind, data, contexts)
        if isinstance(value, (dict, list)): raise BuildFailure("P0_INVALID_TYPE", f"text slot {bind} is not scalar")
        replace_text(node, value)
    href_bind = node.attr("data-bind-href")
    if href_bind:
        value = resolve_slot(href_bind, data, contexts); validate_url(value); node.set_attr("href", value)
    for attr in ("data-bind-text", "data-bind-href", "data-bind-toc", "data-bind-sections"): node.remove_attr(attr)
    for child in list(node.children): process_node(child, data, contexts)

def namespace_tree(root, namespace, component_id, ordinal):
    mapping = {}
    for node in walk(root):
        if not node.tag: continue
        old = node.attr("id")
        if old: mapping[old] = f"{namespace}-{component_id}-{ordinal:02d}-{old}"
    if len(mapping) != len(set(mapping)): raise BuildFailure("P0_DUPLICATE_HTML_ID", component_id)
    for node in walk(root):
        if not node.tag: continue
        old = node.attr("id")
        if old: node.set_attr("id", mapping[old])
        for attr in ("for", "aria-labelledby", "aria-describedby"):
            value = node.attr(attr)
            if value:
                node.set_attr(attr, " ".join(mapping.get(x, x) for x in value.split()))
        href = node.attr("href")
        if href and href.startswith("#") and href[1:] in mapping: node.set_attr("href", "#" + mapping[href[1:]])

def component_marker_set(source):
    tree = parse_fragment(source); markers = set(); repeats = set(); links = set()
    for n in walk(tree):
        if not n.tag: continue
        if n.attr("data-bind-text"): markers.add(n.attr("data-bind-text"))
        if n.attr("data-repeat"): repeats.add(n.attr("data-repeat"))
        if n.attr("data-bind-href"): links.add(n.attr("data-bind-href"))
    return markers, repeats, links

def manifest_marker_set(contract):
    allowed=set()
    for slot in contract.get("binding_slots", []):
        allowed.add(slot)
        for prefix in ("rows.", "steps.", "tasks.", "sources."):
            if slot.startswith(prefix): allowed.add(slot[len(prefix):])
    return allowed

def validate_input(data, manifest, schema):
    if set(data) != set(schema["top_level_fields"]): raise BuildFailure("P0_UNKNOWN_FIELD", "top-level input fields differ")
    if data["build_mode"] not in schema["allowed_build_modes"]: raise BuildFailure("P0_INVALID_MODE", data["build_mode"])
    if data["build_mode"] == "PROOF" and (data.get("fixture_id") != "T00" or data.get("release_eligible") is not False or data.get("document", {}).get("publication_status") != "QA_REQUIRED"): raise BuildFailure("P0_PROOF_RELEASE_INELIGIBLE", "invalid PROOF contract")
    if data["build_mode"] == "PRODUCTION" and data.get("fixture_id") == "T00": raise BuildFailure("P0_INVALID_MODE", "T00 is PROOF-only")
    if data.get("release_eligible") and data["build_mode"] == "PROOF": raise BuildFailure("P0_PROOF_RELEASE_INELIGIBLE", "release_eligible")
    doc = data.get("document", {})
    allowed_doc=set(schema["document_required_fields"]+schema.get("document_optional_fields",[]))
    unknown_doc=set(doc)-allowed_doc
    if unknown_doc: raise BuildFailure("P0_UNKNOWN_FIELD", "document." + sorted(unknown_doc)[0])
    if doc.get("product_id") == "C08": raise BuildFailure("P0_C08_EXCLUDED", "C08")
    if data["build_mode"] == "PRODUCTION" and doc.get("product_id") not in manifest["supported_products"]: raise BuildFailure("P0_INVALID_PRODUCT", "production product_id")
    for key in schema["document_required_fields"]:
        if key not in doc: raise BuildFailure("P0_MISSING_REQUIRED_FIELD", f"document.{key}")
    if doc.get("language") != "de-DE" or doc.get("document_class") not in schema["document_rules"]["document_classes"] or doc.get("risk_class") not in schema["document_rules"]["risk_classes"] or doc.get("update_class") not in schema["document_rules"]["update_classes"]: raise BuildFailure("P0_INVALID_CLASS", "document class/risk/update")
    if forbidden_value(data): raise BuildFailure("P0_RAW_HTML", "forbidden value in input")
    ids = {c["id"]: c for c in manifest["components"]}; seen = set()
    if len(data["sections"]) != 12: raise BuildFailure("P0_MISSING_REQUIRED_FIELD", "all M01-M12 sections required")
    for sec in data["sections"]:
        for key in schema["section_required_fields"]:
            if key not in sec: raise BuildFailure("P0_MISSING_REQUIRED_FIELD", f"section.{key}")
        cid = sec["component_id"]
        if cid not in ids: raise BuildFailure("P0_UNKNOWN_COMPONENT", cid)
        if sec["instance_id"] in seen: raise BuildFailure("P0_DUPLICATE_INSTANCE_ID", sec["instance_id"])
        seen.add(sec["instance_id"])
        if sec["heading_level"] not in ids[cid]["allowed_heading_levels"]: raise BuildFailure("P0_INVALID_CLASS", f"heading {cid}")
        if not isinstance(sec["data"], dict): raise BuildFailure("P0_INVALID_TYPE", cid)
        contract=ids[cid]
        allowed_data=set(contract.get("required_inputs",[])+contract.get("optional_inputs",[])+contract.get("repeat_groups",[]))
        allowed_data.update(slot.split(".")[0] for slot in contract.get("binding_slots",[]))
        unknown_data=set(sec["data"])-allowed_data
        if unknown_data: raise BuildFailure("P0_UNKNOWN_SLOT", f"{cid}.{sorted(unknown_data)[0]}")
    if data.get("build", {}).get("locale") != "de-DE" or data.get("build", {}).get("timezone") != "UTC": raise BuildFailure("P0_INVALID_CLASS", "locale/timezone")

def copy_bundle(bundle, data, manifest, build_system):
    if bundle.exists(): shutil.rmtree(bundle)
    (bundle / "styles").mkdir(parents=True); (bundle / "components").mkdir(); (bundle / "assets" / "fonts" / "source-sans-3").mkdir(parents=True)
    copy_canonical_source(TOKENS_PATH.parent / "design-tokens.css", bundle / "styles" / "tokens.css")
    copy_canonical_source(ROOT / "download-system" / "templates" / "master-template.css", bundle / "styles" / "master-template.css")
    copy_canonical_source(COMPONENT_DIR / "components.css", bundle / "styles" / "components.css")
    used = []
    for component in manifest["components"]:
        src = ROOT / component["source_file"]; dest = bundle / "components" / src.name; copy_canonical_source(src, dest); used.append((src, Path("components") / src.name))
    for font in ["source-sans-3-regular.woff2","source-sans-3-semibold.woff2","source-sans-3-bold.woff2"]:
        src=FONT_DIR/font; copy_canonical_source(src,bundle/"assets"/"fonts"/"source-sans-3"/font); used.append((src,Path("assets")/"fonts"/"source-sans-3"/font))
    used += [(TOKENS_PATH.parent/"design-tokens.css",Path("styles")/"tokens.css"),(ROOT/"download-system"/"templates"/"master-template.css",Path("styles")/"master-template.css"),(COMPONENT_DIR/"components.css",Path("styles")/"components.css"),(TEMPLATE_PATH,Path("master-template.html"))]
    return used

def render_components(data, manifest):
    output=[]; global_ids={}; namespace = re.sub(r"[^A-Za-z0-9_-]", "-", str(data.get("fixture_id") or data["document"].get("canonical_title","document")))
    for ordinal, sec in enumerate(data["sections"], 1):
        contract = next(c for c in manifest["components"] if c["id"] == sec["component_id"])
        source = canonical_source_bytes(ROOT / contract["source_file"]).decode("utf-8"); markers, repeats, links = component_marker_set(source)
        if not markers.issubset(manifest_marker_set(contract)): raise BuildFailure("P0_UNKNOWN_SLOT", sec["component_id"])
        tree=parse_fragment(source)
        for n in walk(tree):
            if n.tag and n.attr("id"):
                global_ids[n.attr("id")] = f"{namespace}-{sec['component_id']}-{ordinal:02d}-{n.attr('id')}"
        process_repeats(tree,sec["data"],{}); process_node(tree,sec["data"],{})
        namespace_tree(tree,namespace,sec["component_id"],ordinal)
        for n in walk(tree):
            if n.tag: n.remove_attr("data-component-version")
        output.append("".join(serialize(c) for c in tree.children))
    rendered="\n".join(output)
    for local, namespaced in global_ids.items(): rendered=rendered.replace(f'href="#{local}"', f'href="#{namespaced}"')
    return rendered

def build(args):
    data=parse_json(Path(args.input)); manifest=parse_json(MANIFEST_PATH); schema=parse_json(SCHEMA_PATH); tokens=parse_json(TOKENS_PATH); build_system=parse_json(BUILD_SYSTEM_PATH)
    source_commit = args.source_commit or resolve_source_commit()
    chrome_version = args.chrome_version or ""
    if not re.fullmatch(r"\d+\.\d+\.\d+\.\d+", chrome_version): raise BuildFailure("P0_CHROME_VERSION_UNAVAILABLE", "normalized Chrome version required")
    if build_system["build_system_version"] != "1.0.1": raise BuildFailure("P0_VERSION_MISMATCH", "build system")
    validate_input(data,manifest,schema)
    if manifest["library_version"] != "1.1.0": raise BuildFailure("P0_VERSION_MISMATCH", "component library")
    for font in ["source-sans-3-regular.woff2","source-sans-3-semibold.woff2","source-sans-3-bold.woff2"]:
        if not (FONT_DIR/font).is_file(): raise BuildFailure("P0_MISSING_FONT", font)
    bundle=Path(args.bundle); output=Path(args.output); used=copy_bundle(bundle,data,manifest,build_system)
    template=parse_fragment(canonical_source_bytes(TEMPLATE_PATH).decode("utf-8")); context={"document":data["document"],"build_mode":data["build_mode"],"build":data["build"]}; process_node(template,data,context)
    rendered=render_components(data,manifest)
    document="".join(serialize(c) for c in template.children).replace("<!-- BIND_COMPONENTS -->",rendered)
    if re.search(r"<script\b|<form\b|https?://[^\"]*\.(?:css|woff2|png|jpg)|url\(https?://",document,re.I): raise BuildFailure("P0_OFFLINE_RESOURCE", "remote build resource")
    for href in re.findall(r"href=\"([^\"]+)\"",document):
        if href.startswith(("file:","javascript:","data:")): raise BuildFailure("P0_UNSAFE_URL",href)
    if len(re.findall(r"<h1\b",document,re.I)) != 1: raise BuildFailure("P0_INVALID_STRUCTURE", "master template must have one H1")
    if output.exists(): shutil.rmtree(output)
    output.mkdir(parents=True); write_utf8_lf(bundle/"document.html", document)
    normalized=canonical(data); input_hash=hashlib.sha256(normalized.encode("utf-8")).hexdigest().upper(); source_hashes={str(rel).replace("\\","/"):(canonical_source_hash(src) if src.suffix.lower() in TEXT_SUFFIXES else raw_sha256(src)) for src,rel in used}
    write_utf8_lf(bundle/"build-input.normalized.json", json.dumps(data,ensure_ascii=False,sort_keys=True,indent=2)+"\n")
    write_utf8_lf(bundle/"source-manifest.json", json.dumps({"sources":source_hashes,"canonicalization":"UTF8_NO_BOM_LF","binary_hashing":"RAW_BYTES"},sort_keys=True,indent=2)+"\n")
    build_identity={"input_hash":input_hash,"source_hashes":source_hashes,"python_version":sys.version.split()[0],"chrome_version":chrome_version,"build_system_version":build_system["build_system_version"],"component_library_version":manifest["library_version"],"design_token_version":build_system["design_token_version"],"input_schema_version":build_system["input_schema_version"],"locale":data["build"]["locale"],"timezone":data["build"]["timezone"]}
    build_id=hashlib.sha256(canonical(build_identity).encode("utf-8")).hexdigest().upper()
    manifest_out={"build_id":build_id,"input_hash":input_hash,"source_hashes":source_hashes,"git_commit":source_commit,"python_version":sys.version.split()[0],"chrome_version":chrome_version,"locale":"de-DE","timezone":"UTC","build_system_version":build_system["build_system_version"],"component_library_version":manifest["library_version"],"token_version":tokens["schema_version"],"flags":build_system["chrome_flags"],"build_id_inputs":build_identity}
    write_utf8_lf(bundle/"build-manifest.json", json.dumps(manifest_out,sort_keys=True,indent=2)+"\n")
    for name in ["document.html","build-input.normalized.json","source-manifest.json","build-manifest.json"]: copy_canonical_source(bundle/name,output/name)
    write_utf8_lf(output/"build-report.json", json.dumps({"result":"BUNDLE_READY","build_id":build_id,"renderer":"pending","chrome_version":chrome_version,"git_commit":source_commit,"offline":True},indent=2)+"\n")
    print(json.dumps({"result":"PASS","build_id":build_id,"bundle":str(bundle),"document":str(bundle/"document.html")},ensure_ascii=False))

def main():
    parser=argparse.ArgumentParser(); parser.add_argument("--input",required=True); parser.add_argument("--bundle",required=True); parser.add_argument("--output",required=True); parser.add_argument("--chrome-version"); parser.add_argument("--source-commit"); args=parser.parse_args()
    try: build(args)
    except BuildFailure as exc: print(str(exc),file=sys.stderr); return 2
    except Exception as exc: print(f"P0_BUILD_ERROR: {exc}",file=sys.stderr); return 3
    return 0
if __name__ == "__main__": raise SystemExit(main())
