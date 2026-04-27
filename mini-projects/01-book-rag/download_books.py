import csv
import re
from pathlib import Path

import httpx

BOOKS_DIR = Path(__file__).parent / "books"
CSV_PATH = Path(__file__).parent / "books.csv"


def safe_filename(title: str) -> str:
    return re.sub(r"[^\w\-. ]", "_", title).strip().replace(" ", "_") + ".pdf"


def download_books() -> None:
    BOOKS_DIR.mkdir(exist_ok=True)

    with CSV_PATH.open(newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        rows = list(reader)

    for row in rows:
        title = row["title"]
        url = row["pdf_url"]
        dest = BOOKS_DIR / safe_filename(title)

        if dest.exists():
            print(f"[skip] {title} already downloaded")
            continue

        print(f"[download] {title} ...")
        try:
            with httpx.stream("GET", url, follow_redirects=True, timeout=60) as r:
                r.raise_for_status()
                with dest.open("wb") as out:
                    for chunk in r.iter_bytes(chunk_size=8192):
                        out.write(chunk)
            print(f"[ok] saved to {dest.name}")
        except httpx.HTTPError as e:
            print(f"[error] {title}: {e}")
            dest.unlink(missing_ok=True)


if __name__ == "__main__":
    download_books()
