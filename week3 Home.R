data = read.csv("C:\\Users\\Roman\\Desktop\\data analysis\\sales6.csv")

model= lm(sales ~ research + marketing + morale, data)
summary(model)

model= lm(sales ~ morale, data)
summary(model)

plot(model$residuals)

model= lm(sales ~ log(morale), data)
summary(model)
plot(model$residuals)

#Read the data from the data\\sales6.csv file
data = read.csv("data\\sales6.csv")



#Model sales vs marketing, research and morale
model = lm(sales ~ research + marketing + morale, data)




#Use the model information and residual plots to identify the best model

#Create an summarize the best model
model= lm(sales ~ log(morale), data)
summary(model)

