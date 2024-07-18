# Pitt-Post-Doc-Mobility-Analysis

# Researchers Success Impact Analysis based on Different Metrics

Brief description of your project.

## Table of Contents
1. [Missing Data Analysis](#1-missing-data-analysis)
2. [Frequency Analysis](#2-frequency-analysis)
3. [Data Preparation and Exploration](#3-data-preparation-and-exploration)
4. [Linear Regression Models](#4-linear-regression-models)
5. [Imputation Strategies](#5-imputation-strategies)
6. [Sensitivity Analysis](#6-sensitivity-analysis)
7. [GitHub Repository Organization](#7-github-repository-organization)

## 1. Missing Data Analysis - Descriptive Analysis to Summarize the Data

- **Code Title:** `Descriptive_Statistics_for_Continuous_Variables.py` for Table 1
- **Functionality:**
  - Perform a descriptive analysis of continuous variables.
  - Calculate missing data percentages.
  - Explore missing data patterns across variables.
  - Visualize missing data.

- **Libraries Used:** pandas, scipy

- **Code Title:** `Descriptive_Statistics_for_Categorical_Variables.py` for Table 1
- **Functionality:**
  - Perform a descriptive analysis of categorical variables.
  - Calculate missing data percentages.
  - Explore missing data patterns across variables.
  - Visualize missing data.

- **Libraries Used:** pandas, scipy, numpy

## 2. Frequency Analysis

- **Code Title:** `Descriptive_Statistics_for_Categorical_Variables.py` for Table 1
- **Functionality:**
  - Generate frequency tables for categorical variables.
  - Include percentages and cumulative frequencies.
  - Handle missing values in frequency tables.
  - Save results to Excel.

- **Libraries Used:** pandas, scipy, numpy

## 3. Data Preparation and Exploration

- **Code Title:** `Linear_Regression_Model_CIM.py` for CIM 
- **Libraries Used:** pandas, numpy, statsmodels, sklearn, matplotlib

- **Code Title:** `Logistic_Regression_Model_CIM.py` for CIM
- **Libraries Used:** statsmodels, pandas, numpy, sklearn, scipy

- **Functionality:**
  - Load and merge datasets.
  - Handle categorical variables.
  - Filter data based on specific criteria.
  - Conduct exploratory data analysis (EDA).
  - Identify missing data patterns.

## 4. Linear Regression Models

- **Code Title:** `Linear_Regression_Model.py` for PITT_EXIT
- **Functionality:**
  - Fit linear regression models for multiple outcomes.
  - Handle categorical variables using label encoding.
  - Evaluate model coefficients, confidence intervals, and p-values.
  - Save results to Excel.

- **Libraries Used:** pandas, numpy, statsmodels, sklearn, matplotlib

- **Code Title:** `Logistic_Regression.py` for PITT_EXIT
- **Functionality:**
  - Fit logistic regression models for binary outcomes.
  - Handle categorical variables using label encoding.
  - Evaluate model coefficients, confidence intervals, and p-values.
  - Save results to Excel.

- **Libraries Used:** pandas, numpy, statsmodels, sklearn, matplotlib

## 5. Imputation Strategies

- **Code Title:** `Linear_Regression_Model.py` for PITT_EXIT
- **Functionality:**
  - Implement imputation strategies for missing values.
  - Use column means for simple imputation.
  - Apply multiple imputation for more complex missing data patterns.
  - Save imputed datasets.

- **Libraries Used:** pandas, numpy, statsmodels, sklearn, matplotlib

## 6. Sensitivity Analysis

- **Code Title:** `Sensitivity_Analysis.py` for linear regression for PITT_EXIT
- **Functionality:**
  - Conduct sensitivity analysis on imputed data.
  - Assess robustness of results under different missing data assumptions.
  - Compare results from multiple imputation and sensitivity analysis.

- **Libraries Used:** pandas, numpy, statsmodels, sklearn, matplotlib

## 7. GitHub Repository Organization

- **Data-Driven-Postdoctoral-Insights:** `README.md`
- **Functionality: Description of the project**

## 8. Functionality:

Descriptive Analysis Code:
File: `Descriptive_Statistics_for_Continuous_Variables.py`

- **Description:**
  - Calculates descriptive statistics and frequencies.
  - Generates a summary report with missing percentages, means, medians, and more.

- **Instructions:**
  - Ensure you have the dataset in the specified format.
  - Run the script to obtain descriptive statistics.
  - Review the generated summary report in 'Result_Data_Summary.xlsx'.

Frequency Analysis Code:
File: `Descriptive_Statistics_for_Categorical_Variables.py`

- **Description:**
  - Performs frequency analysis on categorical variables.
  - Produces frequency tables for different groups of columns.

- **Instructions:**
  - Load the dataset required for frequency analysis.
  - Run the script to generate frequency tables.
  - Explore the results in 'Result_Frequency_tables.xlsx'.

Data Preprocessing and Linear Regression Models:
Files: `Linear_Regression_Model_CIM.py`, `Logistic_Regression_Model_CIM.py`, `Linear_Regression_Model.py`, `Logistic_Regression.py`

- **Description:**
  - Handles missing data through imputation strategies.
  - Applies label encoding to categorical variables.
  - Executes linear regression and logistic regression models with various covariates.

- **Instructions:**
  - Load the merged dataset for postdoc data.
  - Run the script to preprocess and model the data.
  - Explore the results in 'Main_Results.xlsx'.

Sensitivity Analysis:
File: `Sensitivity_Analysis.py`

- **Description:**
  - Conducts sensitivity analysis on imputed data.
  - Assesses the robustness of results under different missing data assumptions.
  - Compares results from multiple imputation and sensitivity analysis.

- **Instructions:**
  - Load the imputed dataset.
  - Run the script to conduct the sensitivity analysis.
  - Review the results in 'Sensitivity_Results.xlsx'.

### How to Run:

1. **Descriptive Analysis for Continuous Variables:**
    ```bash
    python Descriptive_Statistics_for_Continuous_Variables.py
    ```

2. **Descriptive Analysis for Categorical Variables:**
    ```bash
    python Descriptive_Statistics_for_Categorical_Variables.py
    ```

3. **Linear Regression Model for CIM:**
    ```bash
    python Linear_Regression_Model_CIM.py
    ```

4. **Logistic Regression Model for CIM:**
    ```bash
    python Logistic_Regression_Model_CIM.py
    ```

5. **Linear Regression Model for PITT_EXIT:**
    ```bash
    python Linear_Regression_Model.py
    ```

6. **Logistic Regression Model for PITT_EXIT:**
    ```bash
    python Logistic_Regression.py
    ```

7. **Sensitivity Analysis:**
    ```bash
    python Sensitivity_Analysis.py
    ```

Feel free to clone the repository and explore each code file for detailed information.

## License

This project is licensed under a custom license. All rights are reserved.

Permission to use, copy, modify, and distribute this software and its documentation for any purpose must be obtained by contacting the University of Pittsburgh - Office of Academic Career Development, Health Sciences.

For permission requests, please contact:

University of Pittsburgh - Office of Academic Career Development, Health Sciences  
Email: [your_contact_email@pitt.edu]

See the [LICENSE](LICENSE) file for details.

