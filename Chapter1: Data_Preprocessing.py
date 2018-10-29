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

#import the data
df = pd.read_csv('Data.csv')

#take care of the missing data
x = df.iloc[:, :-1].values
y = df.iloc[:, -1:].values
imp = SimpleImputer(missing_values=np.nan, strategy='mean')
imp = imp.fit(x[:, 1:3])
x[:, 1:3] = imp.transform(x[:, 1:3])


#encoding categorical data
labelencoder_x = LabelEncoder()
x[:, 0] = labelencoder_x.fit_transform(x[:, 0])

ohe = OneHotEncoder(categorical_features=[0])
x = ohe.fit_transform(x).toarray()
print(type(x))

labelencoder_y = LabelEncoder()
y = labelencoder_y.fit_transform(y)
print(y)

#splitting the dataset into training set and test set
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=0)

#feature scaling
sc_x = StandardScaler()
x_train = sc_x.fit_transform(x_train)
x_test = sc_x.transform(x_test)



#data preprocessing template




















