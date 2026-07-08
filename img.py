import streamlit as st
import pytesseract
from PIL import Image
import re

# --- Tesseract path (Windows) ---
pytesseract.pytesseract.tesseract_cmd = r'C:\Users\Harish\AppData\Local\Programs\Tesseract-OCR\tesseract.exe'

st.set_page_config(page_title="OCR Text Extractor", layout="centered")

st.title("OCR Text Extractor")
st.write("Upload an image and extract text from it using Tesseract OCR.")

# --- File uploader ---
uploaded_file = st.file_uploader(
    "Choose an image file",
    type=["png", "jpg", "jpeg", "bmp", "tiff", "gif"]
)

if uploaded_file is not None:
    image = Image.open(uploaded_file)

    # Show the uploaded image
    st.image(image, caption="Uploaded Image", use_container_width=True)

    # Run OCR
    with st.spinner("Extracting text..."):
        extracted_text = pytesseract.image_to_string(image)

    st.subheader("Extracted Text")
    st.text_area("Result", extracted_text, height=200)

    # Download button for the extracted text
    st.download_button(
        label="Download as .txt",
        data=extracted_text,
        file_name="extracted_text.txt",
        mime="text/plain"
    )
else:
    st.info("Upload an image to get started.")
