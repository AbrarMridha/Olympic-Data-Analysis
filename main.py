import pandas as pd
import sqlite3
from data_processing import load_data, get_medal_counts_by_country
from data_visualization import plot_top_countries_medals

# Load the data
data_file = 'athlete_events.csv'
data = load_data(data_file)

# Get country-specific medal counts
country_medal_counts = get_medal_counts_by_country(data)

# Plot the top countries by medal count
plot_top_countries_medals(country_medal_counts)

conn = sqlite3.connect(':memory:')  # Use an in-memory database
data.to_sql('athlete_data', conn, index=False, if_exists='replace')

# Query for top medal-winning countries
top_countries_query = '''
SELECT NOC AS Country, COUNT(Medal) AS Total_Medals
FROM athlete_data
WHERE Medal IS NOT NULL
GROUP BY NOC
ORDER BY Total_Medals DESC
LIMIT 10;
'''
top_countries = pd.read_sql(top_countries_query, conn)
print(top_countries)