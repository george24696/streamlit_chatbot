import streamlit as st
from openai import OpenAI
import base64

def get_base64_image(path):
    with open(path, "rb") as f:
        data = f.read()
    return base64.b64encode(data).decode()


st.set_page_config(page_title="SU ChatBot", page_icon="🎓")
image_base64 = get_base64_image("stellenbosch_new_logo.png")

st.markdown(
    f"""
    <div style="background-color: #5C0033; padding: 12px 24px;">
        <img src="data:image/png;base64,{image_base64}" width="100" style="vertical-align: middle;">
    </div>
    """,
    unsafe_allow_html=True
)

# Stellenbosch style customization
st.markdown(
    """
    <style>
    /* Background and font */
    body, .stApp {
        background-color: #ffffff;
        font-family: 'Georgia', serif;
    }

    /* Title styling */
    .st-emotion-cache-18ni7ap h1 {
        font-family: 'Times New Roman', serif;
        color: #5C0033;
        text-align: center;
        font-size: 48px;
    }

    /* Chat input container (align input + button) */
    .stChatInput > div {
        display: flex;
        align-items: center;
        gap: 0px;
    }

    /* Text input field */
    .stChatInput input {
        border: 2px solid #5C0033;
        border-right: none;
        border-radius: 24px 0 0 24px;
        padding: 12px 16px;
        height: 48px;
    }

    /* Send button */
    button[kind="icon"] {
        border: 2px solid #5C0033;
        border-left: none;
        border-radius: 0 24px 24px 0;
        height: 48px;
        width: 48px;
        margin: 0;
        padding: 0;
        background-color: white;
        display: flex;
        align-items: center;
        justify-content: center;
    }

    /* User message styling */
    .st-emotion-cache-1v0mbdj {
        background-color: #F9F2F4 !important;
        border-left: 4px solid #5C0033;
    }

    /* Assistant message styling */
    .st-emotion-cache-1v0mbdj:nth-child(even) {
        background-color: #EFEFEF !important;
        border-left: 4px solid #C4C4C4;
    }

    /* Chat message text */
    .stMarkdown {
        font-size: 18px;
        color: #333333;
    }

    /* Hide deploy button/header */
    header[data-testid="stHeader"] {
        display: none;
    }
    </style>
    """,
    unsafe_allow_html=True
)


st.markdown("<h1 style='color: #1A1110; text-align: left;'>ChatBot 🎓</h1>", unsafe_allow_html=True)


# Set OpenAI API key from Streamlit secrets
client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

# Set a default model
if "openai_model" not in st.session_state:
    st.session_state["openai_model"] = "gpt-3.5-turbo"

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat messages from history on app rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# SU-themed footer
st.markdown(
    '<div style="text-align: center; margin-bottom: 20px; color: #7A003C; position: relative;">'
    '<small>Powered by OpenAI • Stellenbosch University ChatBot Prototype</small></div>',
    unsafe_allow_html=True
)

# Accept user input
if prompt := st.chat_input("What is up?"):
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})
    # Display user message in chat message container
    with st.chat_message("user"):
        st.markdown(prompt)

    # Display assistant response in chat message container
    with st.chat_message("assistant"):
        stream = client.chat.completions.create(
            model=st.session_state["openai_model"],
            messages=[
                {"role": m["role"], "content": m["content"]}
                for m in st.session_state.messages
            ],
            stream=True,
        )
        response = st.write_stream(stream)
    st.session_state.messages.append({"role": "assistant", "content": response})

# === END OF CHAT FUNCTIONALITY ===
