# Flight-Delay-Analysis

# Pacific Northwest Flight Delays and Cancellations Analysis

This project focuses on analyzing flight data from the Pacific Northwest (PNW) in 2022, to determine the factors influencing departure delays and cancellations.

## Table of Contents
- [Project Overview](#project-overview)
- [Objectives](#objectives)
- [Tools Used](#tools-used)
- [Analysis](#analysis)
- [Conclusion](#conclusion)

## Project Overview
The aviation industry is dynamic, with various factors influencing flight operations. The goal of this project is to analyze flight data from two major airports in the Pacific Northwest (SEA and PDX) to investigate the impact of weather conditions, routes, and airlines on departure delays and cancellations.

## Objectives
- Identify routes and airlines with the highest number of cancellations.
- Explore the influence of weather conditions on flight delays.
- Visualize the distribution of delays and cancellations for better insights.

## Tools Used
- `pandas`: For data manipulation and analysis.
- `matplotlib`: For creating visualizations.
- `seaborn`: For advanced data visualization.
- PostgresSQL

## Analysis
1.  **Flight Route Delays and Cancellations**:
    - Group flights by route to find the average departure delay and number of canceled flights.
    - Visualize the top 9 routes with the highest number of cancellations.
    
2.  **Airline Delays and Cancellations**:
    - Group by airline to calculate average delay and count of cancellations.
    - Create a bar plot to show airlines with the most cancellations.

3.  **Weather Impact on Delays**:
    - Group data by wind speed (greater or less than 10 mph) to analyze its effect on delays at each airport.
    - If the precipitation (greater than 20) level impact the delays

## Conclusion
The findings provide valuable insights for both airlines and passengers, suggesting that weather conditions, particularly wind gusts, play a significant role in flight delays. Further steps could involve deeper analysis into other variables like seasonal trends and airline-specific operational issues.
