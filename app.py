import streamlit as st
from utils import extract_text_from_pdf, get_response_from_query

st.set_page_config(page_title="Policy AI Assistant", layout="centered")

st.title("🤖 AI-Powered Policy Query Assistant")
st.markdown("Upload a policy PDF and ask any health-related question to get an AI-backed answer.")

# Upload PDF
pdf_file = st.file_uploader("📄 Upload your policy document (PDF)", type=["pdf"])

# User query input
query = st.text_input("💬 Enter your question (e.g., 'Will my father’s 3-month-old policy cover knee surgery?')")

# Button trigger
if st.button("Ask AI") and pdf_file and query:
    with st.spinner("Processing..."):
        raw_text = extract_text_from_pdf(pdf_file)

        if not raw_text.strip():
            st.error("❌ Failed to extract any text from the PDF.")
        else:
            response = get_response_from_query(query, raw_text)

            st.success("✅ Response generated!")

            if "error" in response:
                st.error(f"❌ Error: {response['error']}")
                st.text_area("🔍 Raw response", value=response.get("raw", ""), height=200)
            else:
                st.subheader("🧾 Result (JSON)")
                st.json(response)
