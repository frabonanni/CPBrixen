import json, requests
from streamlit import st
from pprint import pprint

url = 'https://en.wikipedia.org/w/api.php?action=query&format=json&list=search&srsearch=art&srlimit=3'
response = requests.get(url)
dataFromWikipedia = json.loads(response.text)

from bs4 import BeautifulSoup
textwithHTMLtags = '<span class="searchmatch">>ART</span>is a diverse range of (the products of) human activities involving the conscious use of creative imagination to express technical proficiency, beauty'

soup = BeautifulSoup(textwithHTMLtags)

 
textwithoutHTMLtags = soup.get_text()
st.write(textwithoutHTMLtags)

keyword= st.text_input('plz give me a keyword', 'word')
option = st.selectbox('What you want to know about?')
st.write('')
