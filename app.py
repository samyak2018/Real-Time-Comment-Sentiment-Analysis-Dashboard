import streamlit as st
import matplotlib.pyplot as plt
from sentiment import analyze_sentiment
from database import create_table, insert_comment, get_counts

create_table()

st.title("Real-Time Comment Sentiment Analysis Dashboard")

comment = st.text_area("Enter your comment")

if st.button("Analyze & Submit"):
    if comment.strip() != "":
        sentiment = analyze_sentiment(comment)
        insert_comment(comment, sentiment)
        st.success(f"Sentiment: {sentiment}")
    else:
        st.warning("Please enter a comment")

data = get_counts()

sentiments = {"Positive": 0, "Negative": 0, "Neutral": 0}
total = 0

for s, c in data:
    sentiments[s] = c
    total += c

st.subheader("Summary")
st.write("Total Comments:", total)
st.write("Positive:", sentiments["Positive"])
st.write("Negative:", sentiments["Negative"])
st.write("Neutral:", sentiments["Neutral"])

if total > 0:
    fig, ax = plt.subplots()
    ax.pie(sentiments.values(), labels=sentiments.keys(), autopct="%1.1f%%")
    st.pyplot(fig)

st.subheader("Business Suggestion")

if total > 0:
    neg = (sentiments["Negative"] / total) * 100
    pos = (sentiments["Positive"] / total) * 100

    if neg >= 40:
        st.error("High negative feedback detected. Immediate improvement required.")
    elif pos >= 60:
        st.success("Overall sentiment is positive. Maintain service quality.")
    else:
        st.info("Mixed feedback observed. Analyze comments for improvement.")

import streamlit as st
st.title("Test App Working")
