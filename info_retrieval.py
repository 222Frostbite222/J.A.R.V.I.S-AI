
# Importing required libraries
import requests
from bs4 import BeautifulSoup
import pandas as pd
import matplotlib.pyplot as plt

# Web Search function using Google Search (not for commercial use)
def perform_web_search(query):
    try:
        # Construct the URL
        url = f"https://www.google.com/search?q={query}"
        
        # Make the request and get the content
        response = requests.get(url)
        
        # Parse the HTML content
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Find and print the first link
        link = soup.find('a')
        if link:
            print(f"First search result for {query}: {link.get('href')}")
        else:
            print("No search results found.")
    except Exception as e:
        print(f"An error occurred in web search: {e}")

# Data Analysis function to provide insights
def analyze_data(data):
    try:
        # Convert the data into a DataFrame
        df = pd.DataFrame(data, columns=['Value'])
        
        # Calculate basic statistics
        mean = df['Value'].mean()
        median = df['Value'].median()
        std_dev = df['Value'].std()
        
        print(f"Mean: {mean}, Median: {median}, Standard Deviation: {std_dev}")
        
        # Generate a simple plot
        plt.plot(df['Value'])
        plt.title('Data Analysis')
        plt.xlabel('Index')
        plt.ylabel('Value')
        plt.show()
    except Exception as e:
        print(f"An error occurred in data analysis: {e}")
