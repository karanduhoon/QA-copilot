// Global variables to store generated content
let currentSeleniumScript = '';
let currentBDDCases = '';
let currentSeleniumFilename = '';
let currentBDDFilename = '';

// Tab switching functionality
document.addEventListener('DOMContentLoaded', function() {
    const tabButtons = document.querySelectorAll('.tab-button');
    const tabContents = document.querySelectorAll('.tab-content');

    tabButtons.forEach(button => {
        button.addEventListener('click', () => {
            const targetTab = button.getAttribute('data-tab');
            
            // Remove active class from all buttons and contents
            tabButtons.forEach(btn => btn.classList.remove('active'));
            tabContents.forEach(content => content.classList.remove('active'));
            
            // Add active class to clicked button and corresponding content
            button.classList.add('active');
            document.getElementById(`${targetTab}-tab`).classList.add('active');
        });
    });

    // Form submissions
    setupSeleniumForm();
    setupBDDForm();
});

// Selenium form setup
function setupSeleniumForm() {
    const form = document.getElementById('selenium-form');
    form.addEventListener('submit', async (e) => {
        e.preventDefault();
        
        const formData = new FormData(form);
        const prompt = formData.get('prompt');
        const browser = formData.get('browser');
        const language = formData.get('language');
        
        if (!prompt.trim()) {
            showMessage('Please enter a test scenario description.', 'error');
            return;
        }
        
        showLoading(true);
        
        try {
            const response = await fetch('/generate-selenium', {
                method: 'POST',
                body: formData
            });
            
            const result = await response.json();
            
            if (result.success) {
                currentSeleniumScript = result.script;
                currentSeleniumFilename = result.filename;
                displaySeleniumResult(result.script);
                showMessage('Selenium script generated successfully!', 'success');
            } else {
                showMessage('Failed to generate script. Please try again.', 'error');
            }
        } catch (error) {
            console.error('Error:', error);
            showMessage('An error occurred. Please check your connection and try again.', 'error');
        } finally {
            showLoading(false);
        }
    });
}

// BDD form setup
function setupBDDForm() {
    const form = document.getElementById('bdd-form');
    form.addEventListener('submit', async (e) => {
        e.preventDefault();
        
        const formData = new FormData(form);
        const userStory = formData.get('user_story');
        const formatStyle = formData.get('format_style');
        
        if (!userStory.trim()) {
            showMessage('Please enter a user story or product requirement.', 'error');
            return;
        }
        
        showLoading(true);
        
        try {
            const response = await fetch('/generate-bdd', {
                method: 'POST',
                body: formData
            });
            
            const result = await response.json();
            
            if (result.success) {
                currentBDDCases = result.bdd_cases;
                currentBDDFilename = result.filename;
                displayBDDResult(result.bdd_cases);
                showMessage('BDD test cases generated successfully!', 'success');
            } else {
                showMessage('Failed to generate BDD cases. Please try again.', 'error');
            }
        } catch (error) {
            console.error('Error:', error);
            showMessage('An error occurred. Please check your connection and try again.', 'error');
        } finally {
            showLoading(false);
        }
    });
}

// Display Selenium result
function displaySeleniumResult(script) {
    const resultContainer = document.getElementById('selenium-result');
    const codeElement = document.getElementById('selenium-code');
    
    codeElement.textContent = script;
    resultContainer.style.display = 'block';
    
    // Scroll to result
    resultContainer.scrollIntoView({ behavior: 'smooth' });
}

// Display BDD result
function displayBDDResult(bddCases) {
    const resultContainer = document.getElementById('bdd-result');
    const codeElement = document.getElementById('bdd-code');
    
    codeElement.textContent = bddCases;
    resultContainer.style.display = 'block';
    
    // Scroll to result
    resultContainer.scrollIntoView({ behavior: 'smooth' });
}

// Copy to clipboard functionality
function copyToClipboard(elementId) {
    const element = document.getElementById(elementId);
    const text = element.textContent;
    
    if (navigator.clipboard) {
        navigator.clipboard.writeText(text).then(() => {
            showMessage('Copied to clipboard!', 'success');
        }).catch(err => {
            console.error('Failed to copy: ', err);
            fallbackCopyToClipboard(text);
        });
    } else {
        fallbackCopyToClipboard(text);
    }
}

// Fallback copy method for older browsers
function fallbackCopyToClipboard(text) {
    const textArea = document.createElement('textarea');
    textArea.value = text;
    textArea.style.position = 'fixed';
    textArea.style.left = '-999999px';
    textArea.style.top = '-999999px';
    document.body.appendChild(textArea);
    textArea.focus();
    textArea.select();
    
    try {
        document.execCommand('copy');
        showMessage('Copied to clipboard!', 'success');
    } catch (err) {
        console.error('Fallback copy failed: ', err);
        showMessage('Failed to copy to clipboard.', 'error');
    }
    
    document.body.removeChild(textArea);
}

// Download script functionality
function downloadScript(type) {
    let content, filename;
    
    if (type === 'selenium') {
        content = currentSeleniumScript;
        filename = currentSeleniumFilename;
    } else if (type === 'bdd') {
        content = currentBDDCases;
        filename = currentBDDFilename;
    } else {
        showMessage('Invalid download type.', 'error');
        return;
    }
    
    if (!content) {
        showMessage('No content to download. Please generate something first.', 'error');
        return;
    }
    
    // Create download form
    const form = document.createElement('form');
    form.method = 'POST';
    form.action = '/download-script';
    
    const contentInput = document.createElement('input');
    contentInput.type = 'hidden';
    contentInput.name = 'script_content';
    contentInput.value = content;
    
    const filenameInput = document.createElement('input');
    filenameInput.type = 'hidden';
    filenameInput.name = 'filename';
    filenameInput.value = filename;
    
    form.appendChild(contentInput);
    form.appendChild(filenameInput);
    document.body.appendChild(form);
    form.submit();
    document.body.removeChild(form);
}

// Show/hide loading overlay
function showLoading(show) {
    const overlay = document.getElementById('loading-overlay');
    overlay.style.display = show ? 'flex' : 'none';
}

// Show message
function showMessage(message, type = 'success') {
    // Remove existing messages
    const existingMessages = document.querySelectorAll('.message');
    existingMessages.forEach(msg => msg.remove());
    
    // Create new message
    const messageDiv = document.createElement('div');
    messageDiv.className = `message ${type}`;
    messageDiv.textContent = message;
    
    // Insert at the top of the main content
    const mainContent = document.querySelector('.main-content');
    mainContent.insertBefore(messageDiv, mainContent.firstChild);
    
    // Auto-remove after 5 seconds
    setTimeout(() => {
        if (messageDiv.parentNode) {
            messageDiv.remove();
        }
    }, 5000);
}

// Auto-resize textareas
document.addEventListener('DOMContentLoaded', function() {
    const textareas = document.querySelectorAll('textarea');
    textareas.forEach(textarea => {
        textarea.addEventListener('input', function() {
            this.style.height = 'auto';
            this.style.height = this.scrollHeight + 'px';
        });
    });
});

// Keyboard shortcuts
document.addEventListener('keydown', function(e) {
    // Ctrl/Cmd + Enter to submit forms
    if ((e.ctrlKey || e.metaKey) && e.key === 'Enter') {
        const activeTab = document.querySelector('.tab-content.active');
        const form = activeTab.querySelector('form');
        if (form) {
            form.dispatchEvent(new Event('submit'));
        }
    }
    
    // Escape to hide loading overlay
    if (e.key === 'Escape') {
        showLoading(false);
    }
}); 