#!/usr/bin/env python3
"""Conditionally adds controlled PDF metadata without rebuilding page content."""
from __future__ import annotations
import argparse, json, shutil
from pathlib import Path

def main():
    p=argparse.ArgumentParser(); p.add_argument("--input",required=True); p.add_argument("--output",required=True); p.add_argument("--report",required=True); p.add_argument("--title",required=True); p.add_argument("--subject",required=True); p.add_argument("--keywords",required=True); p.add_argument("--document-version",required=True); p.add_argument("--risk-class",required=True); p.add_argument("--update-class",required=True); p.add_argument("--source-version",required=True); p.add_argument("--build-version",required=True); args=p.parse_args()
    try:
        import fitz
    except Exception as exc:
        raise SystemExit(f"METADATA_GATE_FAIL: PyMuPDF unavailable: {exc}")
    source=Path(args.input); target=Path(args.output); report=Path(args.report)
    shutil.copy2(source,target)
    doc=fitz.open(target); before=dict(doc.metadata)
    after=dict(before)
    values={"title":args.title,"author":"ItalienRadar","subject":args.subject,"keywords":args.keywords,"creationDate":"D:20260715000000Z","modDate":"D:20260715000000Z"}
    for key,value in values.items():
        # Normalize controlled metadata even when Chromium supplied volatile
        # timestamps or a different default value. Page content is untouched.
        if after.get(key) != value: after[key]=value
    changed={k:[before.get(k),after.get(k)] for k in values if before.get(k)!=after.get(k)}
    if changed:
        doc.set_metadata(after)
        try: doc.saveIncr()
        except Exception as exc: raise SystemExit(f"METADATA_GATE_FAIL: incremental save unsupported: {exc}")
    doc.close()
    report.write_text(json.dumps({"mode":"POSTPROCESSING_MODE = CONDITIONAL_METADATA_ONLY","changed":changed,"before":before,"after":after,"document_version":args.document_version,"risk_class":args.risk_class,"update_class":args.update_class,"source_version":args.source_version,"build_version":args.build_version,"result":"PASS"},ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
    print(json.dumps({"result":"PASS","changed_fields":list(changed)}))
if __name__ == "__main__": main()
