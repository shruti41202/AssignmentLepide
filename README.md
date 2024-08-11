### Text Document Summarizer

A web application that allows users to upload text documents and receive summarized versions using a locally deployed Language Model. The application leverages Flask for the backend, React for the frontend, and OpenAI's GPT-3 for summarization.

### Features

- *Upload Documents:* Easily upload text documents for summarization.
- *Receive Summaries:* Get concise summaries of your uploaded documents.
- *User-Friendly Interface:* Enjoy a clean and intuitive user interface.
- *Local Language Model Deployment:* Utilizes OpenAI's GPT-3 via a locally deployed backend.

### Tech Stack

- *Frontend:* React, Axios
- *Backend:* Flask, Transformers, OpenAI GPT-3
- *Styling:* CSS
- *Deployment:* Docker

### Getting Started

Follow the instructions below to set up and run the project locally on your machine.

### Prerequisites

Ensure you have the following software installed:

- Docker and Docker Compose
- Node.js and npm
- Python 3.x
- Virtualenv (if running without Docker)

### Installation

#### Backend

1. *Using Docker:*

   Build and run the Docker container:

  ```bash
   cd backend
  docker-compose up --build
   ```

2. *Without Docker:*

   Navigate to the backend directory:

   ```bash
   cd backend
   ```
   

   Create a virtual environment:

  ```bash
   python -m venv venv
   ```

   Activate the virtual environment:

   On Windows:
   ```bash
   .\venv\Scripts\activate
```
   
   On macOS/Linux:
   ```bash
   source venv/bin/activate
   ```

   Install the required Python packages:

  ```bash
   pip install -r requirements.txt
   ```

   Set your OpenAI API key:

   ```bash
   export OPENAI_API_KEY=sk-your-openai-api-key
   ```

   Run the Flask application:

   ```bash
   python app.py
   ```

#### Frontend

1. *Using Docker:*

   Build and run the Docker container:

  ```bash
   cd ..
   cd document-summarizer
   docker-compose up --build
   ```

2. *Without Docker:*

   Navigate to the frontend directory:

   ```bash
   cd ..
   cd document-summarizer
   ```

   Install the necessary dependencies:

   ```bash
   npm install
   ```

   Start the React application:

   ```bash
   npm start
   ```

### Usage

Once both the frontend and backend are running (either via Docker or manually), open your browser and navigate to [http://localhost:3000](http://localhost:3000) to access the application. From there, you can upload your text documents and receive summarized outputs.

### Bibliography

- OpenAI. (2021). GPT-3
- Hugging Face. (2021). Transformers
- Flask. (2021). Flask Documentation
- React. (2021). React Documentation
- Node.js. (2021). Node.js Documentation
- Docker. (2021). Docker Documentation
