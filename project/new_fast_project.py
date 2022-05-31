import streamlit as st
import json,requests
from pprint import pprint
from gtts import gTTS
from googletrans import Translator
import IPython.display as ipd

st.title("MyWiki")
st.header('Translate Italian words to any language you want')

new_text = st.text_input('give me a text:')
word1=gTTS(text='permesso di soggiorno')
word1.save('italian_permesso_soggiorno')
