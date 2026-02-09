Real-Time Comment Sentiment Analysis Dashboard
Overview

This project is a Streamlit-based Sentiment Analysis Dashboard that allows users to submit comments and instantly view their sentiment (Positive, Negative, or Neutral).
The system stores comments in a SQLite database and dynamically displays sentiment distribution using charts and summary insights.

Features

Real-time comment sentiment analysis

Automatic sentiment detection using NLP

SQLite database storage for comments

Sentiment summary dashboard

Pie chart visualization of sentiment distribution

Business suggestion engine based on sentiment trends

Project Structure
project/
│
├── app.py            # Streamlit dashboard application
├── sentiment.py      # Sentiment analysis logic
├── database.py       # SQLite database operations
├── comments.db       # Database file (auto-created)
└── README.md

Technologies Used

Python

Streamlit

TextBlob (NLP)

SQLite

Matplotlib

How It Works

Users enter comments through the dashboard.

The application analyzes sentiment using TextBlob.

Comments and sentiment labels are stored in a SQLite database.

The dashboard displays total comments and sentiment distribution with charts.

Based on sentiment ratios, business suggestions are automatically generated.

The main application processes user comments, stores results, and displays visualization summaries. 

app


Database operations such as table creation, insertion, and aggregation are handled through SQLite functions. 

database


Sentiment classification is performed using polarity scoring from TextBlob. 

sentiment

Installation
pip install streamlit textblob matplotlib meansqlite3
python -m textblob.download_corpora

Run the Application
streamlit run app.py

Use Cases

Customer feedback analysis

Product review monitoring

Social media sentiment tracking

Service quality monitoring dashboards
