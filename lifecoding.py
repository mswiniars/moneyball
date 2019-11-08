# 1. Read the data
# 2. Extract the most important variables, calculate RD, calculate in, out playoffs
# 3. Plot the variance between RS and Win
# 4. See the correlation between variables
# 5. Linear Regression RD, RS, RA
# 6. Fit the data
# 7. Predict
# 8. Compare the results

import pandas as pd

data = pd.read_csv("baseball.csv")
pd.options.display.max_columns = data.shape[1] + 1
pd.options.display.width = 900
# print(data.head())

data = data[data['Year'] < 2002]
data['RD'] = data['RS'] - data['RA']
in_playoffs = data[data['Playoffs'] == 1]
out_playoffs = data[data['Playoffs'] == 0]

from utils import plot_scatters, plot_histograms
# plot_scatters(in_playoffs, out_playoffs, label='RS')
# plot_scatters(in_playoffs, out_playoffs, label ='RD')
# plot_histograms(data)
# from matplotlib import pyplot as plt
# plt.show()
rd_to_wins = data[['RD', 'W']].corr()

dePodesta = data[['OBP', 'SLG', 'BA', 'RS']].corr()
from sklearn.linear_model import LinearRegression

modelRS = LinearRegression()
modelRS.fit(data[['OBP', 'SLG']].values, data['RS'].values)

print(f"bias RS: {modelRS.intercept_}")
print(f"Coefficients: {modelRS.coef_}")

RA_data = data.dropna()
modelRA = LinearRegression()
modelRA.fit(RA_data[['OOBP', 'OSLG']].values, RA_data['RA'].values)

modelWins = LinearRegression()
modelWins.fit(data[['RD']].values, data[['W']].values)

RS_predicted = modelRS.predict([[0.339, 0.430]])
print(RS_predicted)

RA_predcited = modelRA.predict([[0.307, 0.373]])
print(RA_predcited)

RD_predicted = RS_predicted - RA_predcited
wins_predicted = modelWins.predict([RD_predicted])
print(wins_predicted)



