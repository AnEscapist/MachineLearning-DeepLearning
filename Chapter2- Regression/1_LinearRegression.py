import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import statsmodels.formula.api as smf


data = pd.read_csv('Salary_Data.csv')

x = data.iloc[:, :-1].values
y = data.iloc[:, -1:].values

reg_ols = smf.OLS(y, x).fit()
print(reg_ols.summary())


x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.3, random_state=0)
#fitting simple linear regression to the training set

reg = LinearRegression()
reg.fit(x_train, y_train)

#predicting test set results

y_pred = reg.predict(x_test)
print(y_pred - y_test)

#visualizing the training set results
#sns.scatterplot(x='YearsExperience', y='Salary', data=data)
#plt.show()
plt.scatter(x_train, y_train, color='r')
plt.plot(x_train, reg.predict(x_train), color='b')
plt.title('Salary vs Experience (Training set)')
plt.xlabel('Years of Experience')
plt.ylabel('Salary')
plt.show()


#visualizing the test set results

plt.scatter(x_test, y_test, color='r')
plt.plot(x_test, y_pred, color='b')
plt.title('Salary vs Experience (test set)')
plt.xlabel('Years of Experience')
plt.ylabel('Salary')
plt.show()