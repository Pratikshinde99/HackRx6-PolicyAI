# 🤖 Policy AI Assistant – HackRx 6.0

An AI-powered assistant that helps users understand health insurance coverage by answering natural-language queries based on uploaded policy PDF documents.

---

## 🚀 What It Does

This app allows users to:
- 📄 Upload a health insurance **policy PDF**
- 💬 Ask a **natural-language question** (e.g., “Is knee surgery covered under a 3-month-old policy?”)
- 🧠 Uses **OpenAI GPT-3.5 Turbo** to semantically understand the query and policy content
- 🧾 Returns a **structured JSON output**:
  ```json
  {
    "approved": true/false,
    "amount": "estimated cover",
    "reason": "justification using clause",
    "clause_reference": "Section X.XX"
  }
