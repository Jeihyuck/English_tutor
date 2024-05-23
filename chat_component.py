import streamlit as st
import numpy as np

with st.chat_message("user"):
    st.write("hello")

with st.chat_message("assistant"):
    st.write("hello human")
    st.bar_chart(np.random.randn(30,3))

prompt = st.chat_input("say something")
if prompt:
    with st.chat_message("user"):
        st.write(prompt)

