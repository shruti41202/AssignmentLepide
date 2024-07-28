import React, { useState } from 'react';
import axios from 'axios';
import './App.css';

function App() {
  const [selectedFile, setSelectedFile] = useState(null);
  const [summary, setSummary] = useState("");
  const [error, setError] = useState("");

  const handleFileChange = (event) => {
    setSelectedFile(event.target.files[0]);
  };

  const handleSubmit = async (event) => {
    event.preventDefault();
    if (!selectedFile) {
      alert("Please select a file first!");
      return;
    }

    const formData = new FormData();
    formData.append("file", selectedFile);

    try {
      // Upload the file
      const uploadResponse = await axios.post('http://localhost:5000/upload', formData);
      const { file_path } = uploadResponse.data;

      // Summarize the uploaded file
      const summarizeResponse = await axios.post('http://localhost:5000/summarize', { file_path });
      setSummary(summarizeResponse.data.summary);
      setError(""); // Clear any previous errors
    } catch (error) {
      console.error('Error:', error);
      setError('Error in summarization. Please try again.');
    }
  };

  return (
    <div className="App">
      <h1>Document Summarizer</h1>
      <form onSubmit={handleSubmit}>
        <input type="file" onChange={handleFileChange} />
        <button type="submit">Upload and Summarize</button>
      </form>
      {summary && (
        <div>
          <h2>Summary</h2>
          <textarea value={summary} readOnly rows={10} cols={80} />
        </div>
      )}
      {error && <p style={{ color: 'red' }}>{error}</p>}
    </div>
  );
}

export default App;
