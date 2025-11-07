# computer-infrastructure

## Overview
This project is an assessment for ATU University focused on computer infrastructure, with a particular emphasis on financial data analysis using Python. 
It includes tools to download, process, and visualize stock data for major technology companies (FAANG: META, AAPL, AMZN, NFLX, GOOG).

## How to Run the Notebook

1. **Install Dependencies**
   - Make sure you have Python 3.8+ installed.
   - Install required packages using pip:
     ```bash
     pip install -r requirements.txt
     ```

2. **Download Data**
   - Run the `get_data()` function (provided in `faang.py`) to download the latest FAANG stock data. This will save a CSV file in the `data/` folder.

3. **Open and Run the Notebook**
   - Open `problems.ipynb` in Jupyter Notebook, PyCharm, or VSCode.
   - Run the cells sequentially to perform the analysis and view the plots.

## Folder Structure
- `faang.py` — Python functions for data download and processing
- `problems.ipynb` — Main notebook for analysis
- `data/` — Contains downloaded CSV stock data
- `plots/` — Contains generated plots
- `requirements.txt` — Python dependencies

## Notes
- The data folder will be created automatically if missing.
- Data is downloaded using the [yfinance](https://github.com/ranaroussi/yfinance) package.
