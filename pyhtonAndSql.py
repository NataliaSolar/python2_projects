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


#Create a SQL query (a string) named sql1 that returns the total population by country in 2011

#Your code starts here
sql1 = "SELECT TOP 5 [Country/Region], sum([Population Total]) as 'Population Total' FROM WorldIndicators WHERE Year = '2011' Group By [Country/Region] order by [Population Total] desc"
#sql = "SELECT Year, sum([Population Total]) as 'Population Total' FROM WorldIndicators WHERE Region = 'Asia' Group By Year"

#Your code ends here


data1 = pandas.read_sql(sql1, conn)
print(data1)



#Create a SQL query (a string) named sql2 that returns the average population by region in 2011

#Your code starts here
sql2 = "SELECT Region, avg([Population Total]) as 'Average Population' FROM WorldIndicators WHERE Year = 2011 Group By Region"


#Your code ends here


data2 = pandas.read_sql(sql2, conn)
print(data2)

