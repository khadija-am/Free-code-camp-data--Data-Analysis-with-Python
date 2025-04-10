import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
 df = pd.read_csv('epa-sea-level.csv')

    # Create scatter plot
    plt.scatter(df['Year'], df['CSIRO Adjusted Sea Level'], color='blue', label='Data')


    # Create first line of best fit
    slope, intercept, r_value, p_value, std_err = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
    years_extended = range(1880, 2051)  # Extend the years to 2050 for prediction
    sea_levels_extended = [slope * year + intercept for year in years_extended]
    plt.plot(years_extended, sea_levels_extended, color='red', label='Best Fit Line (1880 - 2050)')


    # Create second line of best fit
    df_recent = df[df['Year'] >= 2000]  # Filter data from 2000 onwards
    slope_recent, intercept_recent, r_value, p_value, std_err = linregress(df_recent['Year'], df_recent['CSIRO Adjusted Sea Level'])
    sea_levels_recent = [slope_recent * year + intercept_recent for year in years_extended]
    plt.plot(years_extended, sea_levels_recent, color='green', label='Best Fit Line (2000 - 2050)')


    # Add labels and title
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.title('Rise in Sea Level')
    plt.legend()
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()