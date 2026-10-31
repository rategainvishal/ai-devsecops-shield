import streamlit as st
import google.generativeai as genai
import os

# 1. 100% Free Gemini API Setup
# The dashboard looks for a key saved on your system or falls back to an optional text input box
api_key = os.getenv("GEMINI_API_KEY", "")

st.set_page_config(
    page_title="AI DevSecOps Pipeline Shield", 
    page_icon="🛡️",
    layout="wide"
)

# Title & Framework Header
st.title("🛡️ AI-Driven DevSecOps & Compliance Guard")
st.markdown("### Interactive Cybersecurity & Audit Simulation for Freshers")
st.markdown("---")

# If the key isn't found in system environment variables, allow input directly on the dashboard
if not api_key:
    api_key = st.sidebar.text_input("🔑 Enter Gemini API Key to unlock AI Features:", type="password")

if api_key:
    genai.configure(api_key=api_key)
else:
    st.sidebar.warning("⚠️ Please provide a Gemini API Key to activate the AI Explainer.")

# 2. Layout Setup: Creating Tabs for the recruiter to click through
tab_secret, tab_sast, tab_supply = st.tabs([
    "🔑 Secret Detection (Gitleaks)", 
    "🔍 Code Analysis (Semgrep)", 
    "📦 Supply Chain Audit (Pip-Audit)"
])

# --- TAB 1: GITLEAKS (SECRET SCANNING) ---
with tab_secret:
    st.subheader("🔒 Gitleaks Scanner Simulation")
    st.write("Gitleaks scans code histories to ensure secrets like passwords or AWS keys are never leaked to public repositories.")
    
    st.info("💡 **Scenario:** A developer accidentally leaves an AWS password in `app/main.py` and pushes it.")
    
    if st.button("🚀 Run Simulated Gitleaks Check"):
        fake_error = "CRITICAL: Leaked Credential Detected in app/main.py: AWS_SECRET_ACCESS_KEY=AKIAIOSFODNN7EXAMPLE"
        st.error(f"❌ Scanner Alert:\n{fake_error}")
        
        if api_key:
            with st.spinner("🧠 Gemini AI Explainer generating mitigation plan..."):
                try:
                    model = genai.GenerativeModel('gemini-1.5-flash')
                    prompt = f"Explain this Gitleaks security error message: '{fake_error}'. Provide simple, beginner-friendly bullet points detailing what the risk is and how to fix it securely."
                    response = model.generate_content(prompt)
                    st.success("🤖 AI Security Analysis Complete:")
                    st.markdown(response.text)
                except Exception as e:
                    st.error(f"AI Engine Error: {e}")
        else:
            st.warning("Please enter your API key to view the AI analysis framework.")

# --- TAB 2: SEMGREP (CODE VULNERABILITIES) ---
with tab_sast:
    st.subheader("💻 Semgrep Static Code Analysis (SAST)")
    st.write("Semgrep reads your application source code to spot dangerous programming practices before your app goes live.")
    
    st.info("💡 **Scenario:** The application takes direct, unvalidated input from a user and passes it straight into a database search.")
    
    if st.button("🚀 Run Simulated Semgrep SAST Check"):
        fake_sast_error = "HIGH: SQL Injection vulnerability detected in database helper script at line 14. User inputs are executed without parameterization."
        st.error(f"❌ Scanner Alert:\n{fake_sast_error}")
        
        if api_key:
            with st.spinner("🧠 Gemini AI Explainer rewriting secure code..."):
                try:
                    model = genai.GenerativeModel('gemini-1.5-flash')
                    prompt = f"Explain this SAST security flaw: '{fake_sast_error}'. Provide a short example showing vulnerable Python code versus secure parameterized Python code."
                    response = model.generate_content(prompt)
                    st.success("🤖 AI Security Analysis Complete:")
                    st.markdown(response.text)
                except Exception as e:
                    st.error(f"AI Engine Error: {e}")
        else:
            st.warning("Please enter your API key to view the AI analysis framework.")

# --- TAB 3: PIP-AUDIT (SUPPLY CHAIN SECURITY) ---
with tab_supply:
    st.subheader("📦 Pip-Audit & Software Supply Chain Security")
    st.write("Scans third-party open-source libraries in your `requirements.txt` to make sure none of your external components are hacked or outdated.")
    
    st.info("💡 **Scenario:** An old framework version is imported that contains known security exploits.")
    
    if st.button("🚀 Run Simulated Dependency Audit"):
        fake_dep_error = "Vulnerability Found: Flask version 2.0.1 matches CVE-2023-30861. Threat rating: HIGH. Impact: Potential Denial of Service."
        st.error(f"❌ Scanner Alert:\n{fake_dep_error}")
        
        if api_key:
            with st.spinner("🧠 Gemini AI Explainer creating patching guide..."):
                try:
                    model = genai.GenerativeModel('gemini-1.5-flash')
                    prompt = f"Explain this open-source package vulnerability: '{fake_dep_error}'. Detail what a CVE means in simple words and how a fresher would remediate it via requirements.txt updates."
                    response = model.generate_content(prompt)
                    st.success("🤖 AI Security Analysis Complete:")
                    st.markdown(response.text)
                except Exception as e:
                    st.error(f"AI Engine Error: {e}")
        else:
            st.warning("Please enter your API key to view the AI analysis framework.")
