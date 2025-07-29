import streamlit as st
import google.generativeai as genai
import os
from dotenv import load_dotenv
import json
from datetime import datetime
from logic import LCFChatbotLogic

# Load environment variables from .env file
load_dotenv()

# Setup
st.set_page_config(
    page_title="LCF AI Assistant", 
    layout="wide",
    initial_sidebar_state="expanded"
)

# Configure Gemini API
api_key = os.getenv("GOOGLE_API_KEY")
genai.configure(api_key=api_key)
model = genai.GenerativeModel("gemini-1.5-flash")

# Initialize chatbot logic
chatbot_logic = LCFChatbotLogic()

# Initialize session state for chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

if "current_mode" not in st.session_state:
    st.session_state.current_mode = "chat"



# Sidebar for navigation
with st.sidebar:
    st.title("🤖 LCF AI Assistant")
    st.markdown("---")
    
    # Mode selection
    mode = st.radio(
        "Choose Mode:",
        ["💬 General Chat", "📊 Deal Evaluation"],
        key="mode_selector"
    )
    
    if mode == "💬 General Chat":
        st.session_state.current_mode = "chat"
    else:
        st.session_state.current_mode = "deal_eval"
    
    st.markdown("---")
    
    # Quick actions
    st.subheader("Quick Actions")
    if st.button("\U0001F3E2 About LCF"):
        user_msg = "Tell me about LCF Group"
        st.session_state.messages.append({"role": "user", "content": user_msg})
        response = chatbot_logic.generate_empathetic_response(user_msg)
        st.session_state.messages.append({"role": "assistant", "content": response})
    
    if st.button("\U0001F4B0 Our Products"):
        user_msg = "What products does LCF offer?"
        st.session_state.messages.append({"role": "user", "content": user_msg})
        response = chatbot_logic.generate_empathetic_response(user_msg)
        st.session_state.messages.append({"role": "assistant", "content": response})
    
    if st.button("\U0001F4CB Eligibility"):
        user_msg = "What are the eligibility requirements?"
        st.session_state.messages.append({"role": "user", "content": user_msg})
        response = chatbot_logic.generate_empathetic_response(user_msg)
        st.session_state.messages.append({"role": "assistant", "content": response})
    
    if st.button("\U0001F4DE Contact Info"):
        user_msg = "How can I contact LCF?"
        st.session_state.messages.append({"role": "user", "content": user_msg})
        response = chatbot_logic.generate_empathetic_response(user_msg)
        st.session_state.messages.append({"role": "assistant", "content": response})
    
    st.markdown("---")
    
    # Clear chat
    if st.button("🗑️ Clear Chat"):
        st.session_state.messages = []
        st.rerun()

# Main content area
if st.session_state.current_mode == "chat":
    # Chat interface
    st.title("💬 LCF AI Assistant")
    st.markdown("*Your empathetic financial advisor and company information assistant*")
    
    # Display chat messages
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])
    
    # Chat input
    if prompt := st.chat_input("Ask me anything about LCF Group..."):
        # Add user message to chat history
        st.session_state.messages.append({"role": "user", "content": prompt})
        
        # Display user message
        with st.chat_message("user"):
            st.markdown(prompt)
        
        # Generate response
        with st.chat_message("assistant"):
            with st.spinner("Thinking..."):
                # Use chatbot logic for empathetic responses
                response = chatbot_logic.generate_empathetic_response(prompt)
                st.markdown(response)
                
                # Add assistant response to chat history
                st.session_state.messages.append({"role": "assistant", "content": response})

