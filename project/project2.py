import streamlit as st
import speech_recognition as sr

import os

from pydub import AudioSegment
from pydub.silence import split_on_silence

def silence_based_conversation(path = "alice-medium.wav"):
    song = AudioSegment.from_wav(path)
    fh= open("recognized.txt", "w+")
    # split track where silence is 0.5 seconds 
    # or more and get chunks
    chunks = split_on_silence(song,
        # must be silent for at least 0.5 seconds
        # or 500 ms. adjust this value based on user
        # requirement. if the speaker stays silent for 
        # longer, increase this value. else, decrease it.
        min_silence_len = 500,
  
        # consider it silent if quieter than -16 dBFS
        # adjust this per requirement
        silence_thresh = -16
        i = 0
     for chunk in chunks:
         chunk_silent= AudioSegment.silent(duration = 10)
         chunk.export(("./chunk{0}.wav".format(i), bitrate ='192k', format ="wav")
         filename = 'chunk'+str(i)+'.wav'
  
        st.write("Processing chunk "+str(i))                  
        file = filename                      
        r = sr.Recognizer()
        uploaded_file = st.file_uploader("Choose a file")
        if uploaded_file is not None:
            with sr.AudioFile(uploaded_file) as source:
                audio = r.record(source)  
                recognised_text= r.recognize_google(audio)
                st.text('the text recognized from the audio seems to be: ')
                st.text( recognised_text)

