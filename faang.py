#!/usr/bin/env python

# Importing libraries
# Dates and times
import datetime as dt
# Data frames
import pandas as pd
# File system operations
import os
#  Yahoo Finance yfinance module to fetch stock data
import yfinance as yf
# For finding files using patterns
import glob
# Matplotlib for plotting
import matplotlib.pyplot as plt

def get_data():
    # FAANG tickers
    tickers = ["META", "AAPL", "AMZN", "NFLX", "GOOG"]
    # Download data for the past 5 days for FAANG
    # https://ranaroussi.github.io/yfinance#ticker
    data = yf.download(tickers, period="5d", interval="1h", auto_adjust=True)
    # Ensure data/ directory exists
    os.makedirs("data", exist_ok=True)
    # Create filename with the current date and time
    # https://docs.python.org/3/library/datetime.html
    # Getting current date and time for filename with format YYYYMMDD-HHmmss
    # https://docs.python.org/3/library/datetime.html#datetime.datetime.now
    filename = dt.datetime.now().strftime("%Y%m%d-%H%M%S") + ".csv"
    # Creating a full file path (including the filename) for saving the stock data
    filepath = os.path.join("data", filename)
    # Saving the CSV file in the data folder with name as per the specified format
    # https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.to_csv.html
    data.to_csv(filepath)
    print(f"Data saved to {filepath}")
    print (data.head())

def plot_data():
    # Find the latest CSV in data/ using glob
    # https://docs.python.org/3/library/glob.html
    csv_files = glob.glob('data/*.csv')
    if not csv_files:
        # If no csv file exists, return
        print("No CSV files found in data/")
        return
    # Get the latest CSV file using os.path.getctime
    # https://www.geeksforgeeks.org/python/python-os-path-getctime-method/
    latest_csv = max(csv_files, key=os.path.getctime)

    # Load CSV with multi-index columns
    # https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.read_csv.html
    df = pd.read_csv(latest_csv, header=[0, 1], index_col=0, parse_dates=True)

    # Plot Close prices for all available tickers
    plt.figure(figsize=(12, 6))

    # Get all tickers in the second level of the multi-index columns
    # We need it for ticker in df.columns.levels[1]: because our CSV uses a MultiIndex for columns:
    # 1. The first level is the price type (Close, High, etc.)
    # 2. The second level is the ticker symbol (AAPL, AMZN, etc.)
    # df.columns.levels[1] gives all unique ticker symbols. So we can loop for each ticker symbol
    # https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.MultiIndex.levels.html
    # I also had some help from ChatGPT to get tickers under the "Close" price type
    # https://chatgpt.com/share/68ffd5b2-6fe4-800f-82bb-25299b654018
    tickers_close = [ticker for price_type, ticker in df.columns if price_type == "Close"]
    # Loop through each ticker and plot its Close price
    for ticker in tickers_close:
        # Plot Close price for each ticker
        # https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.plot.html
        plt.plot(df.index, df[("Close", ticker)], label=ticker)
    # Add axis labels, legend, and title
    plt.xlabel("Time")
    plt.ylabel("Close Price")
    plt.legend()
    plt.title(f"FAANG Close Prices - {os.path.basename(latest_csv).split(".")[0]}")

    # Save plot
    os.makedirs("plots", exist_ok=True)
    # Format the filename with date and time
    # https://docs.python.org/3/library/datetime.html#strftime-and-strptime-behavior
    out_path = f"plots/{dt.datetime.now().strftime('%Y%m%d-%H%M%S')}.png"
    # Save plot
    # https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.savefig.html
    plt.savefig(out_path)
    # Close plot to free up memory
    # https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.close.html
    plt.close()

print("Starting FAANG data collection and plotting...")
get_data()
plot_data()
print("Done!")