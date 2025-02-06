# import streamlit as st
# st.title('Hi Welcome DubaiTripAi')

# name=st.text_input('Enter your name:')

# if st.button('say Hello'):
#     st.write(f'Hello {name},Welcome to DubaiTripAi')

import streamlit as st

# Title of the application
st.title('Hi Welcome to DubaiTripAi')

# Input for name
name = st.text_input('Enter your name:')

# Button action
if st.button('Say Hello'):
    # If the name is provided
    if name:
        st.write(f'Hello {name}, Welcome to DubaiTripAi!')
    else:
        st.write("It seems you haven't entered your name. Please try again!")