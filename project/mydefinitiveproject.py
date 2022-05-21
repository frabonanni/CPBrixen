import streamlit as st
import os

import speech_recognition as sr
!pip install pydub
from pydub import AudioSegment
from pydub.silence import split_on_silence
AUDIO_FILE = "/content/drive/MyDrive/Speech_Technology/Audios/speaker_female_1.wav"
r = sr.Recognizer()
with sr.AudioFile(AUDIO_FILE) as source:
    audio = r.record(source)  # read the entire audio file
    print("Recognized Speech: \n" + r.recognize_google(audio))
!pip install ibm_watson
from ibm_watson import SpeechToTextV1
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
apikey='FoQQPWQYE0B-3i38r1IbI_20uzPYHiF8JMHND1DuQ6yG' ## qui ci va il tuo Apikey che crei nel profilo
url='https://api.eu-gb.speech-to-text.watson.cloud.ibm.com/instances/36876297-be6a-479d-9f8a-f34ef6a63c31' # il tuo url

authenticator = IAMAuthenticator(apikey)
stt = SpeechToTextV1(authenticator=authenticator)

stt.set_service_url(url)
stt.set_disable_ssl_verification(True)
with open("/content/drive/MyDrive/Speech_Technology/Audios/Es_andalucian_audios/dani2.wav", 'rb') as f:  
  res = stt.recognize(audio=f, content_type='audio/wav', model ='es-ES_NarrowbandModel').get_result()

res

for el in res["results"]:
  for l in el["alternatives"]:
    st.write(l["transcript"])
   audio_text= 
for el["results"] in res['results'][0]['alternatives'][0]['transcript']
st.write(audio_text)
