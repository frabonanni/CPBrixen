import streamlit as st
import json,requests
from pprint import pprint
from gtts import gTTS
from googletrans import Translator
import IPython.display as ipd
from PIL import Image

st.title("MyWiki")
st.header('Translate Italian words to any language you want')
st.image("https://raw.githubusercontent.com/frabonanni/CPBrixen/main/project/language-translator-translater.jpg")
word = st.text_input('Give me a word to translate ')
srclang= 'it'
destlang= st.text_input('Tell me a two letter code for the destination language like es or en: ')
if word != ' ':
   translator= Translator()
   TranstoLan= translator.translate(word, src=srclang, dest= destlang)
   ppp= TranstoLan.text                        
   st.write('the translation is',TranstoLan.text)
   word1=gTTS(text=ppp, lang =destlang)
   word1.save('file_name.mp3')
   audio_file= open('file_name.mp3', "rb")
   st.audio(data=audio_file, format="audio/mp3", start_time=0)
   st.download_button(label= "download the audio file", data= audio_file, file_name="new_text_audio", mime="audio/mp3")
else:
   pass                        
