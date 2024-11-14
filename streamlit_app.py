import streamlit as st

st.set_page_config(layout='wide')

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []


with st.sidebar:
    if st.button("\+ New Chat"):
        # reset message
        st.session_state.messages = []

    st.divider()

    # Topic selection
    def on_toppic_session_click(button):
        st.session_state.last_toppic = button
    
    toppic_list = ["toppic 1", "toppic 2", "toppic 3"]
    for n in range(len(toppic_list)):
        st.button(f"Button {toppic_list[n]}", on_click=on_toppic_session_click, kwargs={"button": n})

    if "last_toppic" in st.session_state:
        st.write(f"Last topic: **{toppic_list[st.session_state.last_toppic]}**")



col1, col2 = st.columns(2)

with col1:
    # st.header("J Wiz")
    container1_1 = col1.container(height=716)

    # Display chat messages from history on app rerun
    for message in st.session_state.messages:
        container1_1.chat_message(message["role"]).markdown(message["content"])


with col2:

    container2_1 = col2.container(height=350)
    container2_2 = col2.container(height=350)
    container2_1.subheader('Suggested Conversations')
    container2_2.subheader('Suggested Products')


# React to user input
if prompt := st.chat_input("Say some thing"):
    # Display user message in chat message container
    container1_1.chat_message("user").markdown(prompt)
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})

    response = f"Echo: {prompt}"
    # Display assistant response in chat message container
    container1_1.chat_message("assistant").markdown(response)
    # Add assistant response to chat history
    st.session_state.messages.append({"role": "assistant", "content": response})