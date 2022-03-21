import streamlit as st
st.header("hello world")
title = st.text_input('Gimme a movie title', 'Meet Joe Black')
st.write('The current movie title is', title)
