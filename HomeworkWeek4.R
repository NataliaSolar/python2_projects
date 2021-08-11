suppressMessages(library(tidyverse))

#Load the World Indicators data from "data\\World Indicators.csv"
data = read.csv("C:\\Users\\Roman\\Desktop\\data analysis\\World Indicators.csv")
view(data)
#The data is also available in the materials





#Calculate the mean Female Life Expectancy across the whole world in 2011
data2011 = data %>% filter(Year == 2011)
view(data2011)
dataFem = data2011 %>% select(Year, Life.Expectancy.Female)
dataFem = dataFem %>% filter(Life.Expectancy.Female != "NA")
view(dataFem)
result = mean(dataFem$Life.Expectancy.Female)

#Print the result with 2 decimals
round(result, 2)




#Calculate the mean birth rate across the america in 2011
dataAmerica = data2011 %>% filter(Region == "The Americas")
view(dataAmerica)
dataBRate = dataAmerica %>% select(Year, Region, Birth.Rate)
dataBRate = dataBRate %>% filter(Birth.Rate != "NA")
view(dataBRate)
result = mean(dataBRate$Birth.Rate)
#Print the result with 2 decimals
round(result, 2)


#Create a dataframe that shows the total population per year
data1 = data %>% select(Year, Population.Total)
view(data1)
#Use the column names Year and Population
dataPopulPerYear = data1 %>% group_by(Year)%>% summarise(Population = sum(Population.Total))
view(dataPopulPerYear)
#Print the data set
dataPopulPerYear



#Use the data set on the previous part to create a linear model of population


#over time. Call the model "model" and summarize it.
model = lm(Population ~ Year, dataPopulPerYear)
summary(model)
plot(dataPopulPerYear$Year, dataPopulPerYear$Population)

plot(model$residuals)
#Use the model to predict the expected population in the year 2014

#plot(wa_total$x, wa_total$Total)
#model = lm(Total ~ x, wa_total)
#dataPopulPerYear$x = 1:nrow(dataPopulPerYear)

#model = lm(dataPopulPerYear$Population ~ dataPopulPerYear$x, dataPopulPerYear)
#summary(model)
#plot(dataPopulPerYear$x, dataPopulPerYear$Population)


dataPopulPerYear$original = 1 #or true


#wa_total$original = 1 #or true

year_predict = data.frame(Year = 2014)
view(year_predict)
pr = predict(model, newdata = year_predict)
view(pr)
predicted = data.frame(Year = year_predict, Population = pr, original = 0)#or oridinal = FALSE

together = rbind(dataPopulPerYear, predicted)

plot(together$Year, together$Population)

together %>% ggplot(aes(Year, Population, color=original)) + geom_point()



#Print the prediction
pr
