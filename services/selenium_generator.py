import google.generativeai as genai
import os
from typing import Optional
from dotenv import load_dotenv

load_dotenv()

class SeleniumGenerator:
    def __init__(self):
        api_key = os.getenv("GOOGLE_AI_API_KEY")
        if api_key:
            genai.configure(api_key=api_key)
        self.model = genai.GenerativeModel('gemini-pro')
        
    async def generate_script(self, prompt: str, browser: str = "chrome", language: str = "python") -> str:
        """
        Generate Selenium test script from natural language prompt
        
        Args:
            prompt: Natural language description of the test
            browser: Target browser (chrome, firefox)
            language: Programming language (python, javascript)
            
        Returns:
            Generated test script as string
        """
        
        system_prompt = f"""You are an expert QA automation engineer. Generate a complete, runnable {language} test script using Selenium WebDriver for {browser} browser.

Requirements:
1. Use best practices for {language} and Selenium
2. Include proper imports and setup
3. Add meaningful comments
4. Include proper error handling
5. Use explicit waits where appropriate
6. Make the script production-ready
7. Include assertions to verify expected behavior

For {language}:
- Use proper indentation and formatting
- Include try-catch blocks for error handling
- Add docstrings and comments
- Use Page Object Model when appropriate

For JavaScript:
- Use async/await patterns
- Include proper error handling
- Use modern ES6+ syntax
- Add JSDoc comments

Browser setup should be appropriate for {browser}."""

        user_prompt = f"""Generate a Selenium test script for the following scenario:

{prompt}

Requirements:
- Browser: {browser}
- Language: {language}
- Make it production-ready with proper error handling
- Include all necessary imports and setup
- Add meaningful assertions
- Use explicit waits for better reliability"""

        try:
            prompt_text = f"{system_prompt}\n\n{user_prompt}"
            response = self.model.generate_content(prompt_text)
            
            if response.text:
                return response.text
            else:
                return self._generate_fallback_script(prompt, browser, language)
            
        except Exception as e:
            # Fallback to template-based generation if OpenAI fails
            return self._generate_fallback_script(prompt, browser, language)
    
    def _generate_fallback_script(self, prompt: str, browser: str, language: str) -> str:
        """Fallback script generation when OpenAI is not available"""
        
        if language == "python":
            return f'''from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import time

def test_scenario():
    """
    Generated test for: {prompt}
    """
    # Setup Chrome options
    chrome_options = Options()
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    
    # Initialize driver
    driver = webdriver.Chrome(options=chrome_options)
    
    try:
        # Navigate to the application
        driver.get("https://example.com")
        
        # Wait for page to load
        wait = WebDriverWait(driver, 10)
        
        # TODO: Implement test steps based on prompt: {prompt}
        # This is a template - customize based on your specific requirements
        
        # Example test steps:
        # element = wait.until(EC.presence_of_element_located((By.ID, "login-button")))
        # element.click()
        
        # Add assertions
        assert driver.title, "Page title should be present"
        
        print("Test completed successfully!")
        
    except Exception as e:
        print(f"Test failed: {{e}}")
        raise
    finally:
        driver.quit()

if __name__ == "__main__":
    test_scenario()'''
        
        else:  # JavaScript
            return f'''const {{ Builder, By, until }} = require('selenium-webdriver');

async function testScenario() {{
    /**
     * Generated test for: {prompt}
     */
    let driver;
    
    try {{
        // Setup Chrome driver
        driver = await new Builder().forBrowser('{browser}').build();
        
        // Navigate to the application
        await driver.get('https://example.com');
        
        // TODO: Implement test steps based on prompt: {prompt}
        // This is a template - customize based on your specific requirements
        
        // Example test steps:
        // const element = await driver.wait(until.elementLocated(By.id('login-button')), 10000);
        // await element.click();
        
        // Add assertions
        const title = await driver.getTitle();
        console.assert(title, 'Page title should be present');
        
        console.log('Test completed successfully!');
        
    }} catch (error) {{
        console.error('Test failed:', error);
        throw error;
    }} finally {{
        if (driver) {{
            await driver.quit();
        }}
    }}
}}

testScenario();''' 