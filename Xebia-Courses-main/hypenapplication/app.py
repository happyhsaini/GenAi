import streamlit as st
from predict import predict_intent

st.set_page_config(page_title="ML Chatbot")

st.title("ML Powered Chatbot")
st.write("ChatBot with intent...")

# Initialize chat history
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# Use form (IMPORTANT)
with st.form("chat_form", clear_on_submit=True):
    user_input = st.text_input("Enter something:")
    submitted = st.form_submit_button("Send")

    if submitted and user_input.strip() != "":
        # Add user message
        st.session_state.chat_history.append(("You", user_input))

        # Predict intent
        prediction = predict_intent(user_input)

        if prediction == "greet":
            response = "Hello, how can I help you?"
        elif prediction == "weather":
            response = "The weather is ....."
        else:
            response = "I don't know how to respond to that."

        # Add bot response
        st.session_state.chat_history.append(("Bot", response))

# Display chat history
for sender, message in st.session_state.chat_history:
    st.markdown(f"**{sender}:** {message}")