else:
    # Deal Evaluation Mode
    st.title("📊 LCF Deal Evaluation Assistant")
    st.markdown("*Evaluate loan deals using LCF's AI underwriting assistant*")
    
    # Create two columns for better layout
    col1, col2 = st.columns([1, 1])
    
    with col1:
        st.subheader("📋 Deal Information")

        with st.form("deal_eval_form", clear_on_submit=False):
            industry = st.selectbox(
                "Business Industry", 
                ["Retail", "Construction", "Healthcare", "Restaurants", "Transportation", "Manufacturing", "Technology", "Others"]
            )
            monthly_revenue = st.number_input(
                "Monthly Revenue (Rs)", 
                step=10000, 
                min_value=10000,
                help="Enter your average monthly business revenue"
            )
            loan_amount = st.number_input(
                "Requested Loan Amount (Rs)", 
                step=10000, 
                min_value=10000,
                help="Enter the loan amount you're requesting"
            )
            loan_type = st.selectbox(
                "Loan Type", 
                ["Working Capital", "Line of Credit", "Merchant Cash Advance", "Equipment Financing", "Invoice Factoring"]
            )
            business_age = st.selectbox(
                "Time in Business", 
                ["<1 year", "1-2 years", "2-5 years", ">5 years"]
            )
            tenure = st.selectbox(
                "Requested Tenure", 
                ["3 months", "6 months", "12 months", "18 months", "24 months"]
            )
            credit_score = st.selectbox(
                "Business Credit Score", 
                ["Excellent (750+)", "Good (700-749)", "Fair (650-699)", "Poor (<650)", "Unknown"]
            )

            submitted = st.form_submit_button("🔍 Evaluate Deal", type="primary")

        if submitted:
            deal_info = f"""
            Deal Information:
            - Business Industry: {industry}
            - Monthly Revenue: Rs {monthly_revenue:,}
            - Requested Loan Amount: Rs {loan_amount:,}
            - Loan Type: {loan_type}
            - Time in Business: {business_age}
            - Requested Tenure: {tenure}
            - Credit Score: {credit_score}
    """

            evaluation_prompt = f"""
            You are an expert AI underwriter at LCF Group. Evaluate the following loan request based on LCF's underwriting criteria.
            
            {deal_info}
            
            Provide a comprehensive evaluation including:
            1. **Risk Assessment**: Low/Medium/High risk classification
            2. **Recommendation**: Approve/Reject/Manual Review with confidence level
            3. **Suggested Product**: Recommend the most suitable LCF product
            4. **Loan Terms**: Suggested loan amount, interest rate range, and repayment terms
            5. **Reasoning**: Detailed explanation of your decision
            6. **Next Steps**: What the applicant should do next
            
            Be professional but empathetic in your response. Format the response clearly with headers.
    """

            with col2:
                st.subheader("📊 Evaluation Results")
                with st.spinner("🔍 Analyzing deal with AI..."):
                    deal_data = {
                        'industry': industry,
                        'monthly_revenue': monthly_revenue,
                        'loan_amount': loan_amount,
                        'loan_type': loan_type,
                        'business_age': business_age,
                        'tenure': tenure,
                        'credit_score': credit_score
                    }
                    evaluation = chatbot_logic.evaluate_deal(deal_data)
                    # Format and display the evaluation result
                    result_md = f"""
## 📊 Deal Evaluation Results

### 🎯 Risk Assessment
**Risk Level:** {evaluation['risk_level']}\n
**Recommendation:** {evaluation['recommendation']}\n
**Confidence:** {evaluation['confidence']}

### 💰 Suggested Product
**Recommended Product:** {evaluation['suggested_product']}

### 📋 Risk Factors
"""
                    for factor in evaluation['risk_factors']:
                        result_md += f"- {factor}\n"
                    result_md += f"""

### 💳 Suggested Loan Terms
**Amount:** ₹{evaluation['loan_terms']['suggested_amount']:,.0f}\n
**Interest Rate:** {evaluation['loan_terms']['interest_rate']}\n
**Tenure:** {evaluation['loan_terms']['tenure']}\n
**Processing Fee:** {evaluation['loan_terms']['processing_fee']}\n
### 🚀 Next Steps
"""
                    for step in evaluation['next_steps']:
                        result_md += f"- {step}\n"
                    st.success("✅ Evaluation Complete!")
                    st.markdown("---")
                    st.markdown(result_md)
                    
                    # Add to chat history for reference
                    st.session_state.messages.append({
                        "role": "user", 
                        "content": f"Deal Evaluation Request: {deal_info}"
                    })
                    st.session_state.messages.append({
                        "role": "assistant", 
                        "content": f"Deal Evaluation Results:\n\n{result_md}"
                    })
    
    with col2:
        # Remove the duplicate button and just show tips and help
        st.subheader("💡 Tips for Better Evaluation")
        st.markdown("""
        **To get the most accurate evaluation:**
        
        ✅ Provide accurate financial information\n
        ✅ Include all relevant business details\n
        ✅ Be honest about credit history\n
        ✅ Consider your business needs carefully
        
        **Common factors that improve approval:**
        - Stable monthly revenue
        - Good credit history
        - Clear business purpose
        - Realistic loan amount
        """)
        st.markdown("---")
        st.subheader("📞 Need Help?")
        st.markdown("""
        If you need assistance with your application:
        
        📧 Email: applications@lcfgroup.com
        📞 Phone: +91-XXXXXXXXXX
        💬 Chat: Use the general chat mode
        """)

# Footer
st.markdown("---")
st.markdown(
    """
    <div style='text-align: center; color: #666; font-size: 0.8em;'>
        🤖 Powered by LCF AI Assistant | 
        <a href='#' style='color: #666;'>Privacy Policy</a> | 
        <a href='#' style='color: #666;'>Terms of Service</a>
    </div>
    """, 
    unsafe_allow_html=True
)
