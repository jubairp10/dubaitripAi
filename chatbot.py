from dotenv import load_dotenv
from openai import OpenAI
import streamlit as st

load_dotenv()

client = OpenAI()


initial_message=[
    {"role": "system", "content": "You are a Trip Planner in Dubai. You are an expert in Dubai tourism, locations, food, events, hotels, etc. You guide users to plan their vacations to Dubai. You should respond professionally. Your name is Dubai Genie, short name DG. Responses shouldn't exceed 200 words.Always Ask questions to user and help them to plan the trip.Finally  Give a day wise itinenary. deal with user professionaly  "},
    {"role": "assistant", "content": "Hello, I am DubaiGenie, your expert planner. How can I help you?"}
]
#functions to get respoonce from open Ai LLm
def get_responce_from_llm(messages):
    completion = client.chat.completions.create(
        model="gpt-4o",
        messages=messages, 
)
    return completion.choices[0].message.content


#to initiaalise with initial message
if "messages" not in st.session_state:
    st.session_state.messages= initial_message

# st.title("Dubai Trip Assistant AI!")
# import base64

# def image_to_base64(image_path):
#     with open(image_path, "rb") as img_file:
#         return base64.b64encode(img_file.read()).decode()

# image_base64 = image_to_base64("c:\Users\lenovo\Downloads\advanced-ai-assistant-icon-in-illustration-vector-removebg-preview.png")


st.markdown(
    """
    <h1 style='text-align:leftbottom;  color:rgb(55, 82, 6); font-size: 3em;'>
        <link href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0-beta3/css/all.min.css" rel="stylesheet">
        <img src="https://static.vecteezy.com/system/resources/previews/024/246/469/non_2x/advanced-ai-assistant-icon-in-illustration-vector.jpg" alt="Dubai Logo" style="width:60px; vertical-align:middle; margin-right:10px;">
       

        Dubai Genie: Your AI Travel Planner for Dubai!
    </h1>
    """,
    unsafe_allow_html=True
)

#dispplay prev s chat content in Ui
for message in st.session_state.messages:
    if message["role"] !="system":
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

user_message=st.chat_input("Enter Your Chat")
if user_message:
    new_message= {
            "role": "user",
            "content": user_message
        }
    st.session_state.messages.append(new_message)
    with st.chat_message(new_message[ "role"]):
      st.markdown(new_message["content"]) 

    responce=get_responce_from_llm(st.session_state.messages)
    if responce:
        responce_message={
            "role":"assistant",
            "content":responce
        }
        st.session_state.messages.append(responce_message)
        with st.chat_message(responce_message["role"]):
             st.markdown(responce_message["content"]) 


