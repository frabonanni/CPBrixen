import streamlit as st
st.header("hello world")
title = st.text_input('Gimme a movie title', 'Meet Joe Black', max_chars=7)
st.write('The current movie title is', title)

genre = st.radio("What's your favorite movie genre",('Comedy', 'Drama', 'Documentary'), help= 'click one of the three options')
if genre == 'Comedy':
     st.write('You selected comedy.')
else:
     st.write("You didn't select comedy.")
