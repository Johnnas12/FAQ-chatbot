# 📌 FAQ Chatbot with MeTTa & FastAPI

## 🚀 Project Overview
This is a **domain-specific FAQ chatbot** that integrates **MeTTa** for knowledge graph-based reasoning and **FastAPI** for serving responses via an API. Unlike traditional chatbots that rely only on predefined responses, this chatbot:

✅ **Understands structured relationships** in FAQs.
✅ **Fetches real-time domain-specific insights** dynamically.
✅ **Provides accurate, fact-enriched responses**.
✅ **Is easily extensible** to new knowledge updates.

---

## 🎯 Features
- ** Knowledge Graph Integration**: Uses MeTTa for structured data querying.
- ** Natural Language Understanding**: Matches FAQs dynamically.
- ** FastAPI Backend**: Provides an API for querying responses.
- ** Real-Time Updates**: Can be extended with new knowledge easily.
- ** Minimal & Lightweight**: Runs efficiently with a small footprint.

---

## 📂 Project Structure
```
FAQ-chatbot/
│── backend/
│   ├── knowledge_graph.py  # MeTTa knowledge processing
│   ├── main.py             # FastAPI server
│── README.md               # Project documentation
│── requirements.txt        # Dependencies
```

---

## 🛠️ Installation & Setup
### 1️⃣ **Clone the Repository**
```sh
git clone https://github.com/johnnas12/FAQ-chatbot.git
cd FAQ-chatbot/backend
```

### 2️⃣ **Create a Virtual Environment** (Recommended)
```sh
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3️⃣ **Install Dependencies**
```sh
pip install -r requirements.txt
```

### 4️⃣ **Run the API Server**
```sh
uvicorn main:app --reload
```

The API will now be running at **http://127.0.0.1:8000** 🎉

---

## 🔥 Usage
### **Querying the FAQ Chatbot**
#### **Make a GET request to the API:**
```sh
curl "http://127.0.0.1:8000/chat?question=What%20is%20AI"
```
#### **Expected JSON Response:**
```json
{
  "response": "AI stands for Artificial Intelligence, which simulates human intelligence in machines."
}
```

---

## 📝 Extending the Knowledge Base
You can **add new FAQ entries** in `knowledge_graph.py` like this:
```python
knowledge_base = """
(FAQ "What is AI?" "AI stands for Artificial Intelligence, which simulates human intelligence in machines.")
(FAQ "What is NLP?" "Natural Language Processing (NLP) is a branch of AI focused on human language understanding.")
"""
```
Then **restart the API** to apply changes.

---

## 🛠️ Tech Stack
- **[MeTTa](https://github.com/trueagi-io/hyperon-experimental.git)** → Graph-based AI reasoning
- **[FastAPI](https://fastapi.tiangolo.com/)** → High-performance backend
- **[Uvicorn](https://www.uvicorn.org/)** → ASGI web server for FastAPI

---

## 🤖 Future Improvements
- 🏗️ **Interactive Web UI** for easy FAQ querying
- 📚 **Dynamic Knowledge Updating** without restarting the API
- 🌍 **Multi-language Support** for wider accessibility

---

