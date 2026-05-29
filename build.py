"""Generate files.js — lists all SVG files for the static viewer."""
import json
from pathlib import Path

root = Path(__file__).resolve().parent
svgs = sorted(
    f.name for f in root.iterdir() if f.is_file() and f.suffix.lower() == ".svg"
)
js = "var SVG_FILES = " + json.dumps(svgs, ensure_ascii=False) + ";\n"
Path(root / "files.js").write_text(js, encoding="utf-8")
print(f"files.js written ({len(svgs)} SVG file(s))")
