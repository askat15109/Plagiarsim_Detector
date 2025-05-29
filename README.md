
# 📄 Plagiarism Checker using Flask, TF-IDF & Cosine Similarity

A lightweight plagiarism detection web app where users can upload PDF files and receive a plagiarism score by comparing the content with a stored database of texts.

---

## 🗂️ Repository Structure

```
├── __pycache__/           # Python cache (can be ignored)
├── uploaded_pdfs/         # Temporary uploaded PDFs
├── how to run.txt         # Quick instructions for running the app
├── index.html             # Frontend interface
├── main.py                # Flask backend for PDF plagiarism checking
├── stored_texts.txt       # File containing existing documents to compare against
├── README.md              # You're here!
```

---

## 🚀 Features

- ✅ Upload and check plagiarism of PDF files
- 🧠 Uses **TF-IDF** + **Cosine Similarity** for text similarity scoring
- 🔍 Detects content overlap with existing stored text
- 🌐 Simple frontend interface
- 🧾 Extracts text from PDFs using **PyMuPDF**

---

## 🔧 Requirements

Make sure you have Python 3.7+ installed.

Install dependencies:

```bash
pip install flask scikit-learn pymupdf
```

---

## ▶️ How to Run

You can also see `how to run.txt`, but here's a quick guide:

1. **Start the Flask server**:

```bash
python main.py
```

2. **Open your browser** and go to:

```
http://127.0.0.1:5000
```

3. **Upload a PDF** and click "Check Plagiarism"!

---

## 📌 How It Works

1. **User uploads a PDF** via the HTML interface.
2. **Backend extracts text** using PyMuPDF (`fitz`).
3. Text is **compared with contents** from `stored_texts.txt`.
4. **TF-IDF vectorization + cosine similarity** are used to compute plagiarism score.
5. Results are returned as JSON and displayed to the user.

---

## 📁 stored_texts.txt Format

This file contains your database of reference documents.

```
Artificial Intelligence is changing the world...
Data Science is a growing field...
```

Each line or paragraph can represent a new document in the database.

---

## 🧪 Testing

To test:

- Add content in `stored_texts.txt` you want to detect as plagiarism
- Upload a PDF containing similar or same content
- Output will show "⚠️ Plagiarism Detected" if match > 20%

---

## 📎 Notes

- Temporary files are stored in `uploaded_pdfs/` during runtime.
- `__pycache__` is automatically generated and can be ignored.

---

## 🧑‍💻 Author

Made with ❤️ by Akshat Choubey

---

## 📜 License

This project is for educational purposes and freely available under the [MIT License](LICENSE).
