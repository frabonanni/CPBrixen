import streamlit as st
import speech_recognition as sr

r = sr.Recognizer()
uploaded_file = st.file_uploader("Choose a file")
if AUDIO_FILE is not None:
  
with sr.AudioFile(AUDIO_FILE) as source:
    audio = r.record(source)  
recognised_text= r.recognize_google(audio)
st.text('the text recognized from the audio seems to be: ')
st.text( recognised_text)


