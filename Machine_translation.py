import streamlit as st 
import spacy_streamlit as spt 
import spacy

from transformers import pipeline
pipe = pipeline("translation", model="DunnBC22/opus-mt-de-en-OPUS_Medical_German_to_English")

from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
tokenizer = AutoTokenizer.from_pretrained("DunnBC22/opus-mt-de-en-OPUS_Medical_German_to_English")
model = AutoModelForSeq2SeqLM.from_pretrained("DunnBC22/opus-mt-de-en-OPUS_Medical_German_to_English")

st.title('German to English Translation')
menu = ['Home','translate']
choice = st.sidebar.selectbox('menu', menu) 
if choice =='Home':
    st.subheader('This is an bot which translate german into english')
    st.image("OSK.jpg")
    st.write('''streamlit: Used for creating web-based applications with Python.spacy_streamlit: A Streamlit component for visualizing SpaCy NLP models.pipeline, AutoTokenizer, AutoModelForSeq2SeqLM: Components from the Hugging Face transformers library for handling translation tasks''')
elif choice == 'translate':
    st.subheader('German to English')
    raw_text = st.text_area('Text To Translate', 'Enter Text Here') 
    docs = pipe(raw_text)
    if st.button('Translate'):
        st.write(docs[0]["translation_text"])