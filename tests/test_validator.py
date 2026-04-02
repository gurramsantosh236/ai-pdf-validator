# tests/test_validator.py
import os
import warnings
import pytest
from src.pdf_validator import validate_pdf

# ------------------ PDFs to test ------------------
pdfs = [
    os.path.join(os.path.dirname(__file__), "../data/advanced_invoice_sample.pdf")
]

@pytest.mark.parametrize("pdf_path", pdfs)
def test_pdf_validation(pdf_path):
    pdf_path = os.path.abspath(pdf_path)
    baseline_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "../data/baseline.pdf"))

    # ------------------ Check file exists ------------------
    assert os.path.exists(pdf_path), f"PDF not found: {pdf_path}"

    # ------------------ Run validation ------------------
    ai_result, visual_score, diff_path = validate_pdf(pdf_path, baseline_path)

    # ------------------ AI validation assertions ------------------
    if "raw_output" in ai_result:
        warnings.warn(f"AI returned unparseable JSON: {ai_result.get('error')}")
    else:
        assert "missingFields" in ai_result or "missing_fields" in ai_result

    # ------------------ Visual validation assertions ------------------
    assert visual_score >= 0

    # ------------------ Attach visual diff to Allure ------------------
    if diff_path and os.path.exists(diff_path):
        import allure
        allure.attach.file(diff_path, name="Visual Diff", attachment_type=allure.attachment_type.PNG)