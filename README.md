# 🌟 A_Econometrics_Project_ZS24 🌟

Welcome to our repository for the **Pokémon Cards x Financial Markets Investments** project, presented for the Advanced Econometrics course at IES, Charles University. This adventurous journey through data is brought to you by Jan Hrušák and Jakub Michalski. 📊✨

## 🚀 Scraping and Data Retrieval

Inside the `scraping/fctions` directory, you'll find all the necessary magic spells (functions) along with our main wizard's book, the Python Jupyter Notebook `A_scraper.ipynb`, focused on conjuring (web-scraping) Pokémon cards prices from the vast internet. 🌐

Ensure you're connected to the world's mana (a stable internet connection) before running the cells in the Jupyter Notebook. After gathering all data into the `sets` cauldron, proceed with `A2_data_processing.ipynb` to brew two raw `.xlsx` potions:
- `card_prices_data.xlsx` with Pokémon card prices for various grades
- `card_data_grade.xlsx` with a population report, which we'll leave for another adventure (not used in the analysis).

🌟 **Shortcut:** If you wish to skip the spell casting and go straight to the treasure, download both `.xlsx` files directly from the repository.

⚠️ **Caution:** Running the code might replace existing treasures unless you rename your target folders or files. This is usually done with a simple wave of your wand (function parameter/input).

📈 The **stocks data** potion can be prepared by running `Data_stocks.py`, found not in any dungeon but right at the entrance of our repository. Brewing this potion creates a dataset named `^GSPC_output.csv`.

## 🧙‍♂️ Data Processing

After gathering your data treasures, or if you've already got some in your bag, head over to the main site of our repository to continue the quest. Your first task is to find and run `Data_processin_R.ipynb` to generate datasets rich with observations. The incantation (parameter) for observations per year can be altered; the default is 200.

Next, summon `Data_processing_2.ipynb` (crafted in Python, unlike its R sibling) to merge datasets of stocks/S&P500 with the Pokémon cards prices, creating a monthly frequency dataset. However, this potion lacks the power of hindsight (lagged variables)!

For a more powerful concoction, run `Data_processing_2_lagged.ipynb` **FIRST AFTER** successfully brewing `Data_processing_2.ipynb`. This final potion will be used as input for our analysis.

🌟 **Pro Tip:** If you seek the final potions without the alchemy, download them in `.csv` form from the `lagged_merged_datasets_final` treasure chest!

## 📊 Data Analysis

To behold the magic yourself or replicate our enchantments, consult the following grimoires (Jupyter Notebooks with an R kernel):

- `ANALYSIS1_FINAL.ipynb`
- `ANALYSIS2_FINAL.ipynb`
- `ANALYSIS3_FINAL.ipynb`
- `ANALYSIS4_FINAL.ipynb`
- `ANALYSIS8_FINAL.ipynb`
- `ANALYSIS9_FINAL.ipynb`
- `ANALYSIS10_FINAL.ipynb`

Embark on this journey with us, through realms of data and seas of analysis, to uncover insights as brave and beautiful as the quest itself! 🌌✨
