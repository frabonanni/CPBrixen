import streamlit as st
import json,requests
from pprint import pprint
from gtts import gTTS
from googletrans import Translator
import IPython.display as ipd

st.title("MyWiki")
st.header('Translate Italian words to any language you want')
word = st.text_input('Gimme a word to translate ')
destlang= st.text_input('Tell me a two letter code for the destination language like es or en: ')
st.write('the translation is',abc.text)
st.file_uploader(label= "upload new_text", type=None, accept_multiple_files=False)


word1=gTTS(text='permesso di soggiorno')
word1.save('italian_permesso_soggiorno')
