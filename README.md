# 🤖 AI Meeting Summarizer - Backend API

![Python](https://img.shields.io/badge/Python-3.9%2B-blue?style=flat-square&logo=python)
![FastAPI](https://img.shields.io/badge/FastAPI-0.100%2B-009688?style=flat-square&logo=fastapi)
![NLP](https://img.shields.io/badge/NLP-Transformers-orange?style=flat-square)
![Status](https://img.shields.io/badge/Status-Active-success?style=flat-square)

## 📝 Overview

A powerful **FastAPI-based backend** for the AI Meeting Summarizer application. This API leverages advanced **Natural Language Processing (NLP)** and **Large Language Models (LLMs)** to automatically transcribe, analyze, and summarize meeting recordings with intelligent key point extraction and action item detection.

## ✨ Key Features

- 🎤 **Speech-to-Text**: Automatic transcription of meeting audio
- 🧠 **AI-Powered Summarization**: Extract key insights using transformer models
- 🎯 **Action Item Detection**: Automatically identify tasks and action items
- 📊 **Analytics**: Meeting statistics and participation analysis
- ⚡ **Fast API**: High-performance asynchronous endpoints
- 🔒 **Secure**: API authentication and data encryption
- 📦 **RESTful Design**: Clean and intuitive API endpoints

## 🛠️ Tech Stack

- **Framework**: FastAPI (Python 3.9+)
- **NLP**: Hugging Face Transformers
- **Speech Recognition**: Whisper / SpeechRecognition
- **LLM**: GPT models / BART for summarization
- **Database**: SQLite / PostgreSQL
- **Authentication**: JWT tokens
- **Deployment**: Docker, Uvicorn

## 🚀 Quick Start

### Prerequisites

```bash
python >= 3.9
pip
```

### Installation

1. **Clone the repository**
```bash
git clone https://github.com/amalsp220/AI-MEETING-SUMMARIZER-BACKEND.git
cd AI-MEETING-SUMMARIZER-BACKEND
```

2. **Create virtual environment**
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. **Install dependencies**
```bash
pip install -r requirements.txt
```

4. **Set up environment variables**
```bash
cp .env.example .env
# Edit .env with your configuration
```

5. **Run the server**
```bash
uvicorn main:app --reload
```

6. **Access API documentation**
```
http://localhost:8000/docs
```

## 📚 API Endpoints

### Meeting Management

```
POST   /api/meetings/upload          # Upload meeting audio
GET    /api/meetings/{id}            # Get meeting details
GET    /api/meetings/                # List all meetings
DELETE /api/meetings/{id}            # Delete meeting
```

### Summarization

```
POST   /api/summarize/transcribe     # Transcribe audio to text
POST   /api/summarize/analyze        # Analyze meeting content
GET    /api/summarize/summary/{id}   # Get meeting summary
GET    /api/summarize/actions/{id}   # Get action items
```

### Analytics

```
GET    /api/analytics/stats          # Overall statistics
GET    /api/analytics/trends         # Meeting trends
```

## 📁 Project Structure

```
AI-MEETING-SUMMARIZER-BACKEND/
│
├── main.py                 # FastAPI application entry point
├── requirements.txt        # Python dependencies
├── .env.example            # Environment variables template
├── models/                 # ML models and weights
├── routers/                # API route handlers
├── services/               # Business logic
├── utils/                  # Helper functions
└── tests/                  # Unit and integration tests
```

## 🧠 ML Pipeline

### 1. Speech-to-Text
- Uses Whisper or Google Speech Recognition
- Supports multiple audio formats
- Speaker diarization

### 2. Text Summarization
- BART/T5 transformer models
- Extractive and abstractive summarization
- Customizable summary length

### 3. Action Item Extraction
- Named Entity Recognition (NER)
- Dependency parsing
- Custom rule-based extraction

## 📊 Example Response

```json
{
  "meeting_id": "123abc",
  "summary": "Team discussed Q4 roadmap and feature priorities...",
  "key_points": [
    "Finalize authentication module by end of month",
    "Schedule design review for new dashboard"
  ],
  "action_items": [
    {
      "task": "Update documentation",
      "assignee": "John",
      "due_date": "2024-12-01"
    }
  ],
  "participants": ["John", "Sarah", "Mike"],
  "duration": "45 minutes"
}
```

## 🔧 Configuration

### Environment Variables

```bash
API_KEY=your_api_key
DATABASE_URL=sqlite:///./meetings.db
MODEL_PATH=./models/
MAX_AUDIO_SIZE=50MB
ALLOWED_FORMATS=mp3,wav,m4a
```

## 🐳 Docker Deployment

```bash
# Build image
docker build -t ai-meeting-summarizer-backend .

# Run container
docker run -p 8000:8000 ai-meeting-summarizer-backend
```

## 🛡️ Security Features

- JWT-based authentication
- API rate limiting
- Input validation and sanitization
- CORS configuration
- Encrypted data storage

## 🎯 Performance Optimization

- Async/await for non-blocking operations
- Background tasks for long-running processes
- Response caching
- Database connection pooling
- Model optimization (quantization)

## 📦 Dependencies

```bash
fastapi
uvicorn[standard]
transformers
torch
speech_recognition
pydub
python-multipart
python-jose[cryptography]
passlib[bcrypt]
```

## 🤝 Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit changes (`git commit -m 'Add AmazingFeature'`)
4. Push to branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License.

## 👤 Author

**Amal S P**
- GitHub: [@amalsp220](https://github.com/amalsp220)
- LinkedIn: [amalsp220](https://linkedin.com/in/amalsp220)
- Portfolio: [amalsp220.github.io](https://amalsp220.github.io/amal-portfolio)

## 🚀 Related Projects

- [AI Meeting Summarizer Frontend](https://github.com/amalsp220/AI-MEETING-SUMMARIZER)

## 🔗 Resources

- [FastAPI Documentation](https://fastapi.tiangolo.com/)
- [Hugging Face Transformers](https://huggingface.co/transformers/)
- [Whisper by OpenAI](https://github.com/openai/whisper)

---

<div align="center">

**Built with ❤️ using FastAPI and Transformers**

⭐ Star this repo if you find it helpful!

</div>
