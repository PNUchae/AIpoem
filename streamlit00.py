import streamlit as st

st.header("Welcome to GPT Bot", divider = 'rainbow')

st.write("Welcome to GPT chat-bot")

query = st.text_input('Query: ')
if query :
    st.write('Your Query is ' + query)


#st.button("Run", type="primary")
button_result = st.button('Run')
if button_result:
    st.write('hello')
else:
    st.write('Goodbye')