#!/usr/bin/env python3
"""
QA Copilot AI - Startup Script
"""

import os
import sys
from pathlib import Path

def check_environment():
    """Check if environment is properly configured"""
    env_file = Path('.env')
    
    if not env_file.exists():
        print("⚠️  Environment file not found!")
        print("📝 Creating .env file from template...")
        
        try:
            # Copy from env.example if it exists
            example_file = Path('env.example')
            if example_file.exists():
                with open(example_file, 'r') as f:
                    content = f.read()
                with open(env_file, 'w') as f:
                    f.write(content)
                print("✅ Created .env file from template")
                print("🔑 Please edit .env and add your OpenAI API key")
                return False
            else:
                print("❌ env.example not found")
                return False
        except Exception as e:
            print(f"❌ Error creating .env file: {e}")
            return False
    
    # Check if Google AI API key is configured
    from dotenv import load_dotenv
    load_dotenv()
    
    api_key = os.getenv('GOOGLE_AI_API_KEY')
    if not api_key or api_key == 'your_google_ai_api_key_here':
        print("⚠️  Google AI API key not configured!")
        print("🔑 Please edit .env and add your Google AI API key")
        print("📖 Get your API key from: https://makersuite.google.com/app/apikey")
        return False
    
    return True

def check_dependencies():
    """Check if required dependencies are installed"""
    try:
        import fastapi
        import uvicorn
        import openai
        print("✅ All dependencies are installed")
        return True
    except ImportError as e:
        print(f"❌ Missing dependency: {e}")
        print("📦 Please run: pip install -r requirements.txt")
        return False

def main():
    """Main startup function"""
    print("🤖 QA Copilot AI - Starting up...")
    print("=" * 50)
    
    # Check dependencies
    if not check_dependencies():
        sys.exit(1)
    
    # Check environment
    if not check_environment():
        print("\n💡 You can still run the app without Google AI API key")
        print("   It will use fallback templates for testing")
        response = input("Continue anyway? (y/N): ")
        if response.lower() != 'y':
            sys.exit(0)
    
    # Start the application
    print("\n🚀 Starting QA Copilot AI...")
    print("🌐 Open your browser to: http://localhost:8000")
    print("⏹️  Press Ctrl+C to stop the server")
    print("=" * 50)
    
    try:
        import uvicorn
        uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
    except KeyboardInterrupt:
        print("\n👋 Goodbye!")
    except Exception as e:
        print(f"❌ Error starting server: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main() 