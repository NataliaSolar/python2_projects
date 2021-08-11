import matplotlib.pyplot as pyplot
import pandas as pd
import numpy as np
import statsmodels.api as sm
 

data = pd.read_csv("C:\\Users\\Roman\\Desktop\\data analysis\\kc_house_data.csv")

#1

if(False):
    zipdata = data[(data['zipcode'] == 98178) | (data['zipcode'] == 98125) | (data['zipcode'] == 98028)]

    #pyplot.plot(zipdata["zipcode"], zipdata["price"], "bo")
    zipdata.boxplot(column = "price", by = "zipcode")
    pyplot.xlabel("Zip Code")
    pyplot.ylabel("Price")
    pyplot.show()

#2

if(False):
    #pyplot.plot(data["sqft_living"], data["price"], "bo")
    model = np.polyfit(data["sqft_living"], data["price"], 1)
    predict = np.poly1d(model)
    x_lin_reg = range(min(data["sqft_living"]), max(data["sqft_living"]))
    y_lin_reg = predict(x_lin_reg)

    #pyplot.plot(data["sqft_living"], data["price"], "bo", x_lin_reg, y_lin_reg, "r")
    pyplot.plot(data["sqft_living"], data["price"], "bo")

    pyplot.xlabel("Sqft")
    pyplot.ylabel("Price")
    pyplot.show()

    
#3

if(False):
    data.boxplot(column = "price", by = "bedrooms")
    pyplot.xlabel("bedrooms")
    pyplot.ylabel("Price")
    pyplot.show()


#4
    
if(True):
    #pyplot.plot(data["sqft_living"], data["price"], "bo")
    model = np.polyfit(data["sqft_living"], data["price"], 1)
    predict = np.poly1d(model)
    x_lin_reg = range(min(data["sqft_living"]), max(data["sqft_living"]))
    y_lin_reg = predict(x_lin_reg)

    pyplot.plot(data["sqft_living"], data["price"], "bo")
    pyplot.plot(data["sqft_living"], data["price"], "bo", x_lin_reg, y_lin_reg, "r")

    pyplot.xlabel("Sqft")
    pyplot.ylabel("Price")
    pyplot.show()