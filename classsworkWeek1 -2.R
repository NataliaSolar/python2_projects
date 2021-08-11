1
1+1
1+1
x = c(1,2,3,4,5)#c creates list
y = c(1,2,3,4,5)

plot(x,y)#create a chart

model = lm(y~x)#lm is a function 
summary(model)


y1 = c(2,3,4,5,6)
model1 = lm(y1 ~x)
summary(model1)


y2 = c(10,17,24,31,38)
model2 = lm(y2 ~x)
summary(model2)
#Y = 7x + 3




y3 = c(10.5,11,11.5,12,12.5)
model3 = lm(y3 ~x)
summary(model3)
#Y = 0.5x + 10


y4 = c(5.859873,9.001465,12.14306,15.28465,18.42624)
model4 = lm(y4 ~x)
summary(model4)
#Y = 3.142x + 2.718


y5 = c(2,5,10,17,26)

plot(x,y5)
model5 = lm(y5 ~ I(x*x))
summary(model5)




y6 = c(3,7,13,21,31)

plot(x,y6)
model6 = lm(y6 ~ I(x*x) + x)
summary(model6)

y7 = x*x*x +x
model7 = lm(y7 ~ I(x*x*x)+I(x*x)+ I(x))
summary(model7)



y8 = log(x)
plot(x,y8)
model8 = lm(y8 ~ log(x))
summary(model8)



y9 = c(20.3,52.4,108.5,195.8, 321.5)
plot(x, y9)
model9 = lm(y9 ~ I(x*x*x) + I(x*x)+x)
#Y = 1.2x^3 + 4.8x^2 + 9.3x + 5  

y10 = c(3.1, 12.91175, 28.71111,50.6235,78.68825)
plot(x,y10)
model10 = lm(y10 ~ I(x*x*x) + I(x*x)+x)
summary(model10)
#Y = 0.014x^3 + 2.921x^2 + 0.948x - 0.781

y11 = c(15.70796, 21.99115, 34.55752, 53.40708, 78.53982)
plot(x,y11)
model11 = lm(y11 ~ I(x*x*x) + I(x*x)+x)
summary(model11)
#Y = pi*x^2 - pi*x + 5pi



a= c(1,2,3,4,5)
b= c(2,3,4,5,6)
c = c(3,4,5,6,7)
y12 = c(6,9,12,15,18)
model12 = lm(y ~ a+b+c)
summary(model12)


data = read.csv("C:\\Users\\Roman\\Desktop\\data analisys\\abcy.csv")
plot(data$a, data$b,data$c,data$y)
model13 = lm(data$y ~ I(data$a*data$a) + data$b + data$c)
summary(model13)







#############week 2

grades = c(3.2,3.1,3.5,3.4,3.6,4,3.5,3.8,3.9,3)
median(grades)

quantile(grades, 0.75)
quantile(grades, .90)

quantile(grades)

quantile(grades,c(.1,.9))



data = read.csv("C:\\Users\\Roman\\Desktop\\data analisys\\grades3.csv")

median(data$x)
quantile(data$x, c(0.75, 0.9, 0.99))

#q1
quantile(data$x, .98)


#q2
quantile(data$x, 0.95)

#q3
quantile(data$x, 0.2)


#q4
quantile(data$x, 1)

quantile(data$x, c(.98, .95, 0.2, 1))



mean(grades)
sd(grades)


hist(grades)
plot(grades)

plot(sample(grades))

data = read.csv("C:\\Users\\Roman\\Desktop\\data analisys\\da1.csv")
hist(data$x)
mean(data$x)
sd(data$x)

hist(data$y)
max(data$y)
min(data$y)


hist(data$z)
mean(data$z)
sd(data$z)



ks.test(data$x, "punif", min(data$x), max(data$x))
ks.test(data$y, "punif", min(data$y), max(data$y))

shapiro.test(data$x)
shapiro.test(data$y)


data = read.csv("C:\\Users\\Roman\\Desktop\\data analisys\\da2.csv")
ks.test(data$x, "punif", min(data$x), max(data$x))
shapiro.test(data$x)

max(data$x)
min(data$x)

ks.test(data$y, "punif", min(data$y), max(data$y))
shapiro.test(data$y)
hist(data$y)
plot(sample(data$y))
mean(data$y)
sd(data$y)

da1 = read.csv("C:\\Users\\Roman\\Desktop\\data analisys\\da1.csv")
qnorm(.1,mean(da1$x), sd(da1$x))
qnorm(.9,mean(da1$x), sd(da1$x))

#number of point in % below 6
pnorm(6,mean(da1$x), sd(da1$x))
#number of point in % above 7
1- pnorm(7,mean(da1$x), sd(da1$x))
# number of point between 6 and 7
pnorm(7, mean(da1$x), sd(da1$x)) - pnorm(6, mean(da1$x), sd(da1$x))



#for uniform dist: qunif and punif



data = read.csv("C:\\Users\\Roman\\Desktop\\data analisys\\weight-height (2).csv")

install.packages("tidyverse")
library("tidyverse")
male = data %>% filter(Gender == "Male")
female = data %>% filter(Gender == "Female")

shapiro.test(data$Height)
hist(data$Height)


shapiro.test(male$Height)
hist(data$Height)

1 - pnorm(70, mean(female$Height),sd(female$Height))
pnorm(65, mean(female$Height),sd(female$Height))
qnorm(0.9,mean(female$Height),sd(female$Height))


1 - pnorm(70, mean(male$Height),sd(male$Height))
pnorm(65, mean(male$Height),sd(male$Height))
qnorm(0.9,mean(male$Height),sd(male$Height))

