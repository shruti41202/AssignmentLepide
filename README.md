# Text Document Summarizer

A web application that allows users to upload text documents and receive summarized versions using a locally deployed Language Model. The application leverages Flask for the backend, React for the frontend, and OpenAI's GPT-3 for summarization.

## Features

- **Upload Documents**: Easily upload text documents for summarization.
- **Receive Summaries**: Get concise summaries of your uploaded documents.
- **User-Friendly Interface**: Enjoy a clean and intuitive user interface.
- **Local Language Model Deployment**: Utilizes OpenAI's GPT-3 via a locally deployed backend.

## Tech Stack

- **Frontend**: React, Axios
- **Backend**: Flask, Transformers, OpenAI GPT-3
- **Styling**: CSS

## Getting Started

Follow the instructions below to set up and run the project locally on your machine.

### Prerequisites

Ensure you have the following software installed:

- [Node.js](https://nodejs.org/) and npm
- [Python 3.x](https://www.python.org/downloads/)
- [Virtualenv](https://virtualenv.pypa.io/en/latest/)

### Installation

#### Backend

1. **Navigate to the backend directory**:
    ```bash
    cd backend
    ```

2. **Create a virtual environment**:
    ```bash
    python -m venv venv
    ```

3. **Activate the virtual environment**:
    - On Windows:
      ```bash
      .\venv\Scripts\activate
      ```
    - On macOS/Linux:
      ```bash
      source venv/bin/activate
      ```

4. **Install the required Python packages**:
    ```bash
    pip install -r requirements.txt
    ```

5. **Set your OpenAI API key**:
    ```bash
    export OPENAI_API_KEY=sk-your-openai-api-key
    ```

6. **Run the Flask application**:
    ```bash
    python app.py
    ```

#### Frontend

1. **Navigate to the frontend directory**:
    ```bash
    cd ..
    cd document-summarizer
    ```

2. **Install the necessary dependencies**:
    ```bash
    npm install
    ```

3. **Start the React application**:
    ```bash
    npm start
    ```

## Usage

Once both the frontend and backend are running, open your browser and navigate to `http://localhost:3000` to access the application. From there, you can upload your text documents and receive summarized outputs.

## Bibliography

- **OpenAI**. (2021). [GPT-3](https://www.openai.com/)
- **Hugging Face**. (2021). [Transformers](https://huggingface.co/transformers/)
- **Flask**. (2021). [Flask Documentation](https://flask.palletsprojects.com/)
- **React**. (2021). [React Documentation](https://reactjs.org/docs/getting-started.html)
- **Node.js**. (2021). [Node.js Documentation](https://nodejs.org/en/docs/)


