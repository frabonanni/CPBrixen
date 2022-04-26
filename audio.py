import streamlit as st
from gtts import gTTS

from googletrans import Translator


new_text = st.input()

dest_lan = st.input()
translator = Translator()
transToLan = translator.translate(new_text, dest= dest_lan)

ppp = transToLan.text
print(ppp)

file_name = st.input()
new_name=gTTS(text= ppp, lang= dest_lan)
new_name.save(file_name)
audio_file = open(file_name, "rb")
st.audio(data=audio_file, format="audio/mp3", start_time=0)

