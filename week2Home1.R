#read the data\\sales2.csv
data = read.csv("data\\sales2.csv")


#Create a linear model of sales as a function of research
model = lm(sales ~  research, data)


#Summarize the model
summary(model)


#Print the p-value for the (Intercept) rounded to 2 decimal points
0
#That is 1.234 rounds to 1.23, and 1.001 rounds to 1


#You can do this manually by writing the number directly or accessing the coefficients from the model



#Print the p-value for the (Research) rounded to 2 decimal points
0


#Print the r-squared for the model as a decimal rounded to 2 decimal points
0.95


#Run a Shapiro-Wilks Test of the model residuals
shapiro.test(model$residuals)