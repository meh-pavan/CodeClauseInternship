# -*- coding: utf-8 -*-
"""
Created on Mon Jan  6 16:24:58 2025

@author: PAVAN
"""

import streamlit as st
from textblob import TextBlob

def analyzing_sentiment(text):
    polarity = TextBlob(text).sentiment.polarity
    return polarity
    
st.title("Sentiment Analysis")

text = st.text_input('Enter Text to analyze its sentiment')

if st.button("Analyze Sentiment"):
    polarity = analyzing_sentiment(text)
    if polarity >0.33:
        st.write("Positive")
    elif polarity < -0.33:
        st.write("Negative")
    else:
        st.write("Neutral")