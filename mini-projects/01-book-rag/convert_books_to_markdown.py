from pathlib import Path

from markitdown import MarkItDown

BOOKS_DIR = Path(__file__).parent / "books"
OUTPUT_DIR = Path(__file__).parent / "books_text"

md = MarkItDown()


def convert_books() -> None:
    OUTPUT_DIR.mkdir(exist_ok=True)

    pdfs = sorted(BOOKS_DIR.glob("*.pdf"))
    if not pdfs:
        print("No PDFs found in books/")
        return

    for pdf in pdfs:
        dest = OUTPUT_DIR / pdf.with_suffix(".md").name

        if dest.exists():
            print(f"[skip] {pdf.name} already converted")
            continue

        print(f"[convert] {pdf.name} ...")
        try:
            result = md.convert(str(pdf))
            dest.write_text(result.text_content, encoding="utf-8")
            print(f"[ok] saved to {dest.name}")
        except Exception as e:
            print(f"[error] {pdf.name}: {e}")


if __name__ == "__main__":
    convert_books()
