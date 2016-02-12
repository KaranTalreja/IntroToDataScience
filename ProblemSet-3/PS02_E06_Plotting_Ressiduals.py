import numpy as np
import scipy
import matplotlib.pyplot as plt
from PS02_E05_Linear_Regression import predictions
import pandas
import random

def plot_residuals(turnstile_weather, predictions):
    '''
    Using the same methods that we used to plot a histogram of entries
    per hour for our data, why don't you make a histogram of the residuals
    (that is, the difference between the original hourly entry data and the predicted values).
    Try different binwidths for your histogram.

    Based on this residual histogram, do you have any insight into how our model
    performed?  Reading a bit on this webpage might be useful:

    http://www.itl.nist.gov/div898/handbook/pri/section2/pri24.htm
    '''
    
    plt.figure()
    (turnstile_weather["ENTRIESn_hourly"] - predictions).hist()
    return plt

if __name__ == "__main__":
    dataframe = pandas.read_csv("turnstile_data_master_with_weather.csv")
    num_rows = len(dataframe)
    indices = random.sample(xrange(num_rows),int(num_rows*0.15))
    selected = [False]*num_rows
    for index in indices:
        selected[index] =  True
    prediction,plot,coeff = predictions(dataframe[selected])
    plot_residuals(dataframe[selected],prediction).show()