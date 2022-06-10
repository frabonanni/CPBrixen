import streamlit as st
import json,requests
from pprint import pprint
from gtts import gTTS
from googletrans import Translator
import IPython.display as ipd
from PIL import Image
from lxml import html


def strip_html(stringwithHTML):
    mydefinition = str(html.fromstring(stringwithHTML).text_content())
    return str(html.fromstring(stringwithHTML).text_content())




st.title("TradFromIT")
st.subheader('Translate Italian words to any language you want')
st.image("https://raw.githubusercontent.com/frabonanni/CPBrixen/main/project/language-translator-translater.jpg")
st.markdown('---')
myword = st.text_input('Give me an Italian word to translate ',value='')
srclang= 'it'
destlang= st.text_input('Tell me a two letter code for the destination language like fr or de: ', value= 'en')
if destlang is not None and myword is not '':
   firstword=gTTS(text=myword, lang =srclang)
   firstword.save('file_name.mp3')
   audio_file= open('file_name.mp3', "rb")
   st.audio(data=audio_file, format="audio/mp3", start_time=0)
   st.download_button(label= "download the audio file", data= audio_file, file_name="new_text_audio", mime="audio/mp3")
   
   translator= Translator()
   TranstoLan= translator.translate(myword, src=srclang, dest= destlang)
   ppp= TranstoLan.text
   st.write('Press the play button so that you can hear the word pronounced in Italian')
   st.write('the translation is',TranstoLan.text)
   
   mykeyword = myword
   url = 'https://en.wikipedia.org/w/api.php?action=query&format=json&list=search&srsearch='+mykeyword
   response = requests.get(url)
   dataFromWikipedia = json.loads(response.text)
   textfromWikipedia = dataFromWikipedia['query']['search'][0]['snippet']
   cleanTextfromWikipedia = strip_html(textfromWikipedia)    
   st.write(cleanTextfromWikipedia)
   
   translator= Translator()
   TranstoLan= translator.translate(cleanTextfromWikipedia, src='en', dest= destlang)
   ppp= TranstoLan.text                        
   st.write('the translation is',TranstoLan.text)
      
                          

