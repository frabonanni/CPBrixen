import streamlit as st
import speech_recognition as sr

import os

from pydub import AudioSegment
from pydub.silence import split_on_silence

def silence_based_conversation(path):
    song = AudioSegment.from_wav(path)
    fh= open("recognized.txt", "w+")
    # split track where silence is 0.5 seconds 
    # or more and get chunks
    chunks = split_on_silence(song,silence_thresh = -16)
    i = 0
    st.write("hello")
    for chunk in chunks:
        chunk_silent= AudioSegment.silent(duration = 10)
        audio_chunk.export("./chunk{0}.wav".format(i), bitrate ='192k', format ="wav")
        filename = 'chunk'+str(i)+'.wav'
  
        st.write("Processing chunk "+str(i))                  
                            
        r = sr.Recognizer()
        
        with sr.AudioFile(filename) as source:
             audio = r.record(source)  
             recognised_text= r.recognize_google(audio)
             st.text('the text recognized from the audio seems to be: ')
             st.text( recognised_text)
audiofile = st.file_uploader("Upload wav file")
if audiofile is not None:
    silence_based_conversation(audiofile)
