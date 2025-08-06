# QA Copilot AI 🤖

An LLM-powered QA assistant that transforms natural language input into automated test assets. This tool bridges the gap between product requirements and test implementation, making automated testing accessible to all stakeholders.

## 🚀 Features

### 1. Selenium Script Generator
- **Input**: Natural language test scenarios
- **Output**: Ready-to-run Selenium test scripts
- **Options**: 
  - Browser: Chrome, Firefox
  - Language: Python, JavaScript
  - Download as `.py` or `.js` files

### 2. BDD Test Case Generator
- **Input**: User stories or product requirements
- **Output**: Structured BDD test cases in Gherkin format
- **Options**:
  - Export as `.feature` file
  - Copy to clipboard
  - Multiple formats: Gherkin, Checklist, Plain Text

## 🛠️ Tech Stack

- **Backend**: FastAPI (Python)
- **Frontend**: HTML5, CSS3, JavaScript (Vanilla)
- **AI**: Google AI (Gemini Pro)
- **Styling**: Custom CSS with modern design
- **Browser Automation**: Selenium WebDriver

## 📋 Prerequisites

- Python 3.8+
- Google AI API key
- Modern web browser

## 🚀 Quick Start

### 1. Clone the Repository
```bash
git clone <repository-url>
cd QA-Copilot
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

### 3. Configure Environment
```bash
# Copy the example environment file
cp env.example .env

# Edit .env and add your Google AI API key
GOOGLE_AI_API_KEY=your_actual_api_key_here
```

### 4. Run the Application
```bash
python main.py
```

### 5. Access the Application
Open your browser and navigate to: `http://localhost:8000`

## 📖 Usage Examples

### Selenium Script Generator

**Input:**
```
"Test the login page with invalid email format and check for error message."
```

**Output:** Complete Python Selenium script with proper error handling, explicit waits, and assertions.

### BDD Test Case Generator

**Input:**
```
"As a user, I want to reset my password so I can regain account access if I forget it."
```

**Output:** Comprehensive Gherkin feature file with multiple scenarios covering happy path, edge cases, and error conditions.

## 🎯 Key Features

### ✨ Modern UI/UX
- Clean, responsive design
- Tab-based navigation
- Real-time feedback
- Loading animations
- Copy-to-clipboard functionality
- File download capabilities

### 🔧 Smart Generation
- Fallback templates when OpenAI is unavailable
- Multiple output formats
- Best practices integration
- Error handling
- Production-ready code

### 📱 Responsive Design
- Mobile-friendly interface
- Keyboard shortcuts (Ctrl+Enter to submit)
- Auto-resizing textareas
- Touch-friendly buttons

## 🏗️ Project Structure

```
QA-Copilot/
├── main.py                 # FastAPI application
├── requirements.txt        # Python dependencies
├── env.example            # Environment configuration example
├── README.md              # This file
├── services/              # Core business logic
│   ├── __init__.py
│   ├── selenium_generator.py  # Selenium script generation
│   └── bdd_generator.py       # BDD test case generation
├── templates/             # HTML templates
│   └── index.html         # Main application template
├── static/               # Static assets
│   ├── css/
│   │   └── style.css     # Application styles
│   └── js/
│       └── script.js     # Frontend JavaScript
└── downloads/            # Generated files (created automatically)
```

## 🔧 Configuration

### Environment Variables

| Variable | Description | Required | Default |
|----------|-------------|----------|---------|
| `OPENAI_API_KEY` | Your OpenAI API key | Yes | - |
| `OPENAI_MODEL` | OpenAI model to use | No | `gpt-4` |
| `HOST` | Server host | No | `0.0.0.0` |
| `PORT` | Server port | No | `8000` |

### API Endpoints

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/` | GET | Main application interface |
| `/generate-selenium` | POST | Generate Selenium scripts |
| `/generate-bdd` | POST | Generate BDD test cases |
| `/download-script` | POST | Download generated files |

## 🧪 Testing

The application includes fallback templates that work without a Google AI API key for testing purposes.

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Submit a pull request

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🙏 Acknowledgments

- Google AI for providing the Gemini Pro API
- FastAPI for the excellent web framework
- The Selenium community for browser automation tools

## 🆘 Support

If you encounter any issues:

1. Check that your Google AI API key is correctly configured
2. Ensure all dependencies are installed
3. Check the browser console for JavaScript errors
4. Verify your internet connection for API calls

## 🔮 Future Enhancements

- [ ] Support for Playwright scripts
- [ ] Integration with test management tools
- [ ] Custom test templates
- [ ] Batch processing capabilities
- [ ] API rate limiting and caching
- [ ] User authentication and project management
- [ ] Integration with CI/CD pipelines

---

**Made with ❤️ for the QA community** 