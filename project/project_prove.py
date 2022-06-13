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


col1, col2= st.columns(2)
with col1:
     st.title("MyTransIT")
     st.image("https://raw.githubusercontent.com/frabonanni/CPBrixen/main/project/language-translator-translater.jpg")
with col2:
     st.subheader('Translate Italian words to any language you want')
     st.write('Hello! This app translates any Italian word you put into any language. Then it converts the written word into an audio file which you can listen and download. You can read an Italian definition of the word from Wikipedia and this definition is converted into an audio file that you can listen')
st.markdown("""---""")
option= st.selectbox('How would you like to import the text? Please select either browser or input', (' ','browser', 'input'))
if option == 'browser':
   imported_file=st.file_uploader("Choose a text file")
   if imported_file is not None:
       stringio = io.StringIO(imported_file.getvalue().decode("utf-8"))
       string_data = stringio.read()
       st.write(string_data)
       st.write(stringio)
       srclang= 'it'
       destlang= st.text_input('Tell me a two letter code for the destination language like fr or de: ', value= '')
       option = st.selectbox(
       'Here you can see some language codes to choose for your language',
       ('en','fr','es', 'sq', 'ro', 'af', 'bs', 'mk', 'mt'))
       if destlang is not None and imported_file is not None:
          aaa=gTTS(text=imported_file, lang =srclang)
          st.write('Press the play button below and listen to the audio file')
          aaa.save('file_name.mp3')
          audio_file= open('file_name.mp3', "rb")
          st.audio(data=audio_file, format="audio/mp3", start_time=0)
          st.download_button(label= "If you wish download the audio file", data= audio_file, file_name="new_text_audio", mime="audio/mp3")
          st.markdown("""---""")
          translator= Translator()
          TranstoLan= translator.translate(imported_file, src=srclang, dest= destlang)
          st.write('the translation is',TranstoLan.text)
          url = 'https://it.wikipedia.org/w/api.php?action=query&format=json&list=search&srsearch='+imported_file
          response = requests.get(url)
          dataFromWikipedia = json.loads(response.text)
          textfromWikipedia = dataFromWikipedia['query']['search'][0]['snippet']
          cleanTextfromWikipedia = strip_html(textfromWikipedia)
          st.write(cleanTextfromWikipedia)
          translator= Translator()
          TranstoLan= translator.translate(cleanTextfromWikipedia, src='it', dest= destlang)
          desttranslate = TranstoLan.text
          st.write('the translation is',desttranslate)
          st.markdown("""---""")

          yourtext=gTTS(text= desttranslate, lang=destlang)
          yourtext.save('your_translation.mp3')
          audio_file1= open('your_translation.mp3', "rb")
          st.audio(data=audio_file1, format="audio/mp3", start_time=0)

          st.write('the translation is',TranstoLan.text)
else:
    myword=st.text_input('Give me an Italian word to translate ',value='')
    srclang= 'it'
    destlang= st.text_input('Tell me a two letter code for the destination language like fr or de: ', value= '')
    option = st.selectbox(
    'Here you can see some language codes to choose for your language',
    ('en','fr','es', 'sq', 'ro', 'af', 'bs', 'mk', 'mt'))
    if destlang is not None and myword is not '':
       firstword=gTTS(text=myword, lang =srclang)
       st.write('Press the play button below and listen to the audio file')
       firstword.save('file_name.mp3')
       audio_file= open('file_name.mp3', "rb")
       st.audio(data=audio_file, format="audio/mp3", start_time=0)
       st.download_button(label= "If you wish download the audio file", data= audio_file, file_name="new_text_audio", mime="audio/mp3")
       st.markdown("""---""")
       translator= Translator()
       TranstoLan= translator.translate(myword, src=srclang, dest= destlang)
       st.write('the translation is',TranstoLan.text)
       url = 'https://it.wikipedia.org/w/api.php?action=query&format=json&list=search&srsearch='+myword
       response = requests.get(url)
       dataFromWikipedia = json.loads(response.text)
       textfromWikipedia = dataFromWikipedia['query']['search'][0]['snippet']
       cleanTextfromWikipedia = strip_html(textfromWikipedia)
       st.write(cleanTextfromWikipedia)
       translator= Translator()
       TranstoLan= translator.translate(cleanTextfromWikipedia, src='it', dest= destlang)
       desttranslate = TranstoLan.text
       st.write('the translation is',desttranslate)
       st.markdown("""---""")

       yourtext=gTTS(text= desttranslate, lang=destlang)
       yourtext.save('your_translation.mp3')
       audio_file1= open('your_translation.mp3', "rb")
       st.audio(data=audio_file1, format="audio/mp3", start_time=0)

       st.write('the translation is',TranstoLan.text)

       st.markdown("""---""")

st.write("Credits:")
st.write("""
- For Translator image: https://raw.githubusercontent.com/frabonanni/CPBrixen/main/project/language-translator-translater.jpg
""")
st.write("""- For the Streamlit documentation: https://docs.streamlit.io/library/api-reference/media/st.audio 
""")
st.write("""- For the Wikipedia definitions: https://it.wikipedia.org/wiki/Pagina_principale
""")
