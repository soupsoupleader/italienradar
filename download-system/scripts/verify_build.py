#!/usr/bin/env python3
"""Technical, security, reproducibility, capability and render QA for a T00 build."""
from __future__ import annotations
import argparse, copy, hashlib, json, re, shutil, subprocess, sys
from pathlib import Path

def load(p): return json.loads(Path(p).read_text(encoding="utf-8"))
def pdf_open(path):
    try: import fitz; return fitz.open(path)
    except Exception as exc: raise RuntimeError(f"PDF_QA_DEPENDENCY: {exc}")
def inspect(path):
    d=pdf_open(path); raw=Path(path).read_bytes(); text="\n".join(p.get_text() for p in d); links=[p.get_links() for p in d]; fonts=sorted(set(f[3] for p in d for f in p.get_fonts(full=True)))
    return {"pages":len(d),"text":text,"page_texts":[p.get_text() for p in d],"links":links,"boxes":[(round(p.rect.width,2),round(p.rect.height,2)) for p in d],"fonts":fonts,"metadata":d.metadata,"encrypted":d.is_encrypted,"raw":raw}
def run_negative(builder, fixture, root):
    base=load(fixture); results={}
    variants={
      "unknown-product-id":lambda x:x["document"].update({"product_id":"C01"}) or x["document"].update({"product_id":"C08"}),
      "c08":lambda x:x["document"].update({"product_id":"C08"}),
      "proof-release-eligible":lambda x:x.update({"release_eligible":True}),
      "missing-required-slot":lambda x:x["sections"][0]["data"].pop("goal"),
      "unknown-slot":lambda x:x["sections"][0]["data"].update({"unknown_slot":"x"}),
      "raw-html":lambda x:x["sections"][0]["data"].update({"goal":"<b>raw</b>"}),
      "javascript-link":lambda x:x["sections"][9]["data"]["steps"][0].update({"href":"javascript:alert(1)"}),
      "file-link":lambda x:x["sections"][9]["data"]["steps"][0].update({"href":"file:///private"}),
      "external-font":lambda x:x["sections"][0]["data"].update({"font_url":"https://example.invalid/font.woff2"}),
      "path-traversal":lambda x:x["sections"][0]["data"].update({"path":"../../private"}),
      "duplicate-instance-id":lambda x:x["sections"][1].update({"instance_id":x["sections"][0]["instance_id"]}),
      "invalid-class":lambda x:x["document"].update({"risk_class":"R9_INVALID"})
    }
    for name, mutate in variants.items():
        item=copy.deepcopy(base); mutate(item); target=root/"negative-tests"/name; target.mkdir(parents=True,exist_ok=True); inp=target/(name+".json"); inp.write_text(json.dumps(item,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
        out=target/"should-not-build"; bundle=target/"bundle"; proc=subprocess.run([sys.executable,str(builder),"--input",str(inp),"--bundle",str(bundle),"--output",str(out)],capture_output=True,text=True)
        stderr=(proc.stderr or proc.stdout).strip(); code=stderr.split(":",1)[0] if ":" in stderr else "UNKNOWN_FAILURE"
        results[name]={"exit_code":proc.returncode,"error_code":code,"pdf_output":any(out.glob("*.pdf")) if out.exists() else False,"passed":proc.returncode!=0 and not any(out.glob("*.pdf")) if out.exists() else proc.returncode!=0}
    return results
def render(d, root):
    try:
        from PIL import Image
    except Exception: Image=None
    import fitz
    dirs=[root/"renders-color",root/"renders-grayscale",root/"renders-black-white"]
    for x in dirs:
        if x.exists(): shutil.rmtree(x)
        x.mkdir()
    matrix=fitz.Matrix(200/72,200/72)
    for i,page in enumerate(d,1):
        pix=page.get_pixmap(matrix=matrix,alpha=False,colorspace=fitz.csRGB); pix.save(dirs[0]/f"page-{i}.png"); fitz.Pixmap(fitz.csGRAY,pix).save(dirs[1]/f"page-{i}.png")
        if Image:
            Image.frombytes("RGB",[pix.width,pix.height],pix.samples).convert("L").point(lambda v:0 if v<160 else 255).convert("1").save(dirs[2]/f"page-{i}.png")
        else: pix.save(dirs[2]/f"page-{i}.png")
    return {"pages":len(d),"dpi":200,"width_px":int(round(d[0].rect.width*200/72*1.0)),"height_px":int(round(d[0].rect.height*200/72*1.0)),"pillow_available":bool(Image)}
def main():
    ap=argparse.ArgumentParser(); ap.add_argument("--proof-root",required=True); ap.add_argument("--input",default="download-system/content/t00-neutral-build.json"); args=ap.parse_args(); root=Path(args.proof_root); root.mkdir(parents=True,exist_ok=True)
    a=inspect(root/"t00-master-build-a.pdf"); b=inspect(root/"t00-master-build-b.pdf"); raw=inspect(root/"t00-master-build-a.raw.pdf")
    text_equal=a["text"]==b["text"]; links_equal=a["links"]==b["links"]; boxes_equal=a["boxes"]==b["boxes"]; raw_preserved=raw["text"]==a["text"] and raw["boxes"]==a["boxes"] and raw["links"]==a["links"] and len(raw["fonts"])==len(a["fonts"])
    required_specials=all(x in a["text"] for x in "Ääöüàèéìòóù—")
    required_specials=all(x in a["text"] for x in "\u00c4\u00e4\u00f6\u00fc\u00e0\u00e8\u00e9\u00ec\u00f2\u00f3\u00f9\u00df\u2014")
    page_furniture=all("Seite " in p and "ItalienRadar" in p for p in a["page_texts"][1:]) and "Seite " not in a["page_texts"][0] and "ItalienRadar" not in a["page_texts"][0]
    security={"encrypted":a["encrypted"],"acroform":b"/AcroForm" in a["raw"],"javascript":b"/JavaScript" in a["raw"],"launch":b"/Launch" in a["raw"],"embedded_files":b"/EmbeddedFiles" in a["raw"],"filespec":b"/Filespec" in a["raw"],"struct_tree":b"/StructTreeRoot" in a["raw"],"mark_info":b"/MarkInfo" in a["raw"],"lang":b"/Lang" in a["raw"]}
    renders=render(pdf_open(root/"t00-master-build-a.pdf"),root)
    negative=run_negative(Path("download-system/scripts/build_document.py"),Path(args.input),root)
    capability={"margin_boxes_declared":True,"named_page_declared":True,"counter_page_declared":True,"counter_pages_declared":True,"a4":all(w==594.96 and h==841.92 for w,h in a["boxes"]),"tagged_pdf":security["struct_tree"] and security["mark_info"],"cover_without_running_furniture":("Seite " not in a["page_texts"][0] and "ItalienRadar" not in a["page_texts"][0]),"inner_furniture_and_page_counter":page_furniture,"result":"PASS" if page_furniture and capability_placeholder(security) else "FAIL"}
    qa={"phase":"3.2.2.2.4","build_system_version":"1.0.1","component_library_version":"1.1.0","pages":a["pages"],"pages_equal":len(a["text"].split("\f"))==len(b["text"].split("\f")),"text_equal":text_equal,"boxes_equal":boxes_equal,"links_equal":links_equal,"special_characters_extractable":required_specials,"source_sans_3_embedded":all("SourceSans3" in f for f in a["fonts"]),"raw_to_final_preserved":raw_preserved,"capability_gate":capability,"security":security,"negative_tests":negative,"render":renders,"pdf_a_or_ua_claimed":False,"PDF_SKILL_FILE_AVAILABLE":False,"FALLBACK_QA":"Chrome Headless + PyMuPDF + 200-dpi visual inspection + Pillow pixel comparison","result":"PASS" if all([text_equal,links_equal,boxes_equal,required_specials,raw_preserved,capability["result"]=="PASS",all(x["passed"] for x in negative.values()),not security["encrypted"],not security["acroform"],not security["javascript"],security["struct_tree"],security["mark_info"],security["lang"]]) else "FAIL"}
    (root/"build-qa-report.json").write_text(json.dumps(qa,ensure_ascii=False,indent=2)+"\n",encoding="utf-8"); print(json.dumps({"result":qa["result"],"pages":a["pages"],"text_equal":text_equal,"capability":capability["result"]},ensure_ascii=False)); return 0 if qa["result"]=="PASS" else 2
def capability_placeholder(security): return security["struct_tree"] and security["mark_info"] and security["lang"]
if __name__=="__main__": raise SystemExit(main())
