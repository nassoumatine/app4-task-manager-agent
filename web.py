import os
from dotenv import load_dotenv
from todoist_api_python.api import TodoistAPI
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.tools import tool
from langchain.agents import create_openai_tools_agent, AgentExecutor
from langchain_core.messages import HumanMessage, AIMessage
import streamlit as st 

load_dotenv()

todoist_api_key = os.getenv("TODOIST_API_KEY")
gemini_api_key = os.getenv("GEMINI_API_KEY")

todoist = TodoistAPI(todoist_api_key)

@tool
def add_task(task, desc=None):
    """
    Add a new task to the user's task list.
    Use this when the user wants to add or create a task
    """
    todoist.add_task(content=task,
                     description=desc)
@tool
def show_tasks():
    """
    Show all tasks from Todoist.
    Use this tool when the user wants to see their tasks.
    """
    results_paginator = todoist.get_tasks()
    tasks = []
    for task_list in results_paginator:
        for task in task_list:
            tasks.append(task.content)
    return tasks

tools = [add_task, show_tasks]

llm = ChatGoogleGenerativeAI(
    model='gemini-2.5-flash',
    google_api_key=gemini_api_key,
    temperature=0.3
)

system_prompt = """
    You are a helpful assistant. 
    You answer all user general questions, and will help the user add tasks.
    You will help the user show existing tasks. If the user asks to show the 
    tasks: for example, "show me teh tasks", print out the tasks to the user in
    a bullet list format.
"""

prompt = ChatPromptTemplate([
    ("system", system_prompt),
    MessagesPlaceholder("history"),
    ("user", "{input}"),
    MessagesPlaceholder("agent_scratchpad")
])

agent = create_openai_tools_agent(llm, tools, prompt)
agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=False)


# --- Streamlit App ---
st.set_page_config(page_title="Todoist AI Assistant", page_icon="✅")
st.title("🤖 Todoist AI Assistant")

if "history" not in st.session_state:
    st.session_state.history = []

if "messages" not in st.session_state:
    st.session_state.messages = []

for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

if user_input := st.chat_input("Type a message (or 'clear' to clear the chat and the memory)..."):
    if user_input.lower() == "clear":
        st.session_state.history = []
        st.session_state.messages = []

        st.rerun()

    st.session_state.messages.append({"role": "user", "content": user_input})
    st.chat_message("user").markdown(user_input)

    response = agent_executor.invoke({"input": user_input, "history": st.session_state.history})

    output_text = response["output"]
    st.session_state.messages.append({"role": "assistant", "content": output_text})
    with st.chat_message("assistant"):
        st.markdown(output_text)

    # Update history for context
    st.session_state.history.append(HumanMessage(content=user_input))
    st.session_state.history.append(AIMessage(content=output_text))



