
#Load the data from the data\\week1.csv file
data = read.csv("C:\\Users\\Roman\\Desktop\\data analysis\\week1.csv")

#From now on all questions are about the x column in the data

#x represents a sample from a larger data set


#Run the Kolmogorov-Smirnov on the data
ks.test(data$x, "punif", min(data$x), max(data$x))


#Run the Kolmogorov-Smirnov test on the data
shapiro.test(data$x)


#Calculate the percentage of data points that are below 140
result = punif(140, min(data$x), max(data$x))

#Round the result to 4 decimal places
round(result, 4)



#Calculate the percentage of data points that are above 170
result = 1- punif(170,min(data$x), max(data$x))

#Round the result to 4 decimal places
round(result, 4)


#Calculate the percentage of data points that are between 150 and 160
result = punif(160,min(data$x), max(data$x)) - punif(150,min(data$x), max(data$x))
#Round the result to 4 decimal places
round(result, 4)






#__________________________________________


#Load the data from the data\\week1.csv file
data = read.csv("C:\\Users\\Roman\\Desktop\\data analysis\\week1.csv")


#From now on all questions are about the y column in the data

#y represents a sample from a larger data set


#Run the Kolmogorov-Smirnov on the data
ks.test(data$y, "punif", min(data$y), max(data$y))
#not uniform


#Run the Kolmogorov-Smirnov test on the data
shapiro.test(data$y)
#normal

#Calculate the percentage of data points that are below 100
result = pnorm(100,mean(data$y), sd(data$y))


#Round the result to 4 decimal places
round(result, 4)


#Calculate the percentage of data points that are above 110
result = 1- pnorm(110,mean(data$y), sd(data$y))
#Round the result to 4 decimal places
round(result, 4)


#Calculate the percentage of data points that are between 90 and 110
result = pnorm(110,mean(data$y), sd(data$y)) - pnorm(90,mean(data$y), sd(data$y))
#Round the result to 4 decimal places
round(result, 4)



#expected output

#[1] 1
#[1] 0.1681
#[1] 0.6939







