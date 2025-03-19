import pandas as pd
import statsmodels.api as sm

# Data preparation
data = {
    'Variable': [
        'Age (<30)', 'Age (31-40)', 'Age (41-50)', 'Age (>50)',
        'High school diploma', "Associate's degree", "Bachelor's degree", 'Post graduate',
        'Married', 'Single', 'Employee', 'Housewife', 'Farmer', 'Pensionen', 'Other',
        'Ferdows', 'Other cities', 'Village',
        '<30 minutes per day', '30-60 minutes per day', '60-180 minutes per day', '>180 minutes per day',
        'Reduction of expenses and transportation issues', 'Saving time', 'Accessibility of electronic services',
        'Prevention of missing the test results', 'Other'
    ],
    'Mail': [37, 32, 8, 5, 22, 17, 34, 9, 64, 18, 39, 27, 1, 2, 13, 57, 24, 1, 16, 32, 25, 9, 47, 61, 50, 28, 0],
    'Website': [17, 13, 8, 3, 13, 13, 11, 4, 30, 11, 12, 16, 2, 1, 10, 22, 16, 3, 41, 0, 0, 0, 20, 31, 17, 12, 0],
    'Both': [26, 11, 5, 3, 9, 10, 20, 6, 40, 5, 23, 13, 0, 0, 9, 35, 9, 1, 25, 13, 3, 4, 34, 39, 23, 18, 1],
    'None': [17, 9, 6, 0, 9, 8, 13, 2, 22, 10, 14, 4, 3, 0, 11, 17, 12, 3, 12, 11, 6, 3, 10, 23, 17, 4, 0]
}

df = pd.DataFrame(data)

# Ensuring all columns are numeric
df[['Mail', 'Website', 'Both', 'None']] = df[['Mail', 'Website', 'Both', 'None']].apply(pd.to_numeric)

# Dummy encoding the categorical variable 'Variable'
df = pd.get_dummies(df, columns=['Variable'], drop_first=True)

# Simplified model with a few key predictors
X = df[['Website', 'Both', 'None']]  # Start with a few predictors
X = sm.add_constant(X)

# Target variable
y = df['Mail']

# Fit the regression model
model = sm.OLS(y, X).fit()

# Print the summary of the regression
print(model.summary())

# Plotting the results
import matplotlib.pyplot as plt

plt.figure(figsize=(10, 6))
plt.scatter(y, model.predict(X))
plt.xlabel('Observed values')
plt.ylabel('Predicted values')
plt.title('Observed vs Predicted values')
plt.show()
plt.grid(True)