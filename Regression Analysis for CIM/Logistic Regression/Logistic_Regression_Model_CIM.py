#%%

import statsmodels.api as sm
import pandas as pd
import numpy as np
from sklearn.impute import SimpleImputer
from scipy import stats

# Load your dataset
data = pd.read_excel('datasetname.xlsx')

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

# Create a new variable 'CIM' based on Pitt_Exit
data['CIM'] = np.where(data['Pitt_Exit'] == 0, 1, 0)# Currently set for CIM=1; those who left
# data['CIM'] = np.where(data['Pitt_Exit'] == 1, 1, 0)  # Uncomment to switch to CIM=0; those who stayed


# Grant outcome variables
grant_outcome_variables = [
    '# grant_baseline',
    'grant_amount_baseline',
    '# grant_3yr_checkin',
    'grant_amount_3yr_checkin'
]

# Define models and their covariates
models = {
    'Model 1': ['CIM', 'grant_amount_baseline'],
    'Model 2': ['CIM', 'grant_amount_baseline', 'Gender', 'URM'],
    'Model 3': ['CIM', 'grant_amount_baseline', 'Gender', 'URM', 'FIS_Nationality', 'Months_Worked_in_appointment']
}

# Function to extract model summary
def extract_model_summary(logit_model, covariate_name):
    coef = logit_model.params[covariate_name]
    ci_lower, ci_upper = logit_model.conf_int().loc[covariate_name]
    p_value = logit_model.pvalues[covariate_name]
    odds_ratio = np.exp(coef)
    summary = {
        'Variable': covariate_name,
        'Coefficient': coef,
        'Odds Ratio': odds_ratio,
        '95% CI Lower': np.exp(ci_lower),
        '95% CI Upper': np.exp(ci_upper),
        'P-value': p_value
    }
    return summary

# Prepare to write results to Excel
with pd.ExcelWriter('CIM_Log_Regression_Grant_Outcomes_Results.xlsx') as writer:
    for model_name, covariates in models.items():
        X = data[covariates]
        X = sm.add_constant(X)  # Add constant to the model
        y = data['grant_amount_3yr_checkin'].astype(int)
        
        try:
            logit_model = sm.Logit(y, X).fit()
            model_results = [extract_model_summary(logit_model, var) for var in X.columns if var != 'const']
            
            model_results_df = pd.DataFrame(model_results)
            model_results_df.to_excel(writer, sheet_name=model_name)
            
            print(f"Model Summary for {model_name}:")
            print(logit_model.summary())
        except Exception as e:
            print(f"Failed to fit model {model_name}. Error: {e}")
