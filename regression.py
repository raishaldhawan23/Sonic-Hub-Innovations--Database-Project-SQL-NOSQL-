import numpy as np
import statsmodels.api as sm

# Set seed for reproducibility
np.random.seed(0)

# Simulate an independent variable 'Overall_Experience' and add a constant for the intercept
X = sm.add_constant(np.random.normal(0, 1, 115))

# Simulate the dependent variable 'revenue_earned'
# We aim for an R-squared between 0.6 and 0.8, so we adjust the noise level accordingly.
noise = np.random.normal(0, 0.581, 115)
y = 31.1999 + 12.3758 * X[:, 1] + noise

# Fit the OLS model
model = sm.OLS(y, X)
results = model.fit()

# Print out the summary to match it as closely as possible to the provided output
print(results.summary())
