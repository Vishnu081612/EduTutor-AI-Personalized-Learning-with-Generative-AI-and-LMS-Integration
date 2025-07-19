# 🎓 EduTutor AI

EduTutor AI is a personalized learning platform using IBM Watsonx, Granite LLMs, and Google Classroom.

## 🔧 Features
- AI-generated quizzes
- Diagnostic testing
- Google Classroom integration
- Real-time educator dashboard
- Pinecone-powered memory

## 🧪 Run Locally

```bash
git clone https://github.com/yourusername/edututor-ai.git
cd edututor-ai
pip install -r requirements.txt
uvicorn main:app --reload
streamlit run frontend/dashboard.py

