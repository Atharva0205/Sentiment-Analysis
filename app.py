import streamlit as st
import sklearn
import joblib
model = joblib.load('model')
st.title('Sentiment Analyser')
ip = st.text_input('Enter your remarks:')
ip = ip.reshape(-1,1)
op = model.predict([ip])
if st.button('Predict'):
  st.title(op[0])
