import os
import importlib
import datetime
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt



subset = importlib.import_module('.data.01_subset-data-GBP', 'src') #since my modules start with digit the . allows python to interpret
plotwines = importlib.import_module('.visualization.02_visualize-wines', 'src')
country_sub = importlib.import_module('.data.03_country-subset', 'src')

#remember the prompt:
# Generate a subset of winemag-130k-v2.csv containing only the following columns: country, designation, points, price (in GBP). Save in a .csv file
# Generate and save a table of wines only produced in Chile
# Save a scatterplot of the wines points vs price and a distribution plot of wine scores


#subset_data inputs in filename and outputs fname which contains country, designation, points, price (in GBP).

#plotwines contaning the functions to visualize the wines distribution using a subset data


# ------------------------------------------------------------------------
# Declare variables
# ------------------------------------------------------------------------

# Set raw data path
raw_data = "data/raw/winemag-data-130k-v2.csv"

# Set country
country = "Chile"

# ------------------------------------------------------------------------
# Perform analysis
# ------------------------------------------------------------------------

if __name__ == '__main__': #ie if pythin is running this module as the source file (ie if it's called directly)
    # create the subset of the initial dataframe
    subset_file = subset.process_data_GBP(raw_data)  #inorder to call the functions we need to put the names defined above . before them. 
    # prints out the name of the new file created
    print(subset_file)
    # generate the plots
    plotwines.create_plots(subset_file)
    # subset the data for the country given 
    country_file = country_sub.get_country(subset_file, country)
    print(country_file)