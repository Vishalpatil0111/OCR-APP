import streamlit as st
from PIL import Image
import pytesseract
import tempfile
import os
from pdf2image import convert_from_path
import json

st.set_page_config(page_title="OCR Tool", layout="centered")
st.title("📄 OCR Web App - Image & PDF to JSON")

# Language selector
LANGUAGES = {
    "English": "eng",
    "Hindi": "hin",
    "German": "deu",
    "Japanese": "jpn"
}
selected_lang = st.selectbox("🌐 Select OCR Language", list(LANGUAGES.keys()))
tesseract_lang_code = LANGUAGES[selected_lang]

uploaded_file = st.file_uploader("📤 Upload an Image or PDF", type=["png", "jpg", "jpeg", "pdf"])

if uploaded_file:
    file_type = uploaded_file.type
    result_data = []

    # Save uploaded file to a temp file
    with tempfile.NamedTemporaryFile(delete=False) as tmp_file:
        tmp_file.write(uploaded_file.read())
        temp_path = tmp_file.name

    try:
        if "pdf" in file_type:
            st.info("🔍 Converting PDF to images...")
            pages = convert_from_path(temp_path)
            for i, page in enumerate(pages):
                text = pytesseract.image_to_string(page, lang=tesseract_lang_code)
                result_data.append({"page": i + 1, "text": text})
        else:
            st.info("🖼️ Reading image...")
            image = Image.open(temp_path)
            text = pytesseract.image_to_string(image, lang=tesseract_lang_code)
            result_data.append({"page": 1, "text": text})

        # Display JSON
        st.subheader("📜 Extracted Text in JSON Format")
        st.json(result_data)

        # Download JSON
        st.download_button(
            label="📥 Download Result as JSON",
            data=json.dumps(result_data, indent=2, ensure_ascii=False),
            file_name="ocr_result.json",
            mime="application/json"
        )
    except Exception as e:
        st.error(f"❌ OCR failed: {str(e)}")

    os.remove(temp_path)
