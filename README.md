# QA Copilot AI

An LLM-powered QA assistant that transforms natural language input into automated test assets using Google AI (Gemini Pro).

## Features

### Selenium Script Generator
- Input: Natural language test scenarios
- Output: Ready-to-run Selenium test scripts
- Options: Chrome/Firefox, Python/JavaScript
- Download as .py or .js files

### BDD Test Case Generator
- Input: User stories or product requirements
- Output: Structured BDD test cases
- Formats: Gherkin (.feature), Checklist, Plain Text
- Copy to clipboard or download

## Tech Stack

- Backend: FastAPI (Python)
- Frontend: HTML5, CSS3, JavaScript
- AI: Google AI (Gemini Pro)
- Browser Automation: Selenium WebDriver

## Prerequisites

- Python 3.8+
- Google AI API key
- Modern web browser

## Quick Start

1. **Clone the repository**
   ```bash
   git clone https://github.com/karanduhoon/QA-copilot.git
   cd QA-copilot
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Configure environment**
   ```bash
   cp env.example .env
   # Edit .env and add your Google AI API key
   GOOGLE_AI_API_KEY=your_api_key_here
   ```

4. **Run the application**
   ```bash
   python run.py
   ```

5. **Access the application**
   Open http://localhost:8000 in your browser

## Usage Examples

### Selenium Script Generator
Input: "Test the login page with invalid email format and check for error message."
Output: Complete Python Selenium script with proper error handling and assertions.

### BDD Test Case Generator
Input: "As a user, I want to reset my password so I can regain account access if I forget it."
Output: Comprehensive Gherkin feature file with multiple scenarios.

## Project Structure

```
QA-Copilot/
├── main.py                 # FastAPI application
├── run.py                  # Startup script
├── requirements.txt        # Python dependencies
├── services/              # AI generators
│   ├── selenium_generator.py
│   └── bdd_generator.py
├── templates/             # HTML templates
├── static/               # CSS/JS assets
└── downloads/            # Generated files
```

## Configuration

### Environment Variables

| Variable | Description | Required |
|----------|-------------|----------|
| `GOOGLE_AI_API_KEY` | Google AI API key | Yes |

Get your API key from: https://makersuite.google.com/app/apikey

## API Endpoints

- `GET /` - Main application interface
- `POST /generate-selenium` - Generate Selenium scripts
- `POST /generate-bdd` - Generate BDD test cases
- `POST /download-script` - Download generated files

## Development

The application includes fallback templates that work without a Google AI API key for testing purposes.

## License

MIT License 