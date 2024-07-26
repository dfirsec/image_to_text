import argparse
import logging
import sys
from collections.abc import Callable
from pathlib import Path
from typing import Any

import pytesseract
from PIL import Image

# Set up logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

# Set path to the Tesseract-OCR executable
# Windows installer -> `winget install --id UB-Mannheim.TesseractOCR`
TESSERACT_CMD = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
pytesseract.pytesseract.tesseract_cmd = TESSERACT_CMD


def exceptions_handler(func: Callable[..., Any]) -> Callable[..., Any]:
    """Decorator to handle exceptions."""

    def wrapper(*args, **kwargs) -> None:
        try:
            return func(*args, **kwargs)
        except FileNotFoundError:
            logging.error(f"Image file not found: {args[0]}")
            sys.exit(1)
        except pytesseract.TesseractNotFoundError:
            logging.error("Tesseract OCR not found. Please install it and ensure the correct path in TESSERACT_CMD.")
            sys.exit(1)
        except Exception as e:
            logging.error(f"An unexpected error occurred: {e}")
            sys.exit(1)

    return wrapper


@exceptions_handler
def get_text_from_image(image_path: Path) -> str:
    """Extract text from the image."""
    with Image.open(image_path) as img:
        return pytesseract.image_to_string(img)


@exceptions_handler
def convert_image_to_pdf(image_path: Path, pdf_path: Path) -> None:
    """Convert the image to a PDF."""
    with Image.open(image_path) as img:
        pdf = pytesseract.image_to_pdf_or_hocr(img, extension="pdf")
        pdf_path.write_bytes(pdf)
        logging.info(f"PDF created successfully: {pdf_path}")


def process_image(image_path: Path, output_path: Path | None = None, to_pdf: bool = False) -> None:
    """Process the image: either extract text or convert to PDF."""
    if to_pdf:
        pdf_path = output_path or Path("output.pdf")
        convert_image_to_pdf(image_path, pdf_path)
    else:
        text = get_text_from_image(image_path)
        text_path = output_path or Path("recognized.txt")
        text_path.write_text(text, encoding="utf-8")
        logging.info(f"Text extracted and saved to: {text_path}")


def main() -> None:
    """Run the main program."""
    parser = argparse.ArgumentParser(description="Extract text from an image using Tesseract OCR.")
    parser.add_argument("image_path", type=Path, help="Path to the input image")
    parser.add_argument("-o", "--output", type=Path, help="Path to the output file")
    parser.add_argument("--pdf", help="Convert the image to a PDF", action="store_true")
    args = parser.parse_args()

    try:
        process_image(args.image_path, args.output, args.pdf)
    except Exception as e:
        logging.error(f"An unexpected error occurred in main: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
