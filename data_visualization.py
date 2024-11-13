import matplotlib.pyplot as plt

def plot_top_countries_medals(country_medal_counts, top_n=10):
    # Plot the top countries by total medal count
    top_countries = country_medal_counts.head(top_n)
    plt.figure(figsize=(10, 6))
    plt.bar(top_countries['Country'], top_countries['Total Medals'], color='skyblue')
    plt.xlabel('Country')
    plt.ylabel('Total Medals')
    plt.title(f'Top {top_n} Countries by Total Medals')
    plt.show()