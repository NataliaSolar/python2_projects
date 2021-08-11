#read the data\\sales2.csv
data = read.csv("data\\sales2.csv")


#Create a linear model of sales as a function of marketing
model = lm(sales ~  marketing, data)


#Summarize the model
summary(model)


#Print the p-value for the (Intercept) rounded to 2 decimal points
0
#You can do this manually by writing the number directly



#Print the p-value for the (marketing) rounded to 2 decimal points
0


#Print the r-squared for the model as a decimal rounded to 2 decimal points
0.97


#Run a Shapiro-Wilks Test of the model residuals
shapiro.test(model$residuals)