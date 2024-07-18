#%%
import pandas as pd
import numpy as np
import statsmodels.api as sm
from sklearn.impute import SimpleImputer
import matplotlib.pyplot as plt
from statsmodels.graphics.gofplots import qqplot


# Load your merged dataset
data = pd.read_excel('Full_DATA_NEW.xlsx')

# Filter the data where analytic_set = 1
data = data[data['analytic_set'] == 1]

# Label encode categorical variables
data['Gender'] = data['Gender'].astype('category').cat.codes
data['URM'] = data['URM'].astype('category').cat.codes
data['FIS_Nationality'] = data['FIS_Nationality'].astype('category').cat.codes

# Impute missing values for the entire DataFrame
imputer = SimpleImputer(strategy='most_frequent')
data[:] = imputer.fit_transform(data)

# Ensure all data is numeric (optional based on your dataset specifics)
data = data.apply(pd.to_numeric, errors='coerce')

# Impute any remaining missing values after conversion
data.fillna(data.mean(), inplace=True)


# Create a new variable named 'CIM' based on Pitt_Exit
data['CIM'] = np.where(data['Pitt_Exit'] == 0, 1, 0)# Currently set for CIM=1; those who left
# data['CIM'] = np.where(data['Pitt_Exit'] == 1, 1, 0)  # Uncomment to switch to CIM=0; those who stayed


model_results = []
outcome_variables = [
    '# of Pubs from end of postdoc to 3-year check-in',
    'H-Index ever up to 3 year check-in',
    'Cat. Normal Citation Impact ever up to 3-year check-in',
    '# of 1st Author Pubs from end of postdoc to 3-year check-in',
    '% of 1st Author Pubs from end of postdoc to 3-year check-in',
    '# of last Author Pubs from end of postdoc to 3-year check-in',
    '% of last author pubs from end of postdoc to 3-year check-in',
    '# of corresponding author pubs from end of postdoc to 3-year check-in',
    '% of corresponding author pubs from end of postdoc to 3-year check-in',
    'Mean Relative Citation Ratio ever up to 3-year check-in',
    'Weighted Relative Citation Ratio ever up to 3-year check-in',
    '# of Pubs without Postdoc Mentor from end of postdoc to 3-year check-in',
    'Network Size ever up to 3-year check-in'
]
# Define the constant baseline covariates
baseline_covariates = [
    '# of Pubs ever to end of postdoc',
    'H-Index ever to end of postdoc',
    'Cat. Normal Citation Impact ever to End of Postdoc',
    '# of 1st Author Pubs ever to end of postdoc',
    '% of 1st Author Pubs ever to end of postdoc',
    '# of last Author Pubs ever to end of postdoc',
    '% of last author pubs ever to end of postdoc',
    '# of corresponding author pubs ever to end of postdoc',
    '% of corresponding author pubs ever to end of postdoc',
    'Mean Relative Citation Ratio ever to end of postdoc',
    'Weighted Relative Citation Ratio ever to end of postdoc',
    '# of Pubs without Postdoc Mentor during the postdoc',
    'Network Size ever to end of postdoc',
    'CIM'  # Include CIM instead of Pitt_Exit
]

baseline_covariate_mapping = {
    '# of Pubs from end of postdoc to 3-year check-in': '# of Pubs ever to end of postdoc',
    'H-Index ever up to 3 year check-in': 'H-Index ever to end of postdoc',
    'Cat. Normal Citation Impact ever up to 3-year check-in': 'Cat. Normal Citation Impact ever to End of Postdoc',
    '# of 1st Author Pubs from end of postdoc to 3-year check-in': '# of 1st Author Pubs ever to end of postdoc',
    '% of 1st Author Pubs from end of postdoc to 3-year check-in': '% of 1st Author Pubs ever to end of postdoc',
    '# of last Author Pubs from end of postdoc to 3-year check-in': '# of last Author Pubs ever to end of postdoc',
    '% of last author pubs from end of postdoc to 3-year check-in': '% of last author pubs ever to end of postdoc',
    '# of corresponding author pubs from end of postdoc to 3-year check-in': '# of corresponding author pubs ever to end of postdoc',
    '% of corresponding author pubs from end of postdoc to 3-year check-in': '% of corresponding author pubs ever to end of postdoc',
    'Mean Relative Citation Ratio ever up to 3-year check-in': 'Mean Relative Citation Ratio ever to end of postdoc',
    'Weighted Relative Citation Ratio ever up to 3-year check-in': 'Weighted Relative Citation Ratio ever to end of postdoc',
    '# of Pubs without Postdoc Mentor from end of postdoc to 3-year check-in': '# of Pubs without Postdoc Mentor during the postdoc',
    'Network Size ever up to 3-year check-in': 'Network Size ever to end of postdoc'
}



# Create a list of models and their respective covariates
models = [
    {
        'name': 'Model 1',
        'additional_covariates': []
    },
    {
        'name': 'Model 2',
        'additional_covariates': ['Gender', 'URM']
    },
    {
        'name': 'Model 3',
        'additional_covariates': ['Gender', 'URM', 'FIS_Nationality', 'Months_Worked_in_appointment']
    }
]


def extract_model_summary(initial_model, covariate_name):
    coef = initial_model.params[covariate_name]
    ci_lower, ci_upper = initial_model.conf_int().loc[covariate_name]
    p_value = initial_model.pvalues[covariate_name]
    summary = {
        'Variable': covariate_name,  # This will hold the name of the covariate
        'Coefficient': coef,
        '95% CI Lower': ci_lower,
        '95% CI Upper': ci_upper,
        'P-value': p_value
    }
    return summary


# Diagnostic Plots to Identify Outliers
# Def function definition (already provided previously)

from scipy import stats

# Adjusted workflow to include fitting models with specified covariates and their respective baseline covariate
with pd.ExcelWriter('CIM_RESULT.xlsx') as writer:
    for model_info in models:
        model_name = model_info['name']
        additional_covariates = model_info['additional_covariates']
        all_model_results = []

        for outcome_var in outcome_variables:
            baseline_covariate = baseline_covariate_mapping[outcome_var]
            covariates = ['CIM'] + [baseline_covariate] + additional_covariates  # Update covariate list to use CIM

            X = data[covariates]
            y = data[outcome_var]

            # Standardize X and y
            X_standardized = pd.DataFrame(stats.zscore(X), columns=X.columns)
            y_standardized = pd.Series(stats.zscore(y), name=y.name)

            # Add a constant to the standardized predictors
            X_with_const = sm.add_constant(X_standardized)

            # Fit the initial model with standardized predictors and outcome
            initial_model = sm.OLS(y_standardized, X_with_const).fit()
            print(f"Initial Model Summary for {model_name} - {outcome_var}:")
            print(initial_model.summary())

            # To call Diagnostic Plots Function (commented out, uncomment if needed)
            # diagnostic_plots(initial_model, X_with_const, y_standardized, model_name, outcome_var)

            # Extract model summaries
            for covariate_name in X_with_const.columns:
                if covariate_name == 'const':
                    continue
                summary = extract_model_summary(initial_model, covariate_name)
                summary['Outcome Variable'] = outcome_var
                all_model_results.append(summary)

            # Write to Excel
            model_results_df = pd.DataFrame(all_model_results)
            model_results_df.to_excel(writer, sheet_name=model_name, index=False)
