# Gemini AI Chatbot Using Python Flask

## Project Overview

This project is a simple AI-powered chatbot developed using **Python, Flask, and Google's Gemini AI API**.

The application allows users to enter questions through a web-based interface. Flask receives the user's input, sends it to the Gemini AI model, and displays the AI-generated response on the webpage.

This project demonstrates how to integrate Generative AI into a Python web application using API integration.

## Features

- User-friendly chatbot interface.
- Integration with Google Gemini AI.
- Real-time AI-generated responses.
- Flask-based web application.
- HTML form handling using GET and POST methods.
- Error handling using try-except.
- Secure API key management using environment variables.

## 🛠️ Technologies Used

| Technology | Purpose |
|---|---|
| Python | Backend programming |
| Flask | Web application framework |
| Google Gemini AI | Generative AI model |
| HTML | Frontend structure |
| Jinja2 | Dynamic HTML rendering |
| Google GenAI SDK | Gemini API integration |
| Python-dotenv | Environment variable management |

##  Project Structure

```text
Gemini_Chatbot/
│
├── app.py
├── config.py
├── .env
├── .gitignore
│
└── templates/
    └── index.html
```

##  Installation and Setup

### Step 1: Clone the Repository

```bash
git clone https://github.com/your-username/Gemini_Chatbot.git
```

### Step 2: Navigate to the Project Directory

```bash
cd Gemini_Chatbot
```

### Step 3: Install Required Libraries

```bash
pip install flask google-genai python-dotenv
```

### Step 4: Generate Gemini API Key

1. Visit [Google AI Studio](https://aistudio.google.com/).
2. Generate your Gemini API key.
3. Copy the API key.

### Step 5: Configure Environment Variables

Create a `.env` file in the project directory.

```env
GEMINI_API_KEY=your_actual_api_key
```

### Step 6: Create config.py

```python
from dotenv import load_dotenv
import os

load_dotenv()

def getkey():
    return os.getenv("GEMINI_API_KEY")
```

### Step 7: Run the Application

```bash
python app.py
```

### Step 8: Open the Application

<img width="935" height="593" alt="image" src="https://github.com/user-attachments/assets/590e25b2-7f38-412d-bda5-6ed952fb3770" />

```

##  Application Workflow

1. User opens the chatbot webpage.
2. User enters a question in the input field.
3. Flask receives the question through an HTTP POST request.
4. The question is sent to the Google Gemini AI model.
5. Gemini generates an AI response.
6. Flask receives the response.
7. The answer is displayed on the webpage.

##  Key Python Concepts Covered

- Python modules and packages
- Functions and variables
- Flask application development
- URL routing
- HTTP GET and POST methods
- HTML form handling
- API integration
- Exception handling
- Environment variables
- Dynamic HTML rendering using Jinja2

## Future Enhancements

- Chat history management.
- Improved chatbot UI using Bootstrap.
- User authentication and login system.
- Multiple conversation support.
- Download chatbot responses.
- Integration with a database such as MySQL.
- ## Project Google drive link:
- https://drive.google.com/drive/folders/1R_P7kP877ZCaFi_C29xCB18s7eFSBNsE?usp=sharing

## Author

**Sayan Sau – CoE Kolkata**

Project: Gemini AI Chatbot Using Python Flask

##  License

This project is created for educational and learning purposes. Special Thanks to Amitava Sir (CoE Kolkata).

---

⭐ If you find this project useful, consider giving the repository a star!
