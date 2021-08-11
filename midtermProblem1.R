suppressMessages(library(tidyverse))

#Load the World Indicators data from "data\\World Indicators.csv"
data = read.csv("C:\\Users\\Roman\\Desktop\\data analysis\\World Indicators.csv")

#The data is also available in the materials
view(data)



#Create a linear model between year and population in the US
dusa = data %>%  select(ï..Country.Region,Year, Population.Total) %>%
  filter(ï..Country.Region == "United States")
view(data1)

model = lm(Population.Total ~ Year, dusa)

#Summarize the model and predict the expected population in 2015
summary(model)
year_predict = data.frame(Year = 2015)
view(year_predict)
pr = predict(model, newdata = year_predict)
pr


#Name the model "model"




#For the data from Europe 
deurope = data %>% select(Region, Birth.Rate, GDP, Health.Exp...GDP, Infant.Mortality.Rate, Life.Expectancy.Female, Life.Expectancy.Male) %>%
  filter(Region == "Europe")
view(data2)

#Create a linear model between Life Expectancy Female and the 


#significant predictors among


#Birth Rate


#GDP


#Health Exp % GDP


#Infant Mortality Rate


#Life Expectancy Male


#Name your model 'model', summarize it and use it to predict the 
model = lm(Life.Expectancy.Female ~   GDP + Health.Exp...GDP + Infant.Mortality.Rate + Life.Expectancy.Male, deurope)
summary(model)
#Expected Life Expectancy Female of a country with this characteristics


#Birth Rate = 3%


#GDP = 1 billion


#Health Exp % GDP = 4%


#Infant Mortality Rate = 5%


#Life Expectancy Male = 80
f_predict = data.frame(Birth.Rate = 0.03, GDP = 1000000000, Health.Exp...GDP = 0.04, Infant.Mortality.Rate = 0.05, Life.Expectancy.Male = 80)

view(f_predict)
pr = predict(model, newdata = f_predict)

#Round the prediction to two decimal points
round(pr, 2)












#------------------------













suppressMessages(library(tidyverse))

#Load the World Indicators data from "data\\World Indicators.csv"
data = read.csv("data\\World Indicators.csv")


#The data is also available in the materials




#Create a linear model between year and population in the US
dusa = data %>%  select(Country.Region,Year, Population.Total) %>%
  filter(Country.Region == "United States")
model = lm(Population.Total ~ Year, dusa)


#Summarize the model and predict the expected population in 2015
summary(model)
year_predict = data.frame(Year = 2015)
view(year_predict)
pr = predict(model, newdata = year_predict)
pr
#Name the model "model"




#For the data from Europe 
deurope = data %>% select(Region, Birth.Rate, GDP, Health.Exp...GDP, Infant.Mortality.Rate, Life.Expectancy.Female, Life.Expectancy.Male) %>%
  filter(Region == "Europe")

#Create a linear model between Life Expectancy Female and the 


#significant predictors among


#Birth Rate


#GDP


#Health Exp % GDP


#Infant Mortality Rate


#Life Expectancy Male


#Name your model 'model', summarize it and use it to predict the 
model = lm(Life.Expectancy.Female ~  GDP + Health.Exp...GDP + Infant.Mortality.Rate + Life.Expectancy.Male, deurope)
summary(model)
f_predict = data.frame(Birth.Rate = 0.03, GDP = 1000000000, Health.Exp...GDP = 0.04, Infant.Mortality.Rate = 0.05, Life.Expectancy.Male = 80)

view(f_predict)
pr = predict(model, newdata = f_predict)


#Expected Life Expectancy Female of a country with this characteristics


#Birth Rate = 3%


#GDP = 1 billion


#Health Exp % GDP = 4%


#Infant Mortality Rate = 5%


#Life Expectancy Male = 80


#Round the prediction to two decimal points
round(pr, 2)