import streamlit as st
import sklearn
import joblib
import numpy as np
model = joblib.load('model')
st.title('Sentiment Analyser')
ip = st.text_input('Enter your remarks:')
ip = np.reshape(-1,1)
op = model.predict([ip])
if st.button('Predict'):
  st.title(op[0])
