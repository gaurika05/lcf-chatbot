import streamlit as st
import google.generativeai as genai
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Setup
st.set_page_config(page_title="LCF Deal Evaluation Assistant", layout="centered" )
st.title("LCF Deal Evaluation Assistant")
st.write("Evaluate loan deals using LCF's AI underwriting assistant.")

# Configure Gemini API - use environment variable for security
api_key = os.getenv("GOOGLE_API_KEY")
genai.configure(api_key=api_key)
model = genai.GenerativeModel("gemini-1.5-flash")

# Inputs
industry = st.selectbox("Business Industry", ["Retail", "Construction", "Healthcare", "Restaurants", "Transportation", "Others"])
monthly_revenue = st.number_input("Monthly Revenue (Rs)", step=10000, min_value=10000)
loan_amount = st.number_input("Requested Loan Amount (Rs)", step=10000, min_value=10000)
loan_type = st.selectbox("Loan type", ["Working Capital", "Line of Credit", "Merchant Cash Advance", "Equipment Financing"])
business_age = st.selectbox("Time in Business", ["<1 year", "1-2 years", ">2 years"])
tenure = st.selectbox("Requested Tenure", ["3 months", "6 months", "12 months", "24 months"])

# Submit
if st.button("Evaluate Deal"):
    # Prompt
    user_input = f"""Business: {industry}
    Monthly Revenue: Rs{monthly_revenue}
    Requested Loan: {loan_type}
    Time in Business: {business_age}
    Requested Tenure: {tenure}
    """

    prompt = f"""
    You are an AI assistant at LCF Group that helps evaluate funding requests based on internal underwriting rules.

    Instructions:
    - Classify risk level (Low, Medium, High)
    - Recommend: Approve, Reject, or Manual Review
    - Suggest a suitable LCF product
    - Provide short reasoning

    Deal Info:
    {user_input}
    """

    with st.spinner("Evalauting with Gemini AI..."):
        response = model.generate_content(prompt).text

        st.success("Evaluation Complete")
        st.markdown("### Result")
        st.markdown(response)
