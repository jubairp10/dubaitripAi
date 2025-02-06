import streamlit as st
st.title('Chat Window')

with st.chat_message("assistant"):
    st.markdown("Hello I am your Assistant")
    
with st.chat_message("human"):
    st.markdown("I am palanning vaccation to dubai")    

message=st.chat_input("Enter Your Chat")

if message:
    with st.chat_message('human'):
        st.markdown(message)