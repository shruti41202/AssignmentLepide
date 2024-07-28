# Document Summarizer


A web application that allows users to upload text documents and receive summarized versions using a locally deployed Language Model. The application is built with a Flask backend and a React frontend.

## Features

- Upload text documents for summarization
- Receive concise summaries of the uploaded documents
- User-friendly interface
- Utilizes OpenAI's GPT-3 for summarization

## Tech Stack

- *Frontend*: React, Axios
- *Backend*: Flask, Transformers, OpenAI GPT-3
- *Styling*: CSS

## Getting Started

Follow these instructions to set up the project locally on your machine.

### Prerequisites

Make sure you have the following installed:

- Node.js and npm
- Python 3.x
- Virtualenv

# Installation
### Backend

- Setting up the Backend
-  cd backend
-  \venv\Scripts\activate
-  pip install -r requirements.txt
-  OPENAI_API_KEY=sk-your-openai-api-key
-  python app.py

 ### Frontend
 - cd ../frontend
 - npm install
 - npm start
