from fastapi import FastAPI, Request, Form, HTTPException
from fastapi.responses import HTMLResponse, FileResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import uvicorn
import os
from pathlib import Path
import json
from typing import Optional
import aiofiles
from datetime import datetime

from services.selenium_generator import SeleniumGenerator
from services.bdd_generator import BDDGenerator

app = FastAPI(title="QA Copilot AI", version="1.0.0")

# Mount static files
app.mount("/static", StaticFiles(directory="static"), name="static")

# Templates
templates = Jinja2Templates(directory="templates")

# Initialize generators
selenium_generator = SeleniumGenerator()
bdd_generator = BDDGenerator()

@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    """Home page with the main interface"""
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/generate-selenium")
async def generate_selenium(
    prompt: str = Form(...),
    browser: str = Form(default="chrome"),
    language: str = Form(default="python")
):
    """Generate Selenium test script from natural language prompt"""
    try:
        script = await selenium_generator.generate_script(prompt, browser, language)
        return {
            "success": True,
            "script": script,
            "filename": f"test_{datetime.now().strftime('%Y%m%d_%H%M%S')}.{language}"
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/generate-bdd")
async def generate_bdd(
    user_story: str = Form(...),
    format_style: str = Form(default="gherkin")
):
    """Generate BDD test cases from user story"""
    try:
        bdd_cases = await bdd_generator.generate_bdd(user_story, format_style)
        return {
            "success": True,
            "bdd_cases": bdd_cases,
            "filename": f"test_cases_{datetime.now().strftime('%Y%m%d_%H%M%S')}.feature"
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/download-script")
async def download_script(
    script_content: str = Form(...),
    filename: str = Form(...)
):
    """Download generated script as file"""
    try:
        # Create downloads directory if it doesn't exist
        downloads_dir = Path("downloads")
        downloads_dir.mkdir(exist_ok=True)
        
        file_path = downloads_dir / filename
        
        async with aiofiles.open(file_path, 'w') as f:
            await f.write(script_content)
        
        return FileResponse(
            path=file_path,
            filename=filename,
            media_type='text/plain'
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000) 