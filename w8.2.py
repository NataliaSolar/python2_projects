import matplotlib.pyplot as pyplot
import pandas as pd
import numpy as np
import statsmodels.api as sm
 

data = pd.read_csv("C:\\Users\\Roman\\Desktop\\data analysis\\kc_house_data.csv")

zipdata = data[(data['zipcode'] == 98178) | (data['zipcode'] == 98125) | (data['zipcode'] == 98028)]

#pyplot.plot(zipdata["zipcode"], zipdata["price"], "bo")
zipdata.boxplot(column = "price", by = "zipcode")
pyplot.xlabel("Zip Code")
pyplot.ylabel("Price")
pyplot.show()


#model = np.polyfit(data["Height"], data["Weight"], 1)
#predict = np.poly1d(model)

#x_lin_reg = range(54, 80)
#y_lin_reg = predict(x_lin_reg)

#pyplot.plot(data["Height"], data["Weight"], "bo", x_lin_reg, y_lin_reg, "r")

#pyplot.xlabel("Height")
#pyplot.ylabel("Weight")
#pyplot.show()
#_________________________________________________
x = data["Height"]
Y = data["Weight"]
gender = data["Gender "]
numeric_gender = gender == "Male"
X = sm.add_constant(x)
 
model = sm.OLS(Y,X).fit()
prediction = model.predict()
pyplot.plot(x, Y, "bo", x, prediction, "r")
pyplot.show()
 
pyplot.scatter(x, Y, c=numeric_gender, alpha=0.3)
pyplot.show()


#pyplot.hist(x)
#pyplot.show()

data.boxplot(column = "Height", by = "Gender ")
pyplot.show()

