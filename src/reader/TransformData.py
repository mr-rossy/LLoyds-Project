import pandas as pd
import matplotlib.pyplot as plt
import os.path
from datetime import datetime


def AddChangeInSharePrice():
    files = [f for f in os.listdir('.') if os.path.isfile(f)]
    for f in files:
        filename, ext = os.path.splitext(f)
        if ext == '.csv':
            tempdata = pd.read_csv(f)
            tempdata.insert(1,"Ticker", filename)
            print("Adding daily change in share price")
            tempdata["Change in Share Price"] = tempdata["Open"] - tempdata["Close"]
            tempdata.to_csv("{}".format(f))


def GetBiggestDailyJump():
    files = [f for f in os.listdir('.') if os.path.isfile(f)]
    changes = []
    for f in files:
        filename, ext = os.path.splitext(f)
        if ext == '.csv':
            df = pd.read_csv(f)
            largestDailyIncrease = 0.0
            largestDailyDecrease = 0.0
            dateofIncrease = "2022/01/01"
            dateofDecrease = "2022/01/01"
            for index, row in df.iterrows():
                if row["Change in Share Price"] > 0:
                    if index == 0:
                        largestDailyIncrease = row["Change in Share Price"]
                        dateofIncrease = row["Date"]
                    elif row["Change in Share Price"] > largestDailyIncrease:
                        largestDailyIncrease = row["Change in Share Price"]
                        dateofIncrease = row["Date"]
                                        
                elif row["Change in Share Price"] < 0:
                    if index == 0:
                        largestDailyDecrease = row["Change in Share Price"]
                        dateofDecrease = row["Date"]
                    elif row["Change in Share Price"] < largestDailyDecrease:
                        largestDailyDecrease = row["Change in Share Price"]
                        dateofDecrease = row["Date"]
  
            
        changes.append([filename, largestDailyDecrease, dateofDecrease, largestDailyIncrease, dateofIncrease])
    return changes 


