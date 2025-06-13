# ---------------- IMPORTS ----------------
import streamlit as st
from llama_cpp import Llama
import json
import time
from streamlit_lottie import st_lottie

# ---------------- PAGE CONFIG ----------------
st.set_page_config(page_title="🤖 Godse Local Chatbot", layout="centered")

# ---------------- TYPING EFFECT FUNCTION ----------------
def typing_effect(text, speed=0.03):
    placeholder = st.empty()
    typed_text = ""
    for char in text:
        typed_text += char
        placeholder.markdown(f"**{typed_text}**")
        time.sleep(speed)

# ---------------- LOTTIE LOADER FUNCTION ----------------
def load_lottie(filepath: str):
    try:
        with open(filepath, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        st.warning("⚠️ Animation file not found.")
        return None

# ---------------- LOAD LLaMA MODEL FUNCTION ----------------
@st.cache_resource
def load_llama_model():
    return Llama(model_path="model.gguf")  # Change to your correct model path

# ---------------- LOAD MODEL ----------------
with st.spinner("Loading AI Model..."):
    model = load_llama_model()

# ---------------- LOAD ANIMATION ----------------
lottie_animation = load_lottie("bot_lottie.json")

# ---------------- UI HEADER ----------------
st.title("🤖 Godse Local Chatbot")
if lottie_animation:
    st_lottie(lottie_animation, height=250)

st.markdown("Ask anything! The AI runs 100% locally on your machine. 🧠💻")

# ---------------- CHAT INTERFACE ----------------
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

user_input = st.text_input("You:", placeholder="Type your message here...", key="input")

if st.button("Send") and user_input.strip():
    st.session_state.chat_history.append(("User", user_input))

    # Prepare full prompt
    history_prompt = "\n".join(
        [f"{speaker}: {msg}" for speaker, msg in st.session_state.chat_history]
    )
    full_prompt = f"{history_prompt}\nAssistant:"

    # Generate response
    with st.spinner("Thinking... 🤔"):
        output = model(full_prompt, max_tokens=150, stop=["User:", "Assistant:"])
        reply = output["choices"][0]["text"].strip()
        st.session_state.chat_history.append(("Assistant", reply))

    # Typing animation
    typing_effect(reply)

# ---------------- SHOW CHAT HISTORY ----------------
st.markdown("## 🧾 Conversation")
for speaker, msg in st.session_state.chat_history:
    st.markdown(f"**{speaker}:** {msg}")