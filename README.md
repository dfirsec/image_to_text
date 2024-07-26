# Image to Text

Python script that extracts text from images using Tesseract-OCR.

## Prerequisites

1. **Python 3.10 or higher**
2. **Tesseract OCR**

    - **Windows**: `winget install --id UB-Mannheim.TesseractOCR`
    - **Linux**: `sudo apt-get install tesseract-ocr`

## Setup

1. **Clone the repository**:

    ```sh
    git clone https://github.com/dfirsec/image_to_text.git
    cd image_to_text
    ```

2. **Install Poetry** (if you haven't already).

    ```sh
    pip install poetry
    ```

3. **Install the dependencies**:

    ```sh
    poetry install
    ```

4. **Set the Tesseract OCR executable path**: The script automatically sets the path to the Tesseract executable based on the operating system.

    - For Windows: `C:\Program Files\Tesseract-OCR\tesseract.exe`.
    - For Linux: `/usr/bin/tesseract`.

## Usage

### Activate Virtual Environment

```sh
poetry shell
```

### Extract Text from an Image

```sh
python image_to_text.py <IMAGE_FILE_PATH>
```

- **Option:** Specify output text file path:

    ```sh
    python image_to_text.py <IMAGE_FILE_PATH> -o "output.txt"
    ```

- **Option:** Convert Image to PDF:

    ```sh
    python image_to_text.py <IMAGE_FILE_PATH> --pdf
    ```

- **Option:** Specify the output PDF file path:

    ```sh
    python image_to_text.py <IMAGE_FILE_PATH> --pdf -o "output.pdf"
    ```

## Dependencies

- `pillow`: For image processing
- `pytesseract`: Wrapper for Tesseract-OCR Engine.

## License

This program is licensed under the MIT License.
