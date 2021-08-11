import pyodbc
import pandas
import statsmodels.api as sm
import numpy as np

import pyodbc
import pandas

server = 'ludsampledb.database.windows.net'
database = 'SampleDB'
username = 'sampleadmin'
password = '+U9Ly9/p'   
driver= '{ODBC Driver 17 for SQL Server}'

#Create a variable conn that opens a connection to the database with the parameters above

#Your code starts here
conn = pyodbc.connect("DRIVER="+driver+";SERVER="+server+";PORT=1433;DATABASE="+database+";UID="+username+";PWD="+ password)

#Your code ends here


#Create a SQL query named sql3 that returns total population by year for the 'The Americas' region

#Your code starts here
sql3 = "SELECT Year, sum([Population Total]) as 'Population Total' FROM WorldIndicators WHERE Region = 'The Americas' Group By Year"

#Your code ends here


data3 = pandas.read_sql(sql3, conn)
print(data3)

#Using the data set from the sql3 query preduct the population in 'The Americas' in 2015

#Your code starts here
x = data3["Year"]
x = sm.add_constant(x)
y = data3["Population Total"]
fit = sm.OLS(y,x).fit()
print(fit.predict([1,2015]))
#print(prediction)
#Your code ends here
