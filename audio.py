import streamlit as st
from gtts import gTTS
import IPython.display as ipd
from googletrans import Translator

new_text = st.input('give me a text: ')
dest_lan = st.input('give me a language: ')
translator = Translator()
transToLan = translator.translate(new_text, dest= dest_lan)

ppp = transToLan.text
print(ppp)
file_name = st.input('give me a name with .mp3: ')
new_name=gTTS(text= ppp, lang= dest_lan)
new_name.save(file_name)

st.audio(ipd.Audio(file_name))
