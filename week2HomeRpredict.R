#load the data\\sales2.csv file
data = read.csv("data\\sales2.csv")


#Create a model with research, marketing, and morale and summarize it
model= lm(sales ~ research + marketing + morale, data)
summary(model)

#create a model with the relevant variables and summarize it
model = lm(sales ~ research + marketing - 1, data)
summary(model)

#Predict the expected sales for a budget of 200k in research and 200k in marketing
newdata = data.frame(research = 200000, marketing = 200000)
predict(model, newdata)


#Predict the expected sales for a budget of 500k in research and 1 million in marketing
newdata = data.frame(research = 500000, marketing = 1000000)
predict(model, newdata)
