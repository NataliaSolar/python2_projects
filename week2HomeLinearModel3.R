data = read.csv("C:\\Users\\Roman\\Desktop\\data analysis\\sales6.csv")
model2 = lm(sales ~ research + marketing + morale, data)
summary(model2)
#keep intercept and morale

model = lm(sales ~ morale, data)
summary(model)
plot(model$residuals)


#Read the data\\sales5.csv file
data = read.csv("data\\sales5.csv")


#Create a model to predict sales from research, marketing, and morale and summarize it
model= lm(sales ~ research + marketing + morale, data)
summary(model)


#Study the residuals to see if any of the variables should be transformed

#Transform the variables until the residuals plot look like a straight line
model= lm(sales ~ I(marketing*marketing) -1, data)

#Summarize the model
summary(model)
