import streamlit as st

st.title('Text conversion into german to english')

text_input = st.text_input(
        "Enter some text 👇",
        placeholder=st.session_state.placeholder)

if text_input:
    st.write("You entered: ", text_input)
