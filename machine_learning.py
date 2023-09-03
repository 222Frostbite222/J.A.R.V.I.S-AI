
# Importing required libraries
from sklearn.linear_model import LinearRegression
from sklearn.cluster import KMeans
import numpy as np
import pandas as pd

# Linear Regression for Predictive Analytics
def predictive_analytics(data):
    try:
        X = np.array(data['X']).reshape(-1, 1)
        y = np.array(data['y']).reshape(-1, 1)
        model = LinearRegression()
        model.fit(X, y)
        prediction = model.predict(np.array([[data['predict']]]))
        return prediction[0][0]
    except Exception as e:
        print(f"An error occurred in predictive analytics: {e}")
        return None

# K-Means Clustering for Recommendations
def make_recommendations(data, n_clusters):
    try:
        kmeans = KMeans(n_clusters=n_clusters)
        kmeans.fit(data)
        labels = kmeans.labels_
        recommendations = pd.DataFrame(data, columns=['Feature1', 'Feature2'])
        recommendations['Cluster'] = labels
        return recommendations
    except Exception as e:
        print(f"An error occurred in making recommendations: {e}")
        return None

# Personalization Algorithm (Simple Example)
def personalize(data, user_preferences):
    try:
        personalized_data = data.copy()
        for feature, weight in user_preferences.items():
            personalized_data[feature] *= weight
        return personalized_data
    except Exception as e:
        print(f"An error occurred in personalization: {e}")
        return None

# Main function to demonstrate machine learning functionalities
def main():
    # Sample data for predictive analytics
    predictive_data = {'X': [1, 2, 3, 4, 5], 'y': [2, 4, 3, 3, 5], 'predict': 6}
    prediction = predictive_analytics(predictive_data)
    print(f"Prediction for the given data: {prediction}")

    # Sample data for making recommendations
    recommendation_data = np.array([[1, 2], [5, 8], [1.5, 1.8], [8, 8], [1, 0.6], [9, 11]])
    recommendations = make_recommendations(recommendation_data, 2)
    print(f"Recommendations:\n{recommendations}")

    # Sample data and user preferences for personalization
    personalization_data = pd.DataFrame({'Feature1': [1, 2, 3], 'Feature2': [4, 5, 6]})
    user_preferences = {'Feature1': 0.7, 'Feature2': 1.3}
    personalized_data = personalize(personalization_data, user_preferences)
    print(f"Personalized Data:\n{personalized_data}")

# Entry point of the program
if __name__ == "__main__":
    main()
