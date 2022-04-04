from googletrans import Translator
translator = Translator()

word = st.text_input('Gimme a word to translate ')
destlang= st.text_input('Tell me a two letter code for the destination language like es or en: ')
