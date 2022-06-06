import streamlit as st
import json,requests
from pprint import pprint
from gtts import gTTS
from googletrans import Translator
import IPython.display as ipd
from PIL import Image
from bs4 import BeautifulSoup

st.title("MyWiki")
st.header('Translate Italian words to any language you want')
st.image("https://raw.githubusercontent.com/frabonanni/CPBrixen/main/project/language-translator-translater.jpg")
myword = st.text_input('Give me a word to translate ')
srclang= 'it'
destlang= st.text_input('Tell me a two letter code for the destination language like es or en: ')
if myword != ' ':
   translator= Translator()
   TranstoLan= translator.translate(myword, src=srclang, dest= destlang)
   ppp= TranstoLan.text                        
   st.write('the translation is',TranstoLan.text)
   firstword=gTTS(text=myword, lang =srclang)
   firstword.save('file_name.mp3')
   audio_file= open('file_name.mp3', "rb")
   st.audio(data=audio_file, format="audio/mp3", start_time=0)
   st.download_button(label= "download the audio file", data= audio_file, file_name="new_text_audio", mime="audio/mp3")
else:
   pass                        


mykeyword = myword
url = 'https://en.wikipedia.org/w/api.php?action=query&format=json&list=search&srsearch='+mykeyword
response = requests.get(url)
dataFromWikipedia = json.loads(response.text)
st.write(dataFromWikipedia['query']['search'][0]['snippet'])
soup = BeautifulSoup(dataFromWikipedia['query']['search'][0]['snippet'])
ppdata = soup.get_text()
st.write(ppdata)
