
import pyodbc
import pandas
server = 'ludsampledb.database.windows.net'
database = 'SampleDB'
username = 'sampleadmin'
password = '+U9Ly9/p'   
driver= '{ODBC Driver 17 for SQL Server}'
 
with pyodbc.connect('DRIVER='+driver+';SERVER='+server+';PORT=1433;DATABASE='+database+';UID='+username+';PWD='+ password) as conn:
    with conn.cursor() as cursor:
        cursor.execute("SELECT Rating from googleplaystore")
        #cursor.execute("SELECT count(*), round(avg(Rating),2) FROM dbo.googleplaystore")
        total = 0.0
        count = 0
        row = cursor.fetchone()
        while row:
            if row[0]:
                total += float(row[0])
                count += 1
            row = cursor.fetchone()
 
print("Average rating: ", round((total/count), 2))

