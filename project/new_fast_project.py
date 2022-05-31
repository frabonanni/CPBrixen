import streamlit as st
import json,requests
from pprint import pprint
from gtts import gTTS
from googletrans import Translator
import IPython.display as ipd

st.title("MyWiki")
st.header('Translate Italian words to any language you want')

new_text = st.text_input('give me a text:','permesso di soggiorno')
new_text = st.text_input('give me a text:','ciao')
src_lan = st.text_input('give me a 2-letter code:', 'it')
st.file_uploader(label= "upload new_text", type=None, accept_multiple_files=False)


word1=gTTS(text='permesso di soggiorno')
word1.save('italian_permesso_soggiorno')
