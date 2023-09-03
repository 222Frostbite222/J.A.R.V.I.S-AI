
# Importing required libraries
from textblob import TextBlob
from sklearn.linear_model import LinearRegression
import numpy as np

# Sentiment Analysis function
def sentiment_analysis(text):
    try:
        blob = TextBlob(text)
        sentiment_polarity = blob.sentiment.polarity
        sentiment_subjectivity = blob.sentiment.subjectivity
        
        if sentiment_polarity > 0:
            sentiment = 'positive'
        elif sentiment_polarity < 0:
            sentiment = 'negative'
        else:
            sentiment = 'neutral'
        
        print(f"Sentiment: {sentiment}, Polarity: {sentiment_polarity}, Subjectivity: {sentiment_subjectivity}")
    except Exception as e:
        print(f"An error occurred in sentiment analysis: {e}")

# Predictive Analytics function
def predictive_analytics(data):
    try:
        # Converting data to NumPy array and reshaping it
        data_array = np.array(data).reshape(-1, 1)
        
        # Create target variable (Y value), assuming it is one step ahead of the input
        target = data_array[1:]
        
        # Removing the last element from the original data to match the shape of the target variable
        data_array = data_array[:-1]
        
        # Create a Linear Regression model and fit it to the data
        model = LinearRegression()
        model.fit(data_array, target)
        
        # Make a prediction for the next data point
        next_point = model.predict(np.array([[data_array[-1]]]))
        
        print(f"Predicted next data point: {next_point[0][0]}")
    except Exception as e:
        print(f"An error occurred in predictive analytics: {e}")
