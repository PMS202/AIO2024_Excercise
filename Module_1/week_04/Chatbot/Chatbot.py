import streamlit as st
from hugchat import hugchat
from hugchat.login import Login


def login_page():
    with st.form("chat"):
        st.write("Login to Hugchat")
        username = st.text_input("Email")
        password = st.text_input("Password", type="password")
        submitted = st.form_submit_button("Login")
    if submitted == True:
        if (username == "" and password == ""):
            st . warning("Please enter your account !")
        else:
            try:
                login_hugchat(username, password)
                st.session_state.logged_in = True
                st.session_state.username = username  # Lưu username vào session state
                st.session_state.password = password
                st.rerun()
            except Exception as e:
                st.error("Incorrect username or password")


def show_chat_page(username, password):
    st.markdown("## Chat Page")
    st.write("Welcome to the chat page!")
    # Store LLM generated responses
    if " messages " not in st . session_state . keys():
        st . session_state . messages = [
            {"role": "assistant", "content": "How may I help you?"}]
    # Display chat messages

    for message in st . session_state . messages:
        with st . chat_message(message["role"]):
            st . write(message["content"])
    if prompt := st.chat_input(disabled=not (st.session_state.logged_in)):
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.write(prompt)
    if st.session_state.messages[-1]["role"] != "assistant":
        with st.chat_message("assistant"):
            with st.spinner("Thinking..."):
                response = generate_response(prompt, username, password)
                st.write(response)
        message = {"role": "assistant", "content": response}
        st.session_state.messages.append(message)

    # Nút Logout để quay lại trang đăng nhập
    if st.button("Logout"):
        st.session_state.logged_in = False
        st.rerun()


def login_hugchat(username, password):

    try:
        sign = Login(username, password)
        cookies = sign.login()
        return cookies
    except Exception as e:
        raise Exception(f"Login failed: {e}")


def generate_response(prompt_input, username, password):
    # Hugging Face Login
    # Create ChatBot
    try:
        cookies = login_hugchat(username, password)
        chatbot = hugchat.ChatBot(cookies=cookies.get_dict())
        return chatbot.chat(prompt_input)
    except Exception as e:
        raise Exception(f"Failed to generate response: {e}")


st.markdown("# My chatbot")
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False
if st.session_state.logged_in == False:
    login_page()
else:
    st.write(st.session_state.username)
    show_chat_page(st.session_state.username, st.session_state.password)
