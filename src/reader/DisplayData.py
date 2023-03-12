import pandas as pd
import datetime
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.dates import AutoDateFormatter, AutoDateLocator, date2num
import os

files = [f for f in os.listdir('.') if os.path.isfile(f)]

for f in files:
    filename, ext = os.path.splitext(f)
    if ext == '.csv':
        data = pd.read_csv(f)
        fig, ax = plt.subplots(figsize=(24, 8))
        date = pd.to_datetime(data["Date"])
        plt.plot(date, data["Close"])
        plt.xlabel("Date")  
        plt.ylabel("£price")
        plt.title(filename)
        plt.legend()
        plt.show()

    
    '''data = pd.read_csv("BARC.L.csv")
    plt.figure(figsize=(10,10))
    plt.plot(data.index, data["Close"])
    plt.xlabel("Date")
    plt.ylabel("£price")
    plt.title("")
    plt.legend()
    plt.show()'''
'''    plt.plot(data["Date"], data['Close'])'''


