import requests
import json

def validate_pdf_with_ai(pdf_text, expected_data):
    prompt = f"""
You are a QA validation expert.

Compare the following PDF extracted text:
{pdf_text}

With expected data:
{expected_data}

Identify:
1. Missing fields
2. Incorrect values
3. Mismatches

Return response strictly in JSON format.
"""

    response = requests.post(
        "http://localhost:11434/api/generate",
        json={
            "model": "llama3",
            "prompt": prompt,
            "stream": False
        }
    )

    result = response.json()
    return result["response"]