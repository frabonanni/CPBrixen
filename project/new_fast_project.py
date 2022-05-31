import streamlit as st
import json,requests
from pprint import pprint
from gtts import gTTS

st.title("MyWiki")
st.header('Translate Italian words to any language you want')

option = st.selectbox
('Please select one of the words below',
('permesso di soggiorno', 'domicilio' 'residenza', 'questura', 'reddito di cittadinanza', 'assessore', 'dirigente scolastico'))
st.write('You selected:', option)

word1= gTTS(text='permesso di soggiorno')
tts1.save('english_permesso_di_soggiorno.mp3')
