# src/pdf_validator.py
import json
import os
import re
from shutil import copyfile
import cv2

from .pdf_reader import extract_text
from .ai_engine import validate_pdf_with_ai
from .visual_validator import pdf_to_image, compare_images


def parse_ai_output(ai_result: str) -> dict:
    """
    Extract JSON from AI output. Handles variations like:
    - Triple backticks ```{ ... }```
    - JSON directly
    - Malformed / missing JSON
    """
    # Try triple backticks
    match = re.search(r"```(.*?)```", ai_result, re.DOTALL)
    if match:
        json_text = match.group(1).strip()
    else:
        json_text = ai_result.strip()

    # Remove any leading text like "Here is the JSON response:"
    json_text = re.sub(r'^[^\{]*', '', json_text).strip()

    try:
        return json.loads(json_text)
    except json.JSONDecodeError as e:
        return {
            "raw_output": ai_result,
            "error": str(e)
        }


def validate_pdf(pdf_path, baseline_path=None):
    """
    Validates PDF both text (via AI) and visually.
    Returns:
        ai_json: parsed AI JSON dict
        visual_score: float difference score
        diff_path: path to diff image if visual difference found
    """

    # ------------------ Baseline Handling ------------------
    if baseline_path is None:
        baseline_path = pdf_path
    if not os.path.exists(baseline_path):
        copyfile(pdf_path, baseline_path)

    # ------------------ Text Extraction & AI ------------------
    pdf_text = extract_text(pdf_path)
    expected_data = {
        "Invoice Number": "INV-2026-1005",
        "Date": "2026-04-02",
        "Billing To": "John Doe, Halifax, Canada"
    }
    ai_result = validate_pdf_with_ai(pdf_text, expected_data)
    ai_json = parse_ai_output(ai_result)

    # ------------------ Visual Validation ------------------
    baseline_img = pdf_to_image(baseline_path)
    current_img = pdf_to_image(pdf_path)

    # Resize baseline to match current
    baseline_img = baseline_img.resize(current_img.size)
    score, diff = compare_images(baseline_img, current_img)

    diff_path = None
    if score > 0:
        diff_path = os.path.join(os.path.dirname(pdf_path), "diff.png")
        cv2.imwrite(diff_path, diff)

    return ai_json, score, diff_path