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
            biggestChange = 0.0
            dateofChange = "2022/01/01"
            for index, row in df.iterrows():
                
                if abs(row["Change in Share Price"]) > biggestChange:
                    biggestChange = row["Change in Share Price"]
                    dateofChange = row["Date"]

                    if row["Change in Share Price"] < 0:
                        negativeNum = True
                    else:
                        negativeNum = False     
            
        changes.append([filename, biggestChange, negativeNum, dateofChange])
    return changes 


