import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.dates import AutoDateFormatter, AutoDateLocator, date2num
import os

def displayStockPerformance(start, end, changes):
    files = [f for f in os.listdir('.') if os.path.isfile(f)]

    for f in files:
        filename, ext = os.path.splitext(f)
        if ext == '.csv':
            data = pd.read_csv(f)
            fig, ax = plt.subplots(figsize=(24,8))
            date = pd.to_datetime(data["Date"])
            plt.plot(date, data["Close"])
            plt.xlabel("Date", fontsize="16")  
            plt.ylabel("Price", fontsize="16")
            plt.title("Stock Performance of " + filename + " on LSE between " + start + " and " + end)
            plt.legend()
            fig.canvas.manager.set_window_title(filename + "'s Stock Performance")
            plt.show()

def WriteKeyDetailsToFile(changes):
    with open("Key Dates.txt", "w") as f:
        f.write("Largest Daily Increase and Decrease\n\n")
        for change in changes:
            f.write("For " + change[0] + ", the sharpest drop in stock price was " + str(round(change[1],2)) + " on " + change[2] + ".  The largest increase was " + str(round(change[3])) + " on " + change[4] + ".\n\n")
        
    f.close()