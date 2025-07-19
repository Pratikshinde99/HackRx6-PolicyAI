import fitz  # PyMuPDF
import os
import json
from openai import OpenAI

# Initialize OpenAI client
client = OpenAI(api_key="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")

def extract_text_from_pdf(file) -> str:
    """Extracts all text from an uploaded PDF file."""
    text = ""
    with fitz.open(stream=file.read(), filetype="pdf") as doc:
        for page in doc:
            text += page.get_text()
    return text

def get_response_from_query(query: str, text: str) -> dict:
    """Uses OpenAI to answer a health insurance query based on PDF content."""
    prompt = f"""
You are an AI assistant helping users understand their health insurance coverage.

Context: {text}

User Query: {query}

Respond ONLY in the following JSON format:
{{
  "approved": true/false,
  "amount": "estimated cover if any",
  "reason": "brief justification using policy clause",
  "clause_reference": "exact section or clause if mentioned"
}}
"""
    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.2
        )
        answer = response.choices[0].message.content.strip()
        return json.loads(answer)
    except json.JSONDecodeError:
        return {"error": "Failed to parse JSON", "raw": answer}
    except Exception as e:
        return {"error": str(e)}
