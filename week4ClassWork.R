data = read.csv("C:\\Users\\Roman\\Desktop\\data analysis\\covid_cases.csv")
library(tidyverse)

ncols = ncol(data)
data1 = gather(data, "year", "cases", 3:ncols)
view(data1)

data = read.csv("C:\\Users\\Roman\\Desktop\\data analysis\\Data3-1.csv")

ncols = ncol(data)
data1 = gather(data, "date", "cases", 3:ncols)
view(data1)


#mutate
# %>%
#install.packages("dplyr")
#library(dplyr)

data1 = data %>% gather("year", "cases", 3:ncols)
data2 = data1 %>% mutate(year = str_replace(year, "X", ""))
data3 = data2 %>% mutate(year = as.Date(year, "%m.%d.%Y"))

data3 = data2 %>% mutate(year = year %>% as.Date(year, "%m.%d.%Y"))

wa_data = data# %>% filter(State = "WA")
king_data = wa_data %>% filter(CountyName == "King County")

king_data1 = king_data %>% select(CountyName, year, cases)

king_data2 = king_data1 %>% mutate(Date = year)%>% mutate(Cases = cases)















#___________________________

#data.gather...
data1 = data %>% gather("year", "cases", 3:ncols)

data2 = data1 %>% mutate(year = str_replace(year, "X", ""))

data3 = data2 %>% mutate(year = as.Date(year, "%m.%d.%Y"))

#data.gather...
data1 = data %>% gather("year", "cases", 3:ncols)

data2 = data1 %>% mutate(year = str_replace(year, "X", ""))

data3 = data2 %>% mutate(year = as.Date(year, "%m.%d.%Y"))

data4 = data %>% gather("year", "cases", 3:ncols) %>% 
  mutate(year = year %>% str_replace("X", "")) %>%
  mutate(year = year %>% as.Date("%m.%d.%Y"))

#SQL Where
wa_data = data3 %>% filter(State == "WA")
king_data = wa_data %>% filter(ï..CountyName == "King County")

#SQL Select
king_data1 = king_data %>% select(-State)

king_data1 = king_data %>% select(ï..CountyName, year, cases)

king_data2 = king_data1 %>% mutate(CountyName = ï..CountyName) %>%
  mutate(Date = year) %>% 
  mutate(Cases = cases) %>%
  select(-year, -cases, -ï..CountyName)

view(king_data2)

#average cases per day in king County though this data
mean(king_data2$Cases)

plot(king_data2$Cases)








data = read.csv("C:\\Users\\Roman\\Desktop\\data analysis\\covid_cases.csv")
view(data)
ncols = ncol(data)
data1 = gather(data, "date", "cases", 3:ncols)


data2 = data1 %>% mutate(date = str_replace(date, "X", ""))

data3 = data2 %>% mutate(date = as.Date(date,"%m.%d.%Y" ))
 fl_data = data3 %>% filter(State == "FL")
fl_june = fl_data %>% filter(date <= "2020-06-01")
view(fl_june)

plot(fl_june$cases)

#group by/ summarise (groups and aggrigates)
#any summarization functions, special one n() = count
florida_total = fl_june %>%
  group_by(State, date) %>%
  summarise(Total = sum(cases))
plot(florida_total$Total)

x= 1:nrow(florida_total)

totals_data = data.frame(x=x, y = florida_total$Total)
totals_data = totals_data %>% filter (x>65)

plot(totals_data$x, totals_data$y)
model = lm(y~x, totals_data)
summary(model)


plot(model$residuals)

florida_total

newdata = data.frame(x =133:150)

p = predict(model, newdata = newdata)


















ncols = ncol(data)
data1 = gather(data, "date", "cases", 3:ncols)


data2 = data1 %>% mutate(date = str_replace(date, "X", ""))

data3 = data2 %>% mutate(date = as.Date(date,"%m.%d.%Y" ))
fl_data = data3 %>% filter(State == "FL")
fl_june = fl_data %>% filter(date <= "2020-06-01")
view(fl_june)

plot(fl_june$cases)

#group by/ summarise (groups and aggrigates)
#any summarization functions, special one n() = count
florida_total = fl_june %>%
  group_by(State, date) %>%
  summarise(Total = sum(cases))
plot(florida_total$Total)

florida_total$x = nrow(florida_total)

florida_total = florida_total %>% filter (x>65)

plot(florida_total$x, florida_total$Total)
model = lm(Total~x, florida_total)
summary(model)


plot(model$residuals)

x_predict = data.frame(x = 133:150)


p = predict(model, newdata = x_predict)

predicted = data.frame(x=x_predict, Total = p, year = as.Date("1/1/1900"), state = "FL")

together = rbind(florida_total, predicted)

plot(together$x, together$Total)

together %>% ggplot(aes(x, Total, color = original)) + geom_point()

#__________________


c = ncol(data)
florida_data = data %>% gather("year", "cases", 3:c) %>% mutate(
  year = as.Date(str_replace(year, "X", ""), "%m.%d.%y"))

florida_data = florida_data %>% filter(State == "WA") %>%
  filter(year <= "2020-8-1" )

plot(florida_data$cases)

#group_by / summarize (groups and aggregates)
#any summarization functions, special one n() = count
florida_total = florida_data %>% 
  group_by(State, year) %>% 
  summarise(Total = sum(cases))

plot(florida_total$Total)

florida_total$x = 1:nrow(florida_total)

florida_total = florida_total %>% filter(x > 65)

plot(florida_total$x, florida_total$Total)
model = lm(Total ~ x, florida_total)
summary(model)

plot(model$residuals)

florida_total$original = 1

x_predict = data.frame(x = 133:150)
p = predict(model, newdata = x_predict)

predicted = data.frame(x = x_predict, Total = p, year=as.Date("1/1/1900"), State="FL", original=0)

together = rbind(florida_total, predicted)

plot(together$x, together$Total)

together %>% ggplot(aes(x, Total, color=original)) + geom_point()






#____________________Group work


data = read.csv("C:\\Users\\Roman\\Desktop\\data analysis\\covid_cases.csv")
c = ncol(data)
data = data %>% gather("year", "cases", 3:c) %>% mutate(
  year = as.Date(str_replace(year, "X", ""), "%m.%d.%y"))

wa_data = data %>% filter(State == "WA") %>%
  filter(year >= "2020-6-1" ) %>% filter(year < "2020-7-1")
view(wa_data)
plot(wa_data$cases)

#group_by / summarize (groups and aggregates)
#any summarization functions, special one n() = count
wa_total = wa_data %>% 
  group_by(State, year) %>% 
  summarise(Total = sum(cases))
view(wa_total)
plot(wa_total$Total)

wa_total$x = 1:nrow(wa_total)
view(wa_total)

plot(wa_total$x, wa_total$Total)
model = lm(Total ~ x, wa_total)
summary(model)

plot(model$residuals)

wa_total$original = 1 #or true

x_predict = data.frame(x = 31:35)
view(x_predict)
p = predict(model, newdata = x_predict)
view(p)
predicted = data.frame(x = x_predict, Total = p, year=as.Date("2020-1-7"), State="WA", original=0)#or oridinal = FALSE

together = rbind(wa_total, predicted)

plot(together$x, together$Total)

together %>% ggplot(aes(x, Total, color=original)) + geom_point()
