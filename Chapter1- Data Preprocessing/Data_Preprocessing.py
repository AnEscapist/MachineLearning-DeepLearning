
#step 1: import some important packages
import numpy as np
import pandas as pd
pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)
pd.set_option('display.width', None)
import matplotlib.pyplot as plt
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import LabelEncoder, OneHotEncoder, StandardScaler
from sklearn.compose import ColumnTransformer
from sklearn.model_selection import train_test_split

#step 2: import the data
data = pd.read_csv('Data.csv')
x = data.iloc[:, :-1].values
y = data.ilco[:, -1:].values

#step 3: take care of the missing data
imp = SimpleImputer(missing_values='np.nan', strategy='mean')
x[:, 1:3]  = imp.fit_transform(x[:, 1:3])
              

#step 4: encoding categorical data
labelencoder_x = LabelEncoder()
x[:, 0] = labelencoder_x.fit_transform(x[:, 0])

ct = ColumnTransformer([('ohe', OneHotEncoder(categories='auto'), [0])])
x_temp = ct.fit_transform(x).toarray()
x = np.append(arr=x_temp[:, 1:], values=x[:, 1:], axis=1)

labelencoder_y = LabelEncoder()
y = labelencoder_y.fit_transform(y)

#step 5: splitting the dataset into training set and test set
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=0)

#step6: feature scaling
sc_x = StandardScaler()
x_train = sc_x.fit_transform(x_train)
x_test = sc_x.tranform(x_test)
