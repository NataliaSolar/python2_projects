import matplotlib.pyplot as pyplot
import pandas as pd
import numpy as np
import statsmodels.api as sm
 
#pyplot.plot(y)
#pyplot.ylabel("y")
#pyplot.show()
#x = [1, 2, 3, 4, 5]
#y = [1, 2, 3, 4, 5]
 
#a = [1, 4, 9, 16, 25]
 
#pyplot.plot(x, y, 'rs', x, a, 'b^')
#pyplot.ylabel("y")
#pyplot.xlabel("x")
#pyplot.axis([0, 6, 0, 26])
#pyplot.show()

data = pd.read_csv("C:\\Users\\Roman\\Desktop\\data analysis\\weight-height.csv")
model = np.polyfit(data["Height"], data["Weight"], 1)
predict = np.poly1d(model)

x_lin_reg = range(54, 80)
y_lin_reg = predict(x_lin_reg)

pyplot.plot(data["Height"], data["Weight"], "bo", x_lin_reg, y_lin_reg, "r")

pyplot.xlabel("Height")
pyplot.ylabel("Weight")
pyplot.show()
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


pyplot.hist(x)
pyplot.show()

