import streamlit as st
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
    body, .stApp {
        background-color: #ffffff;
        font-family: 'Georgia', serif;
    }
    .st-emotion-cache-18ni7ap h1 {
        font-family: 'Times New Roman', serif;
        color: #5C0033;
        text-align: center;
        font-size: 48px;
    }
    .stChatInput > div {
        display: flex;
        align-items: center;
        gap: 0px;
    }
    .stChatInput input {
        border: 2px solid #5C0033;
        border-right: none;
        border-radius: 24px 0 0 24px;
        padding: 12px 16px;
        height: 48px;
    }
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
    .st-emotion-cache-1v0mbdj {
        background-color: #F9F2F4 !important;
        border-left: 4px solid #5C0033;
    }
    .st-emotion-cache-1v0mbdj:nth-child(even) {
        background-color: #EFEFEF !important;
        border-left: 4px solid #C4C4C4;
    }
    .stMarkdown {
        font-size: 18px;
        color: #333333;
    }
    header[data-testid="stHeader"] {
        display: none;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.title("ChatBot 🎓")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat history
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# === Chatbot logic ===
def rule_based_response(prompt):
    prompt_lower = prompt.lower()

    if "hi" in prompt_lower or "hello" in prompt_lower or "hey" in prompt_lower:
        return "Hello prospective Stellenbosch student! How can I help you?"
    
    if "faculty" in prompt_lower or "faculties" in prompt_lower:
        return "Stellenbosch has faculties like Engineering, Humanities, Science, AgriSciences, and more. Which one one would you like more info on?"

    elif "engineering" in prompt_lower:
        return "Engineering is a challenging and rewarding faculty. Be sure to visit the Engineering library and Makerspace!"

    elif "humanities" in prompt_lower:
        return "Humanities offers diverse programmes like Psychology, Philosophy, and Sociology. Great choice!"

    elif "science" in prompt_lower:
        return "The Faculty of Science includes majors like Physics, Biology, and Mathematical Sciences."

    elif "1" in prompt_lower and "year" in prompt_lower:
        return "Welcome to your first year! Don’t forget to explore all the support services SU offers."

    elif "2" in prompt_lower and "year" in prompt_lower:
        return "Second year can be intense—make sure to balance academics with wellbeing."

    elif "3" in prompt_lower and "year" in prompt_lower:
        return "You’re almost there! This is a good time to plan internships or postgrad options."

    elif "year" in prompt_lower:
        return "Which year are you in? (1st, 2nd, 3rd, or final year?)"

    elif "final" in prompt_lower or "4" in prompt_lower:
        return "Final year—congrats! Consider attending career fairs and checking out Honours programmes."

    elif "module" in prompt_lower or "subject" in prompt_lower:
        return "Which module are you referring to? Example: ECO101, CSC201, PSY301"

    elif "eco101" in prompt_lower:
        return "ECO101 is Introduction to Economics. Lectures usually take place in the Van der Sterr building."

    elif "csc201" in prompt_lower:
        return "CSC201 is Data Structures & Algorithms. Make sure you're confident with recursion and trees."

    elif "psy301" in prompt_lower:
        return "PSY301 explores advanced psychological theories. Check SUNLearn for weekly readings."

    elif "thank" in prompt_lower:
        return "You’re welcome! Let me know if you have more questions."

    else:
        return "I’m still learning. Could you rephrase or be more specific about faculty, year, degree or module?"

# Chat input + response
if prompt := st.chat_input("Ask me anything about your studies..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    response = rule_based_response(prompt)
    with st.chat_message("assistant"):
        st.markdown(response)
    st.session_state.messages.append({"role": "assistant", "content": response})

# Footer
st.markdown(
    '<div style="text-align: center; margin-top: 50px; color: #7A003C;">'
    '<small>Stellenbosch University ChatBot Prototype – Rule-Based • No API Used</small></div>',
    unsafe_allow_html=True
)
