# Pitt-Post-Doc-Mobility-Analysis



# Researchers Success Impact Analysis based on Diffrent Metrics

Brief description of your project.

## Table of Contents
1. [Missing Data Analysis](#1-missing-data-analysis)
2. [Frequency Analysis](#2-frequency-analysis)
3. [Data Preparation and Exploration](#3-data-preparation-and-exploration)
4. [Linear Regression Models](#4-linear-regression-models)
5. [Imputation Strategies](#5-imputation-strategies)
6. [Sensitivity Analysis](#6-sensitivity-analysis)
7. [GitHub Repository Organization](#7-github-repository-organization)




## 1. Missing Data Analysis ssing Descriptive Analysis - to summarize the data

- **Code Title:** `Descriptive_Analysis.py`
- **Functionality:**
  - Perform a descriptive analysis of missing data.
  - Calculate missing data percentages.
  - Explore missing data patterns across variables.
  - Visualize missing data.

## 2. Frequency Analysis

- **Code Title:** `Frequency_Analysis.py`
- **Functionality:**
  - Generate frequency tables for categorical variables.
  - Include percentages and cumulative frequencies.
  - Handle missing values in frequency tables.
  - Save results to Excel.

## 3. Data Preparation and Exploration

- **Code Title:** `Regression_Model.py` 
- **Functionality:**
- Initial Steps Include processing and handeling the data
  - Load and merge datasets.
  - Handle categorical variables.
  - Filter data based on specific criteria.
  - Conduct exploratory data analysis (EDA).
  - Identify missing data patterns.

## 4. Linear Regression Models

- **Code Title:** `Regression_Model.py`
- **Functionality:**
  - Fit linear regression models for multiple outcomes.
  - Handle categorical variables using label encoding.
  - Evaluate model coefficients, confidence intervals, and p-values.
  - Save results to Excel.

## 5. Imputation Strategies

- **Code Title:** `Regression_Model.py`
- **Functionality:**
- Code Includes:
  - Implement imputation strategies for missing values.
  - Use column means for simple imputation.
  - Apply multiple imputation for more complex missing data patterns.
  - Save imputed datasets.

## 6. Sensitivity Analysis

- **Code Title:** `Sensitivity_Analysis.py`
- **Functionality:**
  - Conduct sensitivity analysis on imputed data.
  - Assess robustness of results under different missing data assumptions.
  - Compare results from multiple imputation and sensitivity analysis.

## 7. GitHub Repository Organization

- **Data-Driven-Postdoctoral-Insights:** `README.md`
- **Functionality: Description of the project**

## 8. Functionality:

Descriptive Analysis Code:
File: Descriptive_Analysis.py

- Description:
Calculates descriptive statistics and frequencies.
Generates a summary report with missing percentages, means, medians, and more.

- Instructions:
Ensure you have the dataset in the specified format.
Run the script to obtain descriptive statistics.
Review the generated summary report in 'Result_Data_Summary.xlsx'.

- Frequency Analysis Code:
File: Frequency_Analysis.py

- Description:
Performs frequency analysis on categorical variables.
Produces frequency tables for different groups of columns.

- Instructions:
Load the dataset required for frequency analysis.
Run the script to generate frequency tables.
Explore the results in 'Result_Frequency_tables.xlsx'.
Data Preprocessing and Linear Regression Models:
File: data_preprocessing_and_regression.py

- Description:
Handles missing data through imputation strategies.
Applies label encoding to categorical variables.
Executes linear regression models with various covariates.

- Instructions:
Load the merged dataset for postdoc data.
Run the script to preprocess and model the data.
Explore the results in 'Main_Results.xlsx'.

### How to Run:

1. **Descriptive Analysis:**
    ```bash
    python Descriptive_Analysis.py
    ```

2. **Frequency Analysis:**
    ```bash
    python Frequency_Analysis.py
    ```

3. **Data Preprocessing and Regression:**
    ```bash
    python Regression_Model.py
    ```


Custom License

Copyright (c) 2024 University of Pittsburgh - Office of Academic Career Development, Health Sciences

All rights reserved.

Permission to use, copy, modify, and distribute this software and its documentation for any purpose must be obtained by contacting the University of Pittsburgh - Office of Academic Career Development, Health Sciences.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

For permission requests, please contact:
University of Pittsburgh - Office of Academic Career Development, Health Sciences

