# LCF AI Assistant 🤖

A comprehensive, empathetic AI chatbot for LCF Group that provides company information, handles customer queries, and includes advanced deal evaluation capabilities.

## 🌟 Features

### 💬 **General Chat Mode**
- **Company Information**: Learn about LCF Group, our mission, and values
- **Product Guidance**: Explore financing options and understand terms
- **Eligibility Check**: Review requirements and qualification criteria
- **Contact & Support**: Get contact information and office hours
- **Empathetic Responses**: Warm, professional, and helpful interactions

### 📊 **Deal Evaluation Mode**
- **AI-Powered Assessment**: Quick loan evaluation using advanced algorithms
- **Risk Analysis**: Low/Medium/High risk classification
- **Product Recommendations**: Suggest the most suitable financing option
- **Loan Terms**: Provide suggested amounts, rates, and tenures
- **Next Steps**: Clear guidance on what to do next

### 🎯 **Key Capabilities**
- **Intent Recognition**: Understands user queries and responds appropriately
- **Context Awareness**: Maintains conversation context
- **Multi-Modal Interface**: Seamless switching between chat and evaluation modes
- **Professional Design**: Clean, modern UI with intuitive navigation

## 🚀 Quick Start

### Prerequisites
- Python 3.8+
- Google Gemini API key
- Required Python packages (see requirements.txt)

### Installation

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd lcf-chatbot
   ```

2. **Set up virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure environment variables**
   Create a `.env` file in the root directory:
   ```
   GOOGLE_API_KEY=your_gemini_api_key_here
   ```

5. **Run the application**
   ```bash
   streamlit run app.py
   ```

## 📁 Project Structure

```
lcf-chatbot/
├── app.py                 # Main Streamlit application
├── logic.py              # Core chatbot logic and business rules
├── prompt_templates/     # AI prompt templates
│   └── deal_prompts.txt  # Deal evaluation prompts
├── assets/              # Static assets (images, etc.)
├── venv/               # Virtual environment
└── README.md           # This file
```

## 🎮 How to Use

### General Chat Mode
1. Select "💬 General Chat" from the sidebar
2. Ask questions about LCF Group, products, or eligibility
3. Use quick action buttons for common queries
4. Get empathetic, informative responses

### Deal Evaluation Mode
1. Select "📊 Deal Evaluation" from the sidebar
2. Fill in your business details:
   - Industry
   - Monthly revenue
   - Loan amount needed
   - Business age
   - Credit score
3. Click "Evaluate Deal" for instant AI assessment
4. Review comprehensive evaluation results

### Quick Actions
Use the sidebar buttons for instant access to:
- 🏢 About LCF
- 💰 Our Products
- 📋 Eligibility
- 📞 Contact Info

## 🧠 AI Capabilities

### Intent Recognition
The chatbot understands various types of queries:
- **Company Information**: "Tell me about LCF", "What does LCF do?"
- **Products**: "What loans do you offer?", "Tell me about working capital"
- **Eligibility**: "Do I qualify?", "What documents do I need?"
- **Contact**: "How can I reach you?", "What are your office hours?"
- **Application**: "How do I apply?", "What's the process?"

### Deal Evaluation Logic
Advanced risk assessment based on:
- **Revenue Analysis**: Monthly revenue patterns and stability
- **Loan-to-Revenue Ratio**: Risk assessment based on borrowing amount
- **Business Age**: Experience and stability factors
- **Credit Score**: Creditworthiness evaluation
- **Industry Factors**: Sector-specific considerations

## 🎨 UI/UX Features

### Modern Design
- **Responsive Layout**: Works on desktop and mobile
- **Clean Interface**: Professional, easy-to-navigate design
- **Visual Hierarchy**: Clear information organization
- **Interactive Elements**: Engaging buttons and forms

### User Experience
- **Conversation History**: Maintains chat context
- **Quick Actions**: One-click access to common queries
- **Progress Indicators**: Loading states and feedback
- **Error Handling**: Graceful error management

## 🔧 Configuration

### Environment Variables
- `GOOGLE_API_KEY`: Your Google Gemini API key

### Customization
You can customize the chatbot by modifying:
- `logic.py`: Business logic and response generation
- `prompt_templates/deal_prompts.txt`: AI prompt templates
- Company information in the knowledge base

## 📊 Deal Evaluation Criteria

### Risk Levels
- **Low Risk**: High approval probability
- **Medium Risk**: Requires manual review
- **High Risk**: Likely rejection with improvement suggestions

### Factors Considered
1. **Monthly Revenue**: Stability and amount
2. **Business Age**: Experience and track record
3. **Credit Score**: Creditworthiness
4. **Loan Amount**: Reasonableness vs. revenue
5. **Industry**: Sector stability and growth potential

## 🤝 Support

### For Users
- **In-App Chat**: Use the chatbot for immediate assistance
- **Contact Information**: Available in the chat interface
- **Office Hours**: Monday-Friday, 9 AM - 6 PM

### For Developers
- **Documentation**: This README and inline code comments
- **Code Structure**: Modular design for easy maintenance
- **Extensibility**: Easy to add new features and capabilities

## 🔒 Security & Privacy

- **API Key Security**: Environment variable protection
- **Data Privacy**: No sensitive data stored permanently
- **Session Management**: Secure session handling
- **Input Validation**: Proper data validation and sanitization

## 🚀 Future Enhancements

### Planned Features
- **Multi-language Support**: Hindi and other regional languages
- **Voice Integration**: Speech-to-text and text-to-speech
- **Document Upload**: Direct document submission
- **Integration APIs**: Connect with external systems
- **Analytics Dashboard**: Usage analytics and insights

### Potential Integrations
- **CRM Systems**: Customer relationship management
- **Loan Management**: Direct loan application processing
- **Payment Gateways**: Online payment processing
- **Email Systems**: Automated email notifications

## 📝 License

This project is proprietary to LCF Group. All rights reserved.

## 👥 Contributing

For internal development:
1. Follow the existing code structure
2. Add comprehensive documentation
3. Test thoroughly before deployment
4. Follow security best practices

---

**Built with ❤️ for LCF Group**

*Empowering businesses with smart financial solutions*
