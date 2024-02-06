# A_Econometrics_Project_ZS24

Welcome to our repository for the **Pokémon Cards x Financial Markets Investments** project, part of the Advanced Econometrics course at IES, Charles University. This project is the collaborative effort of Jan Hrušák and Jakub Michalski, aiming to blend the intriguing world of Pokémon card trading with the rigorous analysis of financial markets.

## Scraping and Data Retrieval

In the `scraping/fctions` directory, you'll find the tools needed for the initial phase of our expedition: gathering data. The main instrument of our data collection, a Python Jupyter Notebook titled `A_scraper.ipynb`, is dedicated to the meticulous task of scraping Pokémon card prices from the web.

A stable internet connection is your ally in this endeavor. Upon successfully running the notebook, the data collected will be stored in the `sets` directory, paving the way for the next phase: `A2_data_processing.ipynb`. This notebook processes the gathered data into two primary datasets:
- `card_prices_data.xlsx` containing prices across various card grades.
- `card_data_grade.xlsx` focusing on the population report for these grades, though this dataset takes a backseat in our analysis.

**For those inclined to skip the data collection saga and dive straight into the treasure trove of data, the aforementioned `.xlsx` files are ready for download directly from the repository.**

A word of caution: launching these scripts may overwrite existing data unless you rename the destination folders or files via a simple parameter adjustment in the functions.

The **stocks data** journey begins with `Data_stocks.py`, conveniently located at the repository's entrance. Executing this script will yield a dataset named akin to `^GSPC_output.csv`.

## Data Processing

With the data in hand, or if you're starting with pre-existing datasets, the main repository page is your next destination. The quest continues with `Data_processin_R.ipynb`, designed to generate datasets enriched with the most observations per year (defaulting to 200).

Following this, `Data_processing_2.ipynb` (this time, a Python notebook) merges the datasets of stocks/S&P500 prices with Pokémon card prices, outputting a dataset of monthly frequency, albeit sans lagged variables.

To incorporate these crucial lagged variables into your analysis, `Data_processing_2_lagged.ipynb` must be run **AFTER** the successful completion of `Data_processing_2.ipynb`, culminating in the datasets destined for final analysis.

**Tip:** For those wishing to bypass the groundwork and access the final datasets directly, they are available for download in `.csv` format within the `lagged_merged_datasets_final` directory.

## Data Analysis

To replicate our analysis or to simply peruse through our code, plots, and findings, the following R-kernel Jupyter Notebooks are at your service:

- `ANALYSIS1_FINAL.ipynb`
- `ANALYSIS2_FINAL.ipynb`
- `ANALYSIS3_FINAL.ipynb`
- `ANALYSIS4_FINAL.ipynb`
- `ANALYSIS8_FINAL.ipynb`
- `ANALYSIS9_FINAL.ipynb`
- `ANALYSIS10_FINAL.ipynb`

We invite you to join us on this scholarly journey, where the worlds of Pokémon and finance collide, promising insights that are as enlightening as they are engaging.

