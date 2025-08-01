# -*- coding: utf-8 -*-
"""carpriceprediction

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1AaeTKODqKDDmvd2L6jMWtb42hiYwdc2-
"""



"""imprting the dependenties\"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import sklearn
from sklearn.linear_model import LinearRegression, Lasso
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.model_selection import train_test_split

"""deta collection and processing"""

#loading the data from csv file to pandas data frame
car_dataset = pd.read_csv('/content/car data.csv')

# from google.colab import drive
# drive.mount('/content/car data.csv') # This line is commented out as it's incorrect.

#inspecting the first 5 rows of the dataframe
car_dataset.head()

#cheaking number of datapoints
car_dataset.shape

#getting some information from the data set
car_dataset.info()

#cheaking perticular missing values
car_dataset.isnull().sum()

#cheak the number of catogorical data
print(car_dataset.Fuel_Type.value_counts())
print(car_dataset.Seller_Type.value_counts())
print(car_dataset.Transmission.value_counts())

#converting words into numbers encording the catogoricsl data
car_dataset.replace({'Fuel_Type':{'Petrol':0,'Diesel':1,'CNG':2}},inplace=True)
#converting words into numbers encording the catogoricsl data
car_dataset.replace({'Seller_Type':{'Dealer':0,'Individual':1}},inplace=True)
#converting words into numbers encording the catogoricsl data
car_dataset.replace({'Transmission':{'Manual':0,'Automatic':1}},inplace=True)

car_dataset.head()

"""splitting data into traning data to test data"""

x=car_dataset.drop(['Car_Name','Selling_Price'],axis=1)
y=car_dataset['Selling_Price']

print(x)

print(y)

"""splittingdata  traning and test data

"""

x_traning,x_test,y_traning,y_test=train_test_split(x,y,test_size=0.1,random_state=2)

"""linear regression

"""

#loading the linear regression model
lin_reg_model=LinearRegression()

lin_reg_model.fit(x_traning,y_traning)

"""model Evaluation"""

#prediction on traninng data
traning_data_prediction=lin_reg_model.predict(x_traning)

#compare value with actual value
r2_error_score=r2_score(y_traning,traning_data_prediction)
print("r squared error:",r2_error_score)

"""visualize the actual price and predicted price"""

plt.scatter(y_traning,traning_data_prediction)
plt.xlabel("actual price")
plt.ylabel("predicted price")
plt.title("actual price vs predicted price")
plt.show()
#v

"""predictin on on traning data"""

test_data_prediction=lin_reg_model.predict(x_test)

#r squared error
error_score=r2_score(y_test,test_data_prediction)
print("r squared error:",error_score)

plt.scatter(y_test,test_data_prediction)
plt.xlabel("actual price")
plt.ylabel("predicted price")
plt.title("actual price vs predicted price")
plt.show()

"""lasso regression"""

lass_reg_model=Lasso()

lass_reg_model.fit(x_traning,y_traning)

#prediction on traninng data
traning_data_prediction=lass_reg_model.predict(x_traning)

#compare value with actual value
r2_error_score=r2_score(y_traning,traning_data_prediction)
print("r squared error:",r2_error_score)

"""visualize the actual price and predicted price"""

plt.scatter(y_traning,traning_data_prediction)
plt.xlabel("actual price")
plt.ylabel("predicted price")
plt.title("actual price vs predicted price")
plt.show()
#v

"""predictin on on traning data"""

test_data_prediction=lass_reg_model.predict(x_test)

#r squared error
error_score=r2_score(y_test,test_data_prediction)
print("r squared error:",error_score)

plt.scatter(y_test,test_data_prediction)
plt.xlabel("actual price")
plt.ylabel("predicted price")
plt.title("actual price vs predicted price")
plt.show()