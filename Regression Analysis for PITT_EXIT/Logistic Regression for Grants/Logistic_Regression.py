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
# print(np.asarray(data))


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


# Recheck data types
print(data.dtypes)



grant_outcome_variables = [
    '# grant_baseline',
    'grant_amount_baseline',
    '# grant_3yr_checkin',
    'grant_amount_3yr_checkin'
]

# Define the outcome variable
outcome_variable = 'grant_amount_3yr_checkin'

# Define the primary predictor and the additional variables for each model
models = {
    'Model 1': ['Pitt_Exit', 'grant_amount_baseline'],
    'Model 2': ['Pitt_Exit', 'grant_amount_baseline', 'Gender', 'URM'],
    'Model 3': ['Pitt_Exit', 'grant_amount_baseline', 'Gender', 'URM', 'FIS_Nationality', 'Months_Worked_in_appointment'] 
}


# Function to extract model summary details for a covariate
def extract_model_summary(refined_model, covariate_name):
    coef = refined_model.params[covariate_name]
    odds_ratio = np.exp(coef)
    ci_lower, ci_upper = np.exp(refined_model.conf_int().loc[covariate_name])
    p_value = refined_model.pvalues[covariate_name]
    summary = {
        'Variable': covariate_name,
        'Coefficient': coef,
        'Odds Ratio': odds_ratio,
        '95% CI Lower': ci_lower,
        '95% CI Upper': ci_upper,
        'P-value': p_value
    }
    return summary

# Run the analysis for each model
with pd.ExcelWriter('LR_Grant_Outcomes_Refined.xlsx') as writer:
    for model_name, covariates in models.items():
        X = data[covariates]  # Use data as is for logistic regression predictors
        X = sm.add_constant(X)  # Add constant to the model
        y = data[outcome_variable].astype(int)  
        
        try:
            logit_model = sm.Logit(y, X).fit()
            model_results = []
            
            for covariate_name in X.columns:
                if covariate_name != 'const':  # Optionally include if you want to see the intercept
                    summary = extract_model_summary(logit_model, covariate_name)
                    summary['Outcome Variable'] = outcome_variable
                    model_results.append(summary)

            model_results_df = pd.DataFrame(model_results)
            model_results_df.to_excel(writer, sheet_name=model_name)
            
            print(f"Model Summary for {model_name}:")
            print(logit_model.summary())
        except Exception as e:
            print(f"Failed to fit model {model_name}. Error: {e}")