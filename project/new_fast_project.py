import streamlit as st
import json,requests
from pprint import pprint
from gtts import gTTS
from googletrans import Translator
import IPython.display as ipd

st.title("MyWiki")
st.header('Translate Italian words to any language you want')

option = st.selectbox('Please select one of the words below',
('permesso di soggiorno', 'domicilio','residenza', 'questura', 'reddito di cittadinanza', 'assessore', 'dirigente scolastico'))
st.write('You selected:', option)

word1= gTTS(text='permesso di soggiorno')
word1.save('english_residence permit.mp3')
ipd.display(ipd.Audio('english_residence permit.mp3', autoplay=True))
