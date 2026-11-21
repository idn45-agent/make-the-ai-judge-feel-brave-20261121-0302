"""Write the entry text to /output/entry.txt. Stdlib only, deterministic, no network."""
import os
from pathlib import Path

TEXT = (
    "The kettle clicks off. Steam rises in one slow ribbon and thins "
    "against the window, where rain hangs, undecided, on the glass. "
    "The mug warms both hands. The chair holds you, and the light stays "
    "where it fell. Nothing here needs hurrying."
)

def main() -> None:
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_text(TEXT, encoding="utf-8")

if __name__ == "__main__":
    main()
