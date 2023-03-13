import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.dates import AutoDateFormatter, AutoDateLocator, date2num
import os

def displayStockPerformance(start, end):
    files = [f for f in os.listdir('.') if os.path.isfile(f)]

    for f in files:
        filename, ext = os.path.splitext(f)
        if ext == '.csv':
            data = pd.read_csv(f)
            fig = plt.figure(figsize=(24, 8))
            date = pd.to_datetime(data["Date"])
            plt.plot(date, data["Close"])
            plt.xlabel("Date", fontsize="16")  
            plt.ylabel("Price", fontsize="16")
            plt.title("Stock Performance of " + filename + "on LSE between " + start + " and " + end)
            plt.legend()
            fig.canvas.manager.set_window_title(filename + "'s Stock Performance")
            plt.show()
