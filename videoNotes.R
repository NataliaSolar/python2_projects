data = read.csv("C:\\Users\\Roman\\Desktop\\data analysis\\sales2.csv")
model1 = lm(sales ~  research, data)
summary(model1)
#intersept = -2.842e+07
#resarch = 6.069e+00
#sales = -2.842e+07 + 6.069e+00*research

#P - value of hte estimate <2e-16 ~0
#p - values of the research <2e-16 ~0

#Multiple R-squared - 0.9451
#Model expains 95% of the behavior of the variable

#residuals measure the distribution of the difference between the model and reality

plot(data$research, data$marketing)

plot(model1, 1)

plot(model1,2)

shapiro.test(model1$residuals)
#result is <0.05, rule it not normal
1.234




#data...

model2 = lm(sales ~ research + marketing + morale, data)
summary(model2)

#intercept  0.143
#research = 0
#marketing 0
# morale 0.124

#keep research and marketing because of high values of p in intercept and morale

model3 = lm(sales ~ research + marketing - 1, data)

summary(model3)
#p values 0
#R- square 0.9953

plot(model3$residuals)
shapiro.test(model3$residuals)



data = read.csv("C:\\Users\\Roman\\Desktop\\data analysis\\sales2.csv")
model= lm(sales ~ research + marketing + morale, data)
summary(model)
model = lm(sales ~ research + marketing - 1, data)
summary(model)
research = 200000
marketing = 200000

newdata = data.frame(research = research, marketing = marketing)
predict(model, newdata)
#expected sales from 100k research, 100k marketing is 371927.9$

newdata = data.frame(research = 500000, marketing = 1000000)
predict(model, newdata)


data = read.csv("C:\\Users\\Roman\\Desktop\\data analysis\\sales3.csv")
model= lm(sales ~ research + marketing + morale, data)
summary(model)

model= lm(sales ~ marketing + morale, data)
summary(model)

plot(model$residuals)

model = lm(sales ~ I(marketing*marketing) + morale, data)
summary(model)
plot(model$residuals)

model = lm(sales ~ I(marketing*marketing)- 1, data)
summary(model)






data = read.csv("C:\\Users\\Roman\\Desktop\\data analysis\\sales4.csv")
model= lm(sales ~ research + marketing + morale, data)
summary(model)

model= lm(sales ~ research + marketing, data)
summary(model)

plot(model$residuals)

model= lm(sales ~ log(research) + marketing, data)
summary(model)

plot(model$residuals)


model= lm(sales ~ research + log(marketing), data)
summary(model)

plot(model$residuals)


model= lm(sales ~ log(marketing), data)
summary(model)

plot(model$residuals)
