import streamlit as st
from groq import Groq
import json
st.set_page_config(page_title="MySpaceFactor", layout="wide")
# Get the API key from Streamlit secrets
groq_api_key = st.secrets["GROQ_API_KEY"]

# Set up API key and initialize Groq client
groq_client = Groq(api_key=groq_api_key)

# Main system message for MySpaceFactor
main_system_message = """
You are an assistant for MySpaceFactor, a real estate firm dedicated to helping clients find their perfect homes. Provide insightful, professional, and helpful responses.
Company: MySpaceFactor
"""

# Individual assistant prompts
assistants = {
    "Raghav": {
        "description": "FAST",
        "prompt": "You are Raghav, an eccentric assistant with unique perspectives. Be witty, creative, and slightly unconventional."
    },
    "Pranav": {
        "description": "CALM",
        "prompt": "You are Pranav, a calm and sweet assistant. Be kind, patient, and supportive."
    },
    "Monesh": {
        "description": "COCKY",
        "prompt": "You are Monesh, a cocky assistant. Be confident, assertive, and slightly arrogant."
    }
}

# Initialize chat history and selected assistant in session state
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []
if "selected_assistant" not in st.session_state:
    st.session_state.selected_assistant = "Raghav"

# Sidebar for assistant selection
st.sidebar.title("Select Your Assistant")
assistant_choice = st.sidebar.selectbox("Choose an assistant:", list(assistants.keys()))

# Update selected assistant in session state
if st.session_state.selected_assistant != assistant_choice:
    st.session_state.selected_assistant = assistant_choice
    st.session_state.chat_history = []  # Clear chat history on assistant change

# Combine main system message with selected assistant's prompt
system_message = f"{main_system_message}\n{assistants[st.session_state.selected_assistant]['prompt']}"

# Add the system message to chat history if it's empty
if not st.session_state.chat_history:
    st.session_state.chat_history.append({"role": "system", "content": system_message})

# Streamlit app UI


st.title("MySpaceFactor")
st.write("Helping you find your perfect home. Talk to our virtual assistant for any inquiries.")

# Display selected assistant's description
st.sidebar.subheader("Assistant Description")
st.sidebar.write(assistants[st.session_state.selected_assistant]['description'])

# Display chat history
for message in st.session_state.chat_history:
    if message["role"] == "user":
        st.markdown(
            f"<div style='border: 2px solid blue; padding: 10px; margin: 10px 0; border-radius: 8px; width: 80%; float: right; clear: both;'>{message['content']}</div>",
            unsafe_allow_html=True
        )
    elif message["role"] == "assistant":
        st.markdown(
            f"<div style='border: 2px solid orange; padding: 10px; margin: 10px 0; border-radius: 8px; width: 80%; float: left; clear: both;'>{message['content']}</div>",
            unsafe_allow_html=True
        )

# Function to handle sending a message
def send_message():
    if st.session_state.input_buffer:
        message = st.session_state.input_buffer  # Store the input in a variable

        # Append user input to chat history
        st.session_state.chat_history.append({"role": "user", "content": message})

        # Call Groq API with the entire chat history
        response = groq_client.chat.completions.create(
            model="llama3-70b-8192",
            messages=st.session_state.chat_history,
            temperature=0.3,
            max_tokens=2000
        )
        chatbot_response = response.choices[0].message.content.strip()

        # Append chatbot response to chat history
        st.session_state.chat_history.append({"role": "assistant", "content": chatbot_response})

        # Clear the input buffer and trigger rerun
        st.session_state.input_buffer = ""
        st.session_state.run_count += 1  # Trigger a rerun by updating session state

if "run_count" not in st.session_state:
    st.session_state.run_count = 0  # Initialize run count

user_input = st.text_input("Type your message here:", key="input_buffer")
st.button("Send", on_click=send_message)

# Dummy element to force rerun without showing error
st.write(f"Run count: {st.session_state.run_count}")
