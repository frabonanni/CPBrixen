import streamlit as st
st.header("hello world")
title = st.text_input('Gimme a movie title', 'Meet Joe Black', max_chars=7)
st.write('The current movie title is', title)
