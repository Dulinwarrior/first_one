import streamlit as st

options = ['The history of cars🕰️', 'Difference between DIESEL and PETROL engines⛽', 'Modern capabilitties of cars🚗', 'Concept Cars🏎️']
st.sidebar.selectbox('Options', options)
st.title('All you need to know about cars')
st.write('This is my first web hosted application')
