#! python3
import json,requests
from pprint import pprint

## Access a word-finding query engine
## See API at http://www.datamuse.com/api/

#this library handles the query with the API so we do not need the following steps:
#Step1: Check the API documentation to see if the APIkey is needed. 
#No APIkey needed.


#Step2: Check API documentation to see what structure of URL is needed to access the data?
#For finding rhyming words for the keyword 'funny', the URL looks like this:
#'https://api.datamuse.com/words?rel_rhy=funny'
# make the above URL more generic, so that it is easy to replace the keyword
keyword=input('plz give me a keyword')
url1= 'https://api.datamuse.com/words?rel_syn=' + keyword + '&max=5'
url2 = 'https://api.datamuse.com/words?rel_ant=' + keyword + '&max=5'


#Step3: Download the JSON data from the API.
response1 = requests.get(url1) 
response2 = requests.get(url2) 
#Uncomment to see the raw JSON text:
#print(response.text)  


#Step4: Load JSON data into a Python variable and use it in your program.
dataFromDatamuse1 = json.loads(response1.text)
dataFromDatamuse2 = json.loads(response2.text)
#print(dataFromDatamuse1)
#print(dataFromDatamuse2)




#Uncomment to see the raw JSON text loaded in a Python Variable:
#print(dataFromDatamuse) 
#Uncomment to see a better readable version:
#pprint(dataFromDatamuse) #dont forget to import the correct pprint library to make this work
pprint(dataFromDatamuse1[0:4])#if you just want to see the first 9 results
pprint(dataFromDatamuse2[0:4])

option = st.selectbox(
     'Which synonym would you choose?',
     ('great', 'special', 'rare'))

st.write('You selected:', option)
