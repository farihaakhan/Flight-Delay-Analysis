# Import required libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns  # Import seaborn for plotting

# Start your code here!
# Load the datasets
df1 = pd.read_csv('flights2022.csv')
df2 = pd.read_csv('flights_weather2022.csv')

# Create new column, combining others
df2['Route'] = df2['origin'] + '-' + df2['dest']


# Group by 'Route' and aggregate 'dep_delay' mean and count of null 'dep_time'
routes_delays_cancels = df2.groupby('Route').agg(
    avg_dep_delay =('dep_delay', 'mean'),
    high_cancelled_flights=('dep_time', lambda x: x.isnull().sum())
).reset_index()

# Airline Delays
airlines_delays_cancels = df2.groupby('airline').agg(
    avg_dep_delay =('dep_delay', 'mean'),
    high_cancelled_flights=('dep_time', lambda x: x.isnull().sum())
).reset_index()

# Create a bar graph for highest number of cancellations by Routes
top9_route_cancels_bar = routes_delays_cancels.nlargest(9, 'high_cancelled_flights')
sns.barplot(data=top9_route_cancels_bar, y='high_cancelled_flights', x='Route', palette='inferno', order=top9_route_cancels_bar['Route'])
plt.title('Top 9 Routes with Highest Number of Cancellations')
plt.xlabel('Route')
plt.xticks(rotation=45)
plt.ylabel('Total Cancellations')
plt.show()
plt.close()

# Create a bar graph for highest number of cancellations by Airlines
top9_airline_cancels_bar = airlines_delays_cancels.nlargest(9, 'high_cancelled_flights')
sns.barplot(data=top9_airline_cancels_bar, y='high_cancelled_flights', x='airline', palette='plasma', order=top9_airline_cancels_bar['airline'])
plt.title('Top 9 Airline with Highest Number of Cancellations')
plt.xlabel('Airline')
plt.xticks(rotation=90,fontsize=8)
plt.ylabel('Total Cancellations')
plt.show()
plt.close()

# Are departure delays impacted by 10+ mph winds from each airport
df2["Wind Gust Group"] = df2["wind_gust"].apply(lambda x: ">= 10mph" if x >= 10 else "< 10 mph")
wind_grouped_data = df2.groupby(["Wind Gust Group", "origin"]).agg(
    Avg_dep_delay=("dep_delay", "mean")
)
wind_grouped_data
