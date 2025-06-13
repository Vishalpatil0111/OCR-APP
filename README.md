

````markdown
# 🧠 OCR Web App – Image & PDF to JSON

A simple and intuitive web app built with Streamlit that extracts text from uploaded images or PDF files using Tesseract OCR, and returns the result in clean JSON format.

## ✨ Features

- 📤 Upload images (`.png`, `.jpg`, `.jpeg`) or PDFs
- 🌐 Multilingual OCR support (English, Hindi, German, Japanese)
- 📜 View extracted text in JSON format
- 📥 Download the result as a JSON file
- 🖼️ Live preview of recognized text per page

## 🔧 Technologies Used

- [Streamlit](https://streamlit.io/) – Web app framework
- [Tesseract OCR](https://github.com/tesseract-ocr/tesseract) – Text recognition engine
- [Pillow](https://python-pillow.org/) – Image processing
- [pdf2image](https://github.com/Belval/pdf2image) – PDF to image conversion
- Python standard libraries



## 🚀 Setup Instructions

### 🖥️ Run Locally

> Ensure [Tesseract OCR](https://github.com/tesseract-ocr/tesseract) is installed and accessible via your system `PATH`.

1. **Clone the repo**
   ```bash
   git clone https://github.com/yourusername/ocr-web-app.git
   cd ocr-web-app
````

2. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

3. **Run the app**

   ```bash
   streamlit run app.py
   ```


### 🌐 Deploy with Docker (Recommended for Tesseract Compatibility)


```dockerfile
# See README for full Dockerfile
```

Then deploy using [Render](https://render.com), Railway, or locally via:

```bash
docker build -t ocr-app .
docker run -p 8501:8501 ocr-app
```

---

## 📷 Screenshot

![image](https://github.com/user-attachments/assets/08e371f8-5a09-4988-b356-7afc72896055)
![image](https://github.com/user-attachments/assets/d534c2d4-e715-4f2e-89f7-0e88e7faf3ea)


## 📄 Example Output

```json
[
  {
    "page": 1,
    "text": "This is the extracted text from the image or PDF page."
  }
]
```

---

## 🤝 Contributions

Pull requests are welcome! For major changes, please open an issue first to discuss what you'd like to change.


## 🧠 License

[MIT License](LICENSE)


## 🙋‍♂️ Author

Built with 💻 by Vishal Patil(https://www.linkedin.com/in/yourname/)



