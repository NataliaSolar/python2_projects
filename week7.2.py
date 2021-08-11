
import pyodbc
import pandas
import numpy
from sklearn.linear_model import LinearRegression
import statsmodels.api as sm
server = 'ludsampledb.database.windows.net'
database = 'SampleDB'
username = 'sampleadmin'
password = '+U9Ly9/p'   
driver= '{ODBC Driver 17 for SQL Server}'
 
conn = pyodbc.connect('DRIVER='+driver+';SERVER='+server+';PORT=1433;DATABASE='+database+';UID='+username+';PWD='+ password)
sql = "SELECT Year, sum([Population Total]) as 'Population Total' FROM WorldIndicators WHERE Region = 'Asia' Group By Year"
byyear = pandas.read_sql(sql,conn)


x = numpy.array(byyear["Year"]).reshape(-1, 1) # reshape makes x a 2d array
y = list(byyear["Population Total"])
 
lm = LinearRegression().fit(x, y)
print(byyear)
print(lm.predict(numpy.array([[2015]])))




