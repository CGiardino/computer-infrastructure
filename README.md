# Computer Infrastructure Project

This project is an assessment for ATU University focused on computer infrastructure, with a particular emphasis on financial data analysis using Python. 
It includes tools to download, process, and visualize close prices of stock data for major technology companies (FAANG: META, AAPL, AMZN, NFLX, GOOG).

## How to Run the Notebook

1. **Install Dependencies**
   - Make sure you have Python 3.8+ installed.
   - Install required packages using pip:
     ```bash
     pip install -r requirements.txt
     ```
2. **Open and Run the Notebook**
   - Open `problems.ipynb`.
   - Run the cells sequentially to perform the analysis and view the plots.

3. **View the Data and Plots**
   - The downloaded stock data will be saved in the `data/` folder with the timestamp of the run.
   - The plots will be saved in the `plots/` folder with the timestamp of the run.

4. **Run by script**
    - You can also run the analysis directly via the command line:
      ```bash
      python faang.py
      ```

## Folder Structure
- `faang.py` — Python functions for data download and processing
- `problems.ipynb` — Main notebook for analysis
- `data/` — Contains downloaded CSV stock data
- `plots/` — Contains generated plots
- `requirements.txt` — Python dependencies

## Notes
- The data folder will be created automatically if missing.
- Data is downloaded using the [yfinance](https://github.com/ranaroussi/yfinance) package.
