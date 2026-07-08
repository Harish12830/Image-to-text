# Image-to-Text (OCR Extractor)

A simple web app that extracts text from images using Optical Character Recognition (OCR). Built with **Python**, **Tesseract OCR**, and **Streamlit**.

## Features

- Upload an image (PNG, JPG, JPEG, BMP, TIFF, GIF)
- Extract all readable text from the image using Tesseract OCR
- View extracted text directly in the browser
- Download the extracted text as a `.txt` file
- Quick field search — search for a specific field (e.g., "Claim ID", "Amount") within the extracted text

## Tech Stack

- **Python 3**
- **Tesseract OCR** — open-source OCR engine
- **pytesseract** — Python wrapper for Tesseract
- **Pillow (PIL)** — image handling
- **Streamlit** — web app frontend

## Prerequisites

Before running this project, you need Tesseract OCR installed on your machine (separate from the Python packages):

- **Windows**: [Download from UB-Mannheim](https://github.com/UB-Mannheim/tesseract/wiki)
- **macOS**: `brew install tesseract`
- **Linux**: `sudo apt install tesseract-ocr`

Verify installation:
```bash
tesseract --version
```

## Setup & Installation

1. Clone this repository:
```bash
git clone https://github.com/Harish12830/Image-to-text.git
cd Image-to-text
```

2. Create a virtual environment (optional but recommended):
```bash
python -m venv env
env\Scripts\activate      # Windows
source env/bin/activate   # macOS/Linux
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Update the Tesseract path in `img.py` if needed (Windows only):
```python
pytesseract.pytesseract.tesseract_cmd = r'C:\path\to\tesseract.exe'
```

## Usage

Run the Streamlit app:
```bash
streamlit run img.py
```

This will open the app in your browser at `http://localhost:8501`. Upload an image and the extracted text will appear instantly.

## How It Works

1. User uploads an image through the Streamlit interface
2. The image is passed to Tesseract OCR via `pytesseract`
3. Tesseract analyzes the image and returns machine-readable text
4. The extracted text is displayed in the app and made available for download
5. Optionally, a regex-based search can extract specific fields from the text

## Limitations

- Works best on clean, high-contrast, printed text
- Not designed for handwriting recognition
- Accuracy drops on blurry, skewed, or low-resolution images
- Currently supports single images only (not multi-page PDFs)

## Future Improvements

- [ ] Add support for PDF file uploads (convert pages to images first)
- [ ] Add image preprocessing (denoising, deskewing) for better accuracy on poor-quality scans
- [ ] Add multi-language OCR support
- [ ] Add structured field extraction using NLP (beyond basic regex)

## Author

Harish — [GitHub](https://github.com/Harish12830)
