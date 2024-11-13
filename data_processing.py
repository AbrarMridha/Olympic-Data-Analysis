import pandas as pd
import numpy as np

def load_data(filename):
    # Load the dataset and handle missing values
    data = pd.read_csv(filename)
    data['Age'] = data['Age'].fillna(data['Age'].median())
    data['Height'] = data['Height'].fillna(data['Height'].mean())
    data['Weight'] = data['Weight'].fillna(data['Weight'].mean())
    return data

def get_medal_counts_by_country(data):
    # Filter only rows where a medal was won
    medal_data = data.dropna(subset=['Medal'])
    # Calculate the total medal count for each country
    country_medal_counts = medal_data['NOC'].value_counts().reset_index()
    country_medal_counts.columns = ['Country', 'Total Medals']
    return country_medal_counts