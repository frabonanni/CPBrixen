#! python3
import json,requests
import streamlit as st
from pprint import pprint

keyword= st.text_input('plz give me a keyword', 'word')
option = st.selectbox('Do you prefer synonyms or antonyms of the word you chose?',('synonym', 'antonym'))
st.write('You selected:', option)

url1= 'https://api.datamuse.com/words?rel_syn=' + keyword + '&max=5'
url2 = 'https://api.datamuse.com/words?rel_ant=' + keyword + '&max=5'
if option == 'synonym':
   url = url1
else:
   url = url2



#Step3: Download the JSON data from the API.
response = requests.get(url)  
#Uncomment to see the raw JSON text:
#print(response.text)  


#Step4: Load JSON data into a Python variable and use it in your program.
dataFromDatamuse = json.loads(response.text)

#print(dataFromDatamuse1)
#print(dataFromDatamuse2)


#Uncomment to see the raw JSON text loaded in a Python Variable:
#print(dataFromDatamuse) 
#Uncomment to see a better readable version:
#pprint(dataFromDatamuse) #dont forget to import the correct pprint library to make this work

st.text("dataFromDatamuse[0:4]")
