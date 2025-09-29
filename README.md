# Todoist AI Assistant  

This project is an **AI-powered task manager** that integrates **Google Gemini** with **Todoist**.  
It can be used both as a **command-line assistant** and as a **Streamlit web app**.  

With natural language commands, you can:  
- **Add tasks** to your Todoist  
- **View existing tasks** in a clear bullet list  
- **Ask general questions** (Gemini handles them like a chatbot)  
- Maintain a conversation **history** for context-aware responses  

---

## Live Demo  
Try the Streamlit app here 👉 [Todoist AI Assistant](https://nassoumatine-app4-task-manager-agent-web-b5fklj.streamlit.app/)  

---

## 📂 Project Structure  
.

├── main.py    # Command-line interface version

├── web.py     # Streamlit web app version

├── requirements.txt

└── README.md


## Setup & Installation

### 1. Clone the repository  
```bash
git clone https://github.com/your-username/todoist-ai-assistant.git
cd todoist-ai-assistant
```
### 2. Create and activate a virtual environment
```bash
python -m venv .venv
source .venv/bin/activate   # On macOS/Linux
.venv\Scripts\activate      # On Windows
```
### 3. Install dependencies
```bash
pip install -r requirements.txt
```
### 4. Set up environment variables
Create a .env file in the root folder and add your keys:
```ini
TODOIST_API_KEY=your_todoist_api_key_here
GEMINI_API_KEY=your_gemini_api_key_here
```

---

## Run Instructions

### Command-line Interface (CLI)

Run the assistant in your terminal:
```bash
python main.py
```
Example usage:
```ini
You: add buy bananas with description from the local store
Assistant: I've added "buy bananas" with the description "from the local store" to your Todoist app.
You: show me my tasks
Assistant:
- Buy bananas
- Finish project report
You: exit
```

### Streamlit Web App
Run the web-based chat interface:
```bash
streamlit run web.py
```
Then open the URL shown in your terminal (usually http://localhost:8501).

Features of the web app:
- Chat interface with scrolling conversation history
- Clear command → ends the conversation and resets history

### Tech Stack
- [Streamlit](https://streamlit.io/) for the web UI
- [LangChain](https://www.langchain.com/) for agent + prompt handling
- [Todoist API](https://developer.todoist.com/rest/v2/) for task management
- [Google Gemini API](https://deepmind.google/technologies/gemini/) for natural language intelligence
