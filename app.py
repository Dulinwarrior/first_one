import streamlit as st

options = ['hello', 'world']
st.sidebar.selectbox('Options', options)
st.title('hello world')
st.write('This is my first web hosted application')