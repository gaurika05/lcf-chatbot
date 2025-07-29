# LCF Deal Evaluation Assistant

An AI-powered loan deal evaluation tool using Google's Gemini Pro model to assess funding requests based on LCF's internal underwriting rules.

## 🚀 Features

- **Risk Assessment**: Classifies deals as Low, Medium, or High risk
- **Recommendation Engine**: Suggests Approve, Reject, or Manual Review
- **Product Matching**: Recommends suitable LCF products
- **Modern UI**: Clean Streamlit interface for easy interaction

## 📋 Prerequisites

- Python 3.8 or higher
- Google AI Studio API key with access to Gemini Pro model
- Internet connection

## 🛠️ Installation

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd lcf-chatbot
   ```

2. **Create and activate virtual environment**
   ```bash
   python -m venv venv
   
   # On Windows
   venv\Scripts\activate
   
   # On macOS/Linux
   source venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up your API key**

   **Option A: .env file (Recommended for development)**
   ```bash
   # Copy the template
   cp env_template.txt .env
   
   # Edit .env file and add your API key
   GOOGLE_API_KEY=your-actual-api-key-here
   ```

   **Option B: Environment Variable**
   ```bash
   # On Windows
   set GOOGLE_API_KEY=your-api-key-here
   
   # On macOS/Linux
   export GOOGLE_API_KEY=your-api-key-here
   ```

   **Option C: Streamlit Secrets (for deployment)**
   Create a `.streamlit/secrets.toml` file:
   ```toml
   GOOGLE_API_KEY = "your-api-key-here"
   ```

## 🔑 Getting Your API Key

1. Go to [Google AI Studio](https://makersuite.google.com/app/apikey)
2. Sign in with your Google account
3. Click "Create API Key"
4. Copy the generated key
5. Set it as an environment variable (see step 4 above)

## 🧪 Testing

Run the test script to verify your setup:

```bash
python test_gemini.py
```

You should see:
```
🧪 Testing Gemini API Configuration
========================================
🔧 Configuring Gemini API...
🤖 Creating Gemini Pro model...
📝 Testing content generation...
✅ Gemini API is working correctly!
📄 Response: API is working correctly
```

## 🚀 Running the Application

```bash
streamlit run app.py
```

The application will open in your browser at `http://localhost:8501`

## 📊 How to Use

1. **Select Business Industry**: Choose from Retail, Construction, Healthcare, etc.
2. **Enter Monthly Revenue**: Specify the business's monthly revenue in Rs
3. **Set Loan Amount**: Enter the requested loan amount
4. **Choose Loan Type**: Select from Working Capital, Line of Credit, etc.
5. **Specify Business Age**: Indicate how long the business has been operating
6. **Set Tenure**: Choose the requested loan tenure
7. **Click "Evaluate Deal"**: Get AI-powered assessment

## 🔧 Troubleshooting

### Common Issues

**❌ "Google API key not found"**
- Make sure you've created a `.env` file with `GOOGLE_API_KEY=your-key`
- Or set the `GOOGLE_API_KEY` environment variable
- Verify the key is correct and has no extra spaces
- Check that your `.env` file is in the project root directory

**❌ "404 models/gemini-pro is not found"**
- Ensure you're using the latest `google-generativeai` library
- Verify your API key has access to Gemini Pro model
- Check that you're not using any deprecated API versions

**❌ "Failed to configure Gemini API"**
- Check your internet connection
- Verify your API key is valid
- Ensure you have sufficient API quota

### Updating Dependencies

```bash
pip install --upgrade google-generativeai streamlit
```

## 📁 Project Structure

```
lcf-chatbot/
├── app.py              # Main Streamlit application
├── logic.py            # Business logic (currently empty)
├── test_gemini.py      # API testing script
├── requirements.txt    # Python dependencies
├── README.md          # This file
└── prompt_templates/   # Prompt templates directory
    └── deal_prompts.txt
```

## 🔒 Security Notes

- Never commit API keys to version control
- Use environment variables or Streamlit secrets for sensitive data
- Regularly rotate your API keys
- Monitor API usage to avoid unexpected charges

## 📈 Future Enhancements

- [ ] Add more sophisticated risk scoring algorithms
- [ ] Integrate with LCF's internal systems
- [ ] Add historical deal analysis
- [ ] Implement user authentication
- [ ] Add export functionality for evaluations

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## 📄 License

This project is proprietary to LCF Group. All rights reserved.

## 🆘 Support

For technical support or questions about the LCF Deal Evaluation Assistant, please contact the development team.
