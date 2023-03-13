# Importing the yfinance package
import yfinance as yf

# Set the start and end date
start_date = '2014-01-01'
end_date = '2021-12-31'

# Set the ticker
tickers = ['LLOY.L', 'NWG.L', 'BARC.L']

# Get the data
def downloadData(tickers, start_date, end_date):
    for x in tickers:
        try:
            print("Sourcing data for " + x)
            stockdata = yf.download(x, start_date, end_date)
            stockdata["Date"] = stockdata.index
            stockdata = stockdata[["Open", "High", "Low", "Close", "Adj Close", "Volume"]]
            stockdata.to_csv("{}.csv".format(x))
            print("Write complete")
        except Exception as e:
            print("There was a problem sourcing data for {x}")
