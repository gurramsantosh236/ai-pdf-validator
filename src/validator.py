from pdf_reader import extract_text
from ai_engine import validate_pdf_with_ai
from visual_validator import pdf_to_image, compare_images
import json
import cv2

pdf_path = "../data/advanced_invoice_sample.pdf"

# Text Extraction
try:
    pdf_text = extract_text(pdf_path)
except FileNotFoundError:
    print("PDF not found:", pdf_path)
    exit(1)

print("**********************Extracted Text:********************")
#print(pdf_text)

# Expected Data
expected_data = {
    "Invoice Number": "INV-2026-1005",
    "Date": "2026-04-02",
    "Billing To": "John Doe, Halifax, Canada"
}

# AI Validation
result = validate_pdf_with_ai(pdf_text, expected_data)

try:
    result_json = json.loads(result)
except:
    result_json = {"raw_output": result}

print("**********************AI Validation Result:********************")
print(result_json)

# Visual Validation
baseline = pdf_to_image("../data/baseline.pdf")
current = pdf_to_image(pdf_path)

# Resize to match
baseline = baseline.resize(current.size)

score, diff = compare_images(baseline, current)
cv2.imwrite("diff.png", diff)

print("**********************Visual Validation Result:********************")
print("Difference Score:", score)

if score > 0:
    print("Visual differences found! (See diff.png)")
else:
    print("No visual differences")