import streamlit as st
from PIL import Image
import os
import speech_recognition as sr
st.title('LawWiki translator for foreigners')
st.write(""" -Hello user! This is the ILT app. It is very simple to use and it will help you understand some useful words in a particular situation or context""")
st.write(""" -Please listen to the first recording, read the text below it and then listen to the second audio file""")
image1 = Image.open("language-translator-translater.jpg")
st.image(image1)
#pip install pydub
from pydub import AudioSegment
from pydub.silence import split_on_silence
AUDIO_FILE = "/content/drive/MyDrive/Rec_project_python.wav"
r = sr.Recognizer()
with sr.AudioFile(AUDIO_FILE) as source:
    audio = r.record(source)  # read the entire audio file
    print("Recognized Speech: \n" + r.recognize_google(audio))

apikey='FoQQPWQYE0B-3i38r1IbI_20uzPYHiF8JMHND1DuQ6yG' ## qui ci va il tuo Apikey che crei nel profilo
url='https://api.eu-gb.speech-to-text.watson.cloud.ibm.com/instances/36876297-be6a-479d-9f8a-f34ef6a63c31' # il tuo url

authenticator = IAMAuthenticator(apikey)
stt = SpeechToTextV1(authenticator=authenticator)

stt.set_service_url(url)
stt.set_disable_ssl_verification(True)
with open("/content/drive/MyDrive/registrazione python 1 (online-audio-converter.com).wav", 'rb') as f:  
  res = stt.recognize(audio=f, content_type='audio/wav', model ='es-ES_NarrowbandModel').get_result()

res

for el in res["results"]:
  for l in el["alternatives"]:
    st.write(l["transcript"])

new_list = []
for el in l["transcript"]:
    new_list.append(l["transcript"])
    st.write(new_list)
