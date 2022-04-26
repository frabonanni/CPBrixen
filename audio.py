import streamlit as st
from gtts import gTTS

from googletrans import Translator


new_text = st.text_input('ciao')
dest_lan = st.text_input('it')

if new_text != ' ':
    translator = Translator()
    transToLan = translator.translate(new_text, dest= dest_lan)
    ppp = transToLan.text
else:
    pass



new_name=gTTS(text= ppp, lang= dest_lan)
new_name.save('file_name.mp3)
audio_file = open('file_name.mp3', "rb")
st.audio(data=audio_file, format="audio/mp3", start_time=0)

