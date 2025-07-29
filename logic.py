import json
from datetime import datetime
from typing import Dict, List, Optional

class LCFChatbotLogic:
    """Core logic for LCF AI Assistant chatbot"""
    
    def __init__(self):
        self.company_knowledge = self._load_company_knowledge()
        self.conversation_history = []
        self.user_context = {}
    
    def _load_company_knowledge(self) -> Dict:
        """Load comprehensive company knowledge base"""
        return {
            "company_info": {
                "name": "LCF Group",
                "tagline": "Empowering businesses with smart financial solutions",
                "founded": "2015",
                "mission": "To provide accessible and flexible financial solutions to small and medium businesses",
                "vision": "To be the most trusted financial partner for growing businesses"
            },
            "products": {
                "working_capital": {
                    "name": "Working Capital Loans",
                    "description": "Short-term financing for day-to-day business operations",
                    "amount_range": "₹50,000 - ₹50,00,000",
                    "tenure": "3-24 months",
                    "interest_rate": "1.5% - 3% per month",
                    "requirements": ["6+ months in business", "₹50,000+ monthly revenue", "Valid business registration"]
                },
                "merchant_cash_advance": {
                    "name": "Merchant Cash Advance",
                    "description": "Funding based on future credit card sales",
                    "amount_range": "₹25,000 - ₹25,00,000",
                    "tenure": "3-18 months",
                    "factor_rate": "1.15 - 1.35",
                    "requirements": ["Credit card sales", "3+ months processing history", "₹30,000+ monthly sales"]
                },
                "equipment_financing": {
                    "name": "Equipment Financing",
                    "description": "Loans specifically for purchasing business equipment",
                    "amount_range": "₹1,00,000 - ₹1,00,00,000",
                    "tenure": "12-60 months",
                    "interest_rate": "12% - 18% per annum",
                    "requirements": ["Equipment quote", "Down payment (10-20%)", "Good credit history"]
                },
                "line_of_credit": {
                    "name": "Line of Credit",
                    "description": "Revolving credit facility for flexible borrowing",
                    "amount_range": "₹1,00,000 - ₹1,00,00,000",
                    "tenure": "12-36 months",
                    "interest_rate": "15% - 22% per annum",
                    "requirements": ["2+ years in business", "Strong financials", "Good credit score"]
                },
                "invoice_factoring": {
                    "name": "Invoice Factoring",
                    "description": "Convert outstanding invoices to immediate cash",
                    "amount_range": "₹50,000 - ₹50,00,000",
                    "advance_rate": "70% - 90%",
                    "fee": "1% - 3% per month",
                    "requirements": ["B2B invoices", "Creditworthy customers", "Valid invoices"]
                }
            },
            "eligibility": {
                "basic_requirements": [
                    "Minimum 6 months in business",
                    "Monthly revenue of ₹50,000+",
                    "Valid business registration",
                    "Indian business entity"
                ],
                "documents_required": [
                    "Business registration certificate",
                    "Bank statements (6 months)",
                    "GST registration (if applicable)",
                    "Business PAN card",
                    "Address proof",
                    "Identity proof of directors/partners"
                ],
                "credit_requirements": {
                    "excellent": "750+ credit score",
                    "good": "700-749 credit score",
                    "fair": "650-699 credit score",
                    "poor": "Below 650 credit score"
                }
            },
            "process": {
                "application_steps": [
                    "Submit online application",
                    "Upload required documents",
                    "AI-powered evaluation",
                    "Manual review (if needed)",
                    "Approval and disbursement"
                ],
                "timeline": {
                    "application": "10-15 minutes",
                    "evaluation": "24 hours",
                    "disbursement": "Same day after approval"
                }
            },
            "contact": {
                "phone": "+91-XXXXXXXXXX",
                "email": "info@lcfgroup.com",
                "support_email": "support@lcfgroup.com",
                "website": "www.lcfgroup.com",
                "office_hours": "Monday-Friday, 9 AM - 6 PM",
                "emergency": "+91-XXXXXXXXXX"
            },
            "faqs": {
                "general": [
                    {
                        "question": "What makes LCF different from traditional banks?",
                        "answer": "LCF offers faster approval (24 hours), flexible terms, minimal documentation, and personalized service. We focus on your business potential rather than just credit scores."
                    },
                    {
                        "question": "Do I need collateral for LCF loans?",
                        "answer": "Most of our products don't require collateral. We offer unsecured business loans based on your business performance and creditworthiness."
                    },
                    {
                        "question": "How quickly can I get funds?",
                        "answer": "Once approved, funds are typically disbursed within 24 hours. The entire process from application to disbursement usually takes 1-2 business days."
                    }
                ],
                "eligibility": [
                    {
                        "question": "What if I have a low credit score?",
                        "answer": "We consider multiple factors beyond just credit scores. Strong business performance, consistent revenue, and clear business purpose can help offset lower credit scores."
                    },
                    {
                        "question": "Can startups apply for LCF loans?",
                        "answer": "Yes, but you need at least 6 months of business operations and consistent monthly revenue of ₹50,000+. We also look at the business model and growth potential."
                    }
                ]
            }
        }
    
    def generate_empathetic_response(self, user_query: str, context: Dict = None) -> str:
        """Generate empathetic and helpful response based on user query"""
        
        # Analyze query intent
        intent = self._analyze_intent(user_query.lower())
        
        # Generate appropriate response
        if intent == "company_info":
            return self._get_company_info_response()
        elif intent == "products":
            return self._get_products_response()
        elif intent == "eligibility":
            return self._get_eligibility_response()
        elif intent == "contact":
            return self._get_contact_response()
        elif intent == "application":
            return self._get_application_response()
        elif intent == "deal_evaluation":
            return self._get_deal_evaluation_guidance()
        elif intent == "greeting":
            return self._get_greeting_response()
        elif intent == "help":
            return self._get_help_response()
        else:
            return self._get_general_response(user_query)
    
    def _analyze_intent(self, query: str) -> str:
        """Analyze user query to determine intent"""
        query_lower = query.lower()
        
        # Company information
        if any(word in query_lower for word in ["about", "company", "lcf", "what is", "tell me about"]):
            return "company_info"
        
        # Products
        if any(word in query_lower for word in ["product", "loan", "financing", "advance", "credit", "funding"]):
            return "products"
        
        # Eligibility
        if any(word in query_lower for word in ["eligible", "requirement", "qualify", "need", "document"]):
            return "eligibility"
        
        # Contact
        if any(word in query_lower for word in ["contact", "phone", "email", "call", "reach", "support"]):
            return "contact"
        
        # Application
        if any(word in query_lower for word in ["apply", "application", "process", "how to", "start"]):
            return "application"
        
        # Deal evaluation
        if any(word in query_lower for word in ["evaluate", "deal", "assessment", "approval", "risk"]):
            return "deal_evaluation"
        
        # Greeting
        if any(word in query_lower for word in ["hello", "hi", "hey", "good morning", "good afternoon"]):
            return "greeting"
        
        # Help
        if any(word in query_lower for word in ["help", "assist", "support", "what can you do"]):
            return "help"
        
        return "general"
    
    def _get_greeting_response(self) -> str:
        """Generate warm greeting response"""
        return (
            "👋 Hello! I'm your LCF AI Assistant, here to help you with all things related to LCF Group.\n\n"
            "I can help you with:\n"
            "• 📊 **Company Information** - Learn about LCF Group\n"
            "• 💰 **Our Products** - Explore financing options\n"
            "• 📋 **Eligibility** - Check if you qualify\n"
            "• 📞 **Contact Information** - Get in touch with us\n"
            "• 🔍 **Deal Evaluation** - Get a quick assessment of your loan request\n\n"
            "What would you like to know about today? I'm here to make your financial journey smoother! 😊"
        )
    
    def _get_company_info_response(self) -> str:
        """Generate company information response"""
        company = self.company_knowledge["company_info"]
        return f"""🏢 **About LCF Group**

{company['tagline']}

**Our Story:**
Founded in {company['founded']}, LCF Group has been dedicated to {company['mission']}. Our vision is {company['vision']}.

**What We Do:**
We specialize in providing smart financial solutions to small and medium businesses, including:
• Working Capital Loans
• Merchant Cash Advances  
• Equipment Financing
• Line of Credit
• Invoice Factoring

**Why Choose LCF?**
✅ **Fast Approval** - Get decisions in 24 hours
✅ **Flexible Terms** - Tailored to your business needs
✅ **Minimal Documentation** - Simple application process
✅ **No Collateral** - Most loans are unsecured
✅ **Personalized Service** - Dedicated relationship managers

Would you like to know more about our specific products or how to get started? 💼"""
    
    def _get_products_response(self) -> str:
        """Generate products information response"""
        products = self.company_knowledge["products"]
        
        response = "💰 **LCF Financial Products**\n\n"
        
        for key, product in products.items():
            response += f"**{product['name']}**\n"
            response += f"📝 {product['description']}\n"
            response += f"💵 Amount: {product['amount_range']}\n"
            
            if 'tenure' in product:
                response += f"⏰ Tenure: {product['tenure']}\n"
            if 'interest_rate' in product:
                response += f"📊 Rate: {product['interest_rate']}\n"
            if 'factor_rate' in product:
                response += f"📊 Factor Rate: {product['factor_rate']}\n"
            if 'advance_rate' in product:
                response += f"📊 Advance Rate: {product['advance_rate']}\n"
            
            response += "\n"
        
        response += "**Ready to explore?** I can help you understand which product might be best for your business needs! 🚀"
        
        return response
    
    def _get_eligibility_response(self) -> str:
        """Generate eligibility information response"""
        eligibility = self.company_knowledge["eligibility"]
        
        response = "📋 **Eligibility Requirements**\n\n"
        
        response += "**Basic Requirements:**\n"
        for req in eligibility["basic_requirements"]:
            response += f"✅ {req}\n"
        
        response += "\n**Documents You'll Need:**\n"
        for doc in eligibility["documents_required"]:
            response += f"📄 {doc}\n"
        
        response += "\n**Credit Score Guidelines:**\n"
        for score, desc in eligibility["credit_requirements"].items():
            response += f"• {score.title()}: {desc}\n"
        
        response += "\n**💡 Good News:** We look at your overall business performance, not just credit scores. Strong revenue and clear business purpose can help! 🌟"
        
        return response
    
    def _get_contact_response(self) -> str:
        """Generate contact information response"""
        contact = self.company_knowledge["contact"]
        
        return f"""📞 **Get in Touch with LCF**

**General Inquiries:**
📧 Email: {contact['email']}
🌐 Website: {contact['website']}
📱 Phone: {contact['phone']}

**Customer Support:**
📧 Support: {contact['support_email']}
🚨 Emergency: {contact['emergency']}

**Office Hours:**
🕘 {contact['office_hours']}

**💬 Prefer to chat?** I'm here 24/7 to answer your questions! You can also schedule a call with our relationship managers for personalized assistance. 😊"""
    
    def _get_application_response(self) -> str:
        """Generate application process response"""
        process = self.company_knowledge["process"]
        
        response = "🚀 **How to Apply for LCF Financing**\n\n"
        
        response += "**Simple 5-Step Process:**\n"
        for i, step in enumerate(process["application_steps"], 1):
            response += f"{i}. {step}\n"
        
        response += f"\n**Timeline:**\n"
        for stage, time in process["timeline"].items():
            response += f"• {stage.title()}: {time}\n"
        
        response += "\n**🎯 Ready to Start?**\n"
        response += "You can begin your application right here! I can guide you through the process or help you evaluate your deal first. What would you prefer? 💪"
        
        return response
    
    def _get_deal_evaluation_guidance(self) -> str:
        """Generate deal evaluation guidance"""
        return """🔍 **Deal Evaluation**

Great! I can help you get a quick assessment of your loan request. 

**What I'll evaluate:**
• Risk assessment (Low/Medium/High)
• Approval recommendation
• Suggested loan terms
• Product recommendations
• Next steps

**To get started:**
1. Switch to "📊 Deal Evaluation" mode in the sidebar
2. Fill in your business details
3. Get instant AI-powered evaluation

**💡 Pro Tip:** The more accurate information you provide, the better the evaluation will be!

Would you like to try the deal evaluation now? I'm here to make the process as smooth as possible! ✨"""
    
    def _get_help_response(self) -> str:
        """Generate help response"""
        return """🤝 **How Can I Help You?**

I'm your LCF AI Assistant, and I'm here to make your financial journey easier! Here's what I can do:

**📊 Company Information**
• Learn about LCF Group
• Understand our mission and values
• Discover what makes us different

**💰 Product Guidance**
• Explore our financing options
• Understand loan terms and rates
• Find the best product for your needs

**📋 Eligibility Check**
• Review requirements
• Check if you qualify
• Understand documentation needed

**🔍 Deal Evaluation**
• Get quick loan assessment
• Understand approval chances
• Receive personalized recommendations

**📞 Contact & Support**
• Get contact information
• Find office hours
• Connect with our team

**💬 Just Chat**
• Ask any questions
• Get personalized advice
• Receive empathetic support

What would you like to explore today? I'm here to help! 😊"""
    
    def _get_general_response(self, query: str) -> str:
        """Generate general response for unrecognized queries"""
        return f"""I understand you're asking about "{query}". While I'm specifically trained to help with LCF Group information, I'd be happy to assist you with:

• 📊 Information about LCF Group and our services
• 💰 Our financing products and eligibility
• 📋 Application process and requirements
• 🔍 Deal evaluation and assessment
• 📞 Contact information and support

Could you rephrase your question about LCF, or would you like to know about any of these topics? I'm here to help! 😊"""

    def evaluate_deal(self, deal_data: Dict) -> Dict:
        """Evaluate a loan deal based on provided data"""
        
        # Extract deal information
        industry = deal_data.get('industry', '')
        monthly_revenue = deal_data.get('monthly_revenue', 0)
        loan_amount = deal_data.get('loan_amount', 0)
        loan_type = deal_data.get('loan_type', '')
        business_age = deal_data.get('business_age', '')
        tenure = deal_data.get('tenure', '')
        credit_score = deal_data.get('credit_score', '')
        
        # Basic risk assessment logic
        risk_score = 0
        risk_factors = []
        
        # Revenue analysis
        if monthly_revenue < 50000:
            risk_score += 3
            risk_factors.append("Low monthly revenue")
        elif monthly_revenue < 100000:
            risk_score += 1
            risk_factors.append("Moderate monthly revenue")
        else:
            risk_score -= 1
        
        # Loan amount vs revenue ratio
        loan_to_revenue_ratio = loan_amount / monthly_revenue if monthly_revenue > 0 else 0
        if loan_to_revenue_ratio > 6:
            risk_score += 3
            risk_factors.append("High loan-to-revenue ratio")
        elif loan_to_revenue_ratio > 3:
            risk_score += 1
            risk_factors.append("Moderate loan-to-revenue ratio")
        
        # Business age analysis
        if business_age == "<1 year":
            risk_score += 2
            risk_factors.append("New business")
        elif business_age == "1-2 years":
            risk_score += 1
            risk_factors.append("Young business")
        
        # Credit score analysis
        if "Poor" in credit_score or "Unknown" in credit_score:
            risk_score += 2
            risk_factors.append("Credit concerns")
        elif "Excellent" in credit_score:
            risk_score -= 1
        
        # Determine risk level
        if risk_score <= 0:
            risk_level = "Low"
            recommendation = "Approve"
            confidence = "High"
        elif risk_score <= 3:
            risk_level = "Medium"
            recommendation = "Manual Review"
            confidence = "Medium"
        else:
            risk_level = "High"
            recommendation = "Reject"
            confidence = "High"
        
        # Suggest product
        suggested_product = self._suggest_product(deal_data)
        
        # Generate response
        evaluation = {
            "risk_level": risk_level,
            "recommendation": recommendation,
            "confidence": confidence,
            "suggested_product": suggested_product,
            "risk_factors": risk_factors,
            "loan_terms": self._suggest_loan_terms(deal_data, risk_level),
            "next_steps": self._get_next_steps(recommendation)
        }
        
        return evaluation
    
    def _suggest_product(self, deal_data: Dict) -> str:
        """Suggest the most suitable product based on deal data"""
        loan_type = deal_data.get('loan_type', '')
        monthly_revenue = deal_data.get('monthly_revenue', 0)
        business_age = deal_data.get('business_age', '')
        
        # If user already specified a loan type, suggest it
        if loan_type:
            return loan_type
        
        # Suggest based on business characteristics
        if business_age == "<1 year":
            return "Merchant Cash Advance"
        elif monthly_revenue < 100000:
            return "Working Capital Loan"
        else:
            return "Line of Credit"
    
    def _suggest_loan_terms(self, deal_data: Dict, risk_level: str) -> Dict:
        """Suggest loan terms based on risk level"""
        loan_amount = deal_data.get('loan_amount', 0)
        
        if risk_level == "Low":
            return {
                "suggested_amount": loan_amount,
                "interest_rate": "1.5% - 2% per month",
                "tenure": "12-24 months",
                "processing_fee": "1-2%"
            }
        elif risk_level == "Medium":
            return {
                "suggested_amount": loan_amount * 0.8,
                "interest_rate": "2% - 2.5% per month",
                "tenure": "6-18 months",
                "processing_fee": "2-3%"
            }
        else:
            return {
                "suggested_amount": loan_amount * 0.5,
                "interest_rate": "2.5% - 3% per month",
                "tenure": "3-12 months",
                "processing_fee": "3-5%"
            }
    
    def _get_next_steps(self, recommendation: str) -> List[str]:
        """Get next steps based on recommendation"""
        if recommendation == "Approve":
            return [
                "Submit complete application with required documents",
                "Complete KYC verification",
                "Sign loan agreement",
                "Receive funds within 24 hours"
            ]
        elif recommendation == "Manual Review":
            return [
                "Submit detailed business plan",
                "Provide additional financial documents",
                "Schedule call with relationship manager",
                "Await manual underwriting decision"
            ]
        else:
            return [
                "Focus on improving business metrics",
                "Build credit history",
                "Increase monthly revenue",
                "Reapply in 3-6 months"
            ]
