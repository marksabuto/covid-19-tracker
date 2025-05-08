# COVID-19 Global Data Tracker

## Project Overview
This project analyzes global COVID-19 trends using data from [Our World in Data](https://ourworldindata.org/covid-cases). It includes:
- Data cleaning and preprocessing
- Exploratory Data Analysis (EDA)
- Visualization of cases, deaths, and vaccinations
- Key insights and reporting

## Output Files Handling
For Jupyter notebook projects, we recommend this approach for output files:

1. **Dynamic Generation**:
   - All plots and outputs are generated when you run the notebook
   - Output directory (`/outputs`) is excluded from Git (via `.gitignore`)
   - To get the outputs:
     ```bash
     jupyter notebook notebooks/covid_analysis.ipynb
     ```
     Then run all cells

2. **Example Outputs**:
   - Selected sample plots are available in `/docs/examples/`
   - These demonstrate expected outputs without committing all generated files

## How to Run
1. Clone this repository:
   ```bash
   git clone https://github.com/marksabuto/covid-19-tracker.git
   cd covid-19-tracker
