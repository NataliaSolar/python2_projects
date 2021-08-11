#Load the data file from data\\xyab.csv
data = read.csv("C:\\Users\\Roman\\Desktop\\data analysis\\xyab.csv")


#Answer the following questions. In your submission include only


#the results. Comment (but don't remove) any steps that you used 


#to get to the results (i.e. distribution tests). The results


#need to come from calculations and can't be hard-coded.


#I will manually review the code after the submission date.


#Assume x, y, a, and b represent samples


#Round all your results to 2 decimals



#What are the chances that the variable x will take a value below 1.5?
ks.test(data$x, "punif", min(data$x), max(data$x))
#p-value = 0.5039 =>unifom
shapiro.test(data$x)
#p-value < 2.2e-16 => not normal
round(punif(1.5, min(data$x), max(data$x)), 2)


#What are the chances that the variable y will take a value below 1.5?
ks.test(data$y, "punif", min(data$y), max(data$y))
# p-value = 0.07785 => uniform
shapiro.test(data$y)
#p-value < 2.2e-16 => not normal
result = punif(1.5, min(data$y), max(data$y))
round(result, 2)



#What the are chances that the variable a will take a value between 1.1 and 1.2?
ks.test(data$a, "punif", min(data$a), max(data$a))
# p-value < 2.2e-16 => not uniform
shapiro.test(data$a)
#p-value = 0.3901 =>normal
result = pnorm(1.2,mean(data$a), sd(data$a)) - pnorm(1.1,mean(data$a), sd(data$a))
round(result, 2)



#What is the value of the variable b for which 60% of the values are below it?
ks.test(data$b, "punif", min(data$b), max(data$b))
# p-value < 2.2e-16 => not uniform
shapiro.test(data$b)
#p-value = 0.9341 =>normal
result = qnorm(.6,mean(data$b), sd(data$b))
round(result, 2)


#What is the value of the variable (a + b) for which 10% of the values are above it?
ks.test((data$a+data$b), "punif", min(data$a+data$b), max(data$a+data$b))
# p-value < 2.2e-16 => not uniform
shapiro.test(data$a+data$b)
#p-value = 0.3987 =>normal
result = qnorm(.9,mean(data$a+data$b), sd(data$a+data$b))
round(result, 2)
