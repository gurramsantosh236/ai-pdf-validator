# 🤖 AI-Powered PDF Validator with Visual Testing

## 📌 Overview

This project is an **AI-driven PDF validation framework** that combines:

* 🧠 **AI-based content validation** (using LLMs / Ollama)
* 👁️ **Visual regression testing** (image comparison)
* 📊 **Allure reporting** for professional test insights

It is designed to validate **dynamic PDF documents** like invoices, reports, and statements in an automated and intelligent way.

---

## 🚀 Features

✅ Extracts text from PDF files
✅ Validates content using AI (semantic validation)
✅ Detects missing fields and incorrect values
✅ Performs visual comparison between baseline and current PDFs
✅ Generates **difference images (diff.png)**
✅ Integrates with **Pytest + Allure reports**
✅ Auto-creates baseline PDFs for first-time execution

---

## 🏗️ Project Structure

```
ai-pdf-validator/
│
├── src/
│   ├── pdf_reader.py
│   ├── ai_engine.py
│   ├── visual_validator.py
│   ├── pdf_validator.py
│   └── __init__.py
│
├── tests/
│   └── test_validator.py
│
├── data/
│   ├── baseline.pdf
│   └── advanced_invoice_sample.pdf
│
├── reports/
│
└── README.md
```

---

## ⚙️ Tech Stack

* **Python 3.14**
* **Pytest**
* **Allure Reporting**
* **OpenCV**
* **pdf2image**
* **Ollama / LLM (AI validation)**

---

## 🧠 How It Works

### 1. Text Validation (AI)

* Extracts text from PDF
* Compares against expected data
* Identifies:

  * Missing fields
  * Incorrect values
  * Mismatches

### 2. Visual Validation

* Converts PDF → images
* Compares with baseline image
* Generates:

  * Difference score
  * Visual diff (`diff.png`)

### 3. Reporting

* Pytest executes validations
* Allure generates interactive HTML reports
* Includes:

  * Test status
  * Logs
  * Visual attachments

---

## ▶️ How to Run

### 1. Install dependencies

```
pip install pytest allure-pytest opencv-python pdf2image
```

---

### 2. Install Poppler (Windows)

Download from:
https://github.com/oschwartz10612/poppler-windows/releases/

Add `poppler/bin` to system PATH.

---

### 3. Run Tests

```
pytest --alluredir=reports/allure-results
```

---

### 4. View Allure Report

```
allure serve reports/allure-results
```

---

## 📸 Sample Output

* ✅ AI validation results (JSON)
* ✅ Visual difference score
* ✅ Diff image (`diff.png`)
* ✅ Interactive Allure dashboard

---

## 💡 Use Cases

* Invoice validation automation
* Financial document verification
* Regression testing for generated PDFs
* QA automation for document-heavy applications

---

## 🏆 Key Highlights

* Combines **AI + Visual Testing** in one framework
* Handles **non-deterministic AI outputs robustly**
* Designed for **real-world automation testing scenarios**
* Easily extendable for UI/API testing

---

## 🔮 Future Enhancements

* Multi-PDF batch validation
* API-based PDF validation
* Cloud execution (AWS)
* CI/CD integration (GitHub Actions)

---

## 👨‍💻 Author

**Santoshkumar Gurram**
📍 Halifax, Canada
