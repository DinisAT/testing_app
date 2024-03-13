from main.main import *
import streamlit as st

input = st.text_input("Enter your text")

coach = st.text_input("Enter your coach's name")

while coach == "":
    continue
if coach:
    st.write(createTalk(input, coach))
