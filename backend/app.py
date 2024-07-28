from flask import Flask, request, jsonify
from flask_cors import CORS
from transformers import pipeline
import openai
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

app = Flask(__name__)
CORS(app)

# Load OpenAI API key from environment variable
openai.api_key = os.getenv('OPENAI_API_KEY')

# Initialize the summarization pipeline for local summarization
summarizer = pipeline("summarization")

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'}), 400
    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400
    if not file.filename.endswith(('.txt', '.pdf', '.docx')):
        return jsonify({'error': 'Unsupported file type. Please upload a text file, PDF, or DOCX.'}), 400
    
    file_path = os.path.join('uploads', file.filename)
    file.save(file_path)
    return jsonify({'message': 'File uploaded successfully', 'file_path': file_path}), 200

@app.route('/summarize', methods=['POST'])
def summarize_document():
    data = request.get_json()
    file_path = data.get('file_path')
    if not file_path or not os.path.exists(file_path):
        return jsonify({"error": "File not found"}), 400
    
    with open(file_path, 'r') as file:
        text = file.read()

    try:
        # Choose whether to use OpenAI or local summarizer based on file size
        if len(text) > 1000:  # Use OpenAI for larger texts
            response = openai.Completion.create(
                engine="text-davinci-003",
                prompt=f"Summarize the following document:\n\n{text}",
                max_tokens=150
            )
            summary = response.choices[0].text.strip()
        else:  # Use local summarizer for smaller texts
            summary = summarizer(text, max_length=150, min_length=50, do_sample=False)[0]['summary_text']

        return jsonify({"summary": summary}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    # Ensure the upload folder exists
    if not os.path.exists('uploads'):
        os.makedirs('uploads')
    app.run(debug=True)
