import pyodbc
import pandas
import statsmodels.api as sm
import numpy as np

server = 'ludsampledb.database.windows.net'
database = 'SampleDB'
username = 'sampleadmin'
password = '+U9Ly9/p'   
driver = '{ODBC Driver 17 for SQL Server}'
table = 'GooglePlayStore'

conn = pyodbc.connect('DRIVER='+driver+';SERVER='+server+';PORT=1433;DATABASE='+database+';UID='+username+';PWD='+ password)

#Create a combination of a SQL query and data manipulation in 

#Python to generate a list that can be used to calculate the average and standard deviation application size in MB for the GAME category 

#Your code starts here

sql1 = "SELECT Size FROM GooglePlayStore Where Category = 'GAME' AND Size != 'Varies with device'"
size1 = pandas.read_sql(sql1, conn)
#size1 = np.asarray(size1['Size'])


#for i in range(len(size1)):
#    if size1[i][-1] == 'M':
#        size1[i] = pandas.to_numeric(size1[i][:len(size1[i]) - 1])*1000000
#    else:
#       size1[i] = pandas.to_numeric(size1[i][:len(size1[i]) - 1])

for index in size1.index:
    if size1.loc[index,'Size'][-1]=='M':
        size1.loc[index,'Size'] = pandas.to_numeric(size1.loc[index,'Size'][:len(size1.loc[index,'Size']) - 1])*1000000
    else:
       size1.loc[index,'Size'] = pandas.to_numeric(size1.loc[index,'Size'][:len(size1.loc[index,'Size']) - 1])



#print(size1)
#size1 = np.array(size1['Size'])  

#pandas.set_option('display.max_rows', None)
#pandas.set_option('display.max_columns', None)
#pandas.set_option('display.width', None)
#pandas.set_option('display.max_colwidth', -1)
#print(size1)
#size1 = size1['Size'].values[]      
#Your code ends here
size1 = pandas.array(size1['Size'])

print("Mean: " + str(round(size1.mean()/1000000, 2)))
print("Standard Deviation: " + str(round(size1.std()/1000000, 2)))
#Mean: 44.37
#Standard Deviation: 27.74

#Mean: 44.36867
#Standard Deviation: 27.73019
#Prediction: 1130468
#1014  17000000

#Mean: Size    44.36867
#dtype: float64
#Standard Deviation: Size    27.74386
#dtype: float64
#Prediction: 1130468

#Use a linear model to help predict number of reviews (in thousands) based on the significant variables among

#rating, size (in MB), installs (in tens of thousands), and price (in dollars)

#Your code starts here
sql2 = "SELECT Reviews, Rating, Size, REPLACE(REPLACE(Installs,'+', ''), ',','') as Installs, Price FROM GooglePlayStore Where Size != 'Varies with device' AND Rating NOT like '%NaN%'"
data = pandas.read_sql(sql2, conn)
#pandas.set_option('display.max_rows', None)
#pandas.set_option('display.max_columns', None)
#pandas.set_option('display.width', None)
#pandas.set_option('display.max_colwidth', -1)



for index in data.index:
    if data.loc[index,'Size'][-1]=='M':
        data.loc[index,'Size'] = pandas.to_numeric(data.loc[index,'Size'][:len(data.loc[index,'Size']) - 1])
    else:
        data.loc[index,'Size'] = pandas.to_numeric(data.loc[index,'Size'][:len(data.loc[index,'Size']) - 1])/1000

    if data.loc[index,'Price'][0] == '$':
        data.loc[index,'Price'] = pandas.to_numeric(data.loc[index,'Price'][1:])

    data.loc[index,'Installs'] = pandas.to_numeric(data.loc[index,'Installs'])/10000

    data.loc[index,'Reviews'] = pandas.to_numeric(data.loc[index,'Reviews'])/1000

    data.loc[index,'Rating'] = pandas.to_numeric(data.loc[index,'Rating'])

#print(data3)


x1 = data[["Rating", "Size", "Installs"]]
#x1 = data["Price"]
x = sm.add_constant(x1)
y =  data["Reviews"]
fit = sm.OLS(y,x.astype(float)).fit()
#print(fit.summary())


#Your code ends here


prediction = fit.predict([[1, 4.5, 100000, 100000]])
print("Prediction: " + str(int(round(prediction[0], 0))))
#Prediction: 1130468