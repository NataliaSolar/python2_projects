import pyodbc
import pandas
import statsmodels.api as sm
import numpy as np
from matplotlib import pyplot as plt 
import seaborn as sns

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

#sql1 = "SELECT Size FROM GooglePlayStore Where Category = 'GAME' AND Size != 'Varies with device'"
#size1 = pandas.read_sql(sql1, conn)
#size1 = np.asarray(size1['Size'])






#pandas.set_option('display.max_rows', None)
#pandas.set_option('display.max_columns', None)
#pandas.set_option('display.width', None)
#pandas.set_option('display.max_colwidth', -1)
#print(size1)
#size1 = size1['Size'].values[]      
#Your code ends here
#size1 = pandas.array(size1['Size'])

#print("Mean: " + str(round(size1.mean()/1000000, 2)))
#print("Standard Deviation: " + str(round(size1.std()/1000000, 2)))
#Mean: 44.37
#Standard Deviation: 27.74



#Use a linear model to help predict number of reviews (in thousands) based on the significant variables among

#rating, size (in MB), installs (in tens of thousands), and price (in dollars)

#Your code starts here
#sql2 = "SELECT Reviews, Rating, Size, REPLACE(REPLACE(Installs,'+', ''), ',','') as Installs, Price FROM GooglePlayStore Where Size != 'Varies with device' AND Rating NOT like '%NaN%'"
#data = pandas.read_sql(sql2, conn)

#sql3 = "SELECT count(App) as [Number of Apps], Category FROM GooglePlayStore Group by Category"
#data3 = pandas.read_sql(sql3, conn)


  
  
# Creating explode data 
#explode = (0.1, 0.0, 0.2, 0.3, 0.0, 0.0) 
  
# Creating color parameters 
#colors = ( "orange", "cyan", "brown", 
          #"grey", "indigo", "beige") 
  
# Wedge properties 
#wp = { 'linewidth' : 1, 'edgecolor' : "green" } 
  
# Creating autocpt arguments 
#def func(pct, allvalues): 
#    absolute = int(pct / 100.*np.sum(allvalues)) 
 #   return "{:.1f}%".format(pct, absolute) 
  
 #Creating plot 
#fig, ax = plt.subplots(figsize =(12, 9)) 
#fig.subplots_adjust(wspace=0, top=1, right=1, left=0, bottom=0)

#wedges, texts, autotexts = ax.pie(data3['Number of Apps'],  
 #                                 autopct = lambda pct: func(pct, data3['Number of Apps']), 
  #                                #explode = explode,  
#                                  labels = data3['Category'],
 #                                 #shadow = True, 
#                                  #colors = colors, 
#                                  #startangle = 90,
#                                  wedgeprops = wp)
                                  #textprops = dict(color ="magenda")) 
  
# Adding legend 
#ax.legend(wedges, data3['Category'], 
#          title ="Categories", 
#          loc ="center left", 
#          bbox_to_anchor =(1, 0, 0.5, 1)) 
  
#plt.setp(autotexts, size = 8, weight ="bold") 
#ax.set_title("Customizing pie chart") 
  
# show plot 
#plt.show() 
#pandas.set_option('display.max_rows', None)
#pandas.set_option('display.max_columns', None)
#pandas.set_option('display.width', None)
#pandas.set_option('display.max_colwidth', -1)
#print(data3)
#fig = plt.figure(figsize =(11, 8))
#plt.pie(data3['Number of Apps'], labels = data3['Category']) 
# Adding legend 
#fig.legend(data3['Category'], 
#          title ="Categories", 
#          loc ="center left", 
#          bbox_to_anchor =(1, 0, 0.5, 1))
  
# show plot 
#plt.show()

#sql4 = "SELECT * FROM GooglePlayStore Where Size != 'Varies with device' AND Rating NOT like '%NaN%'"
#data4 = pandas.read_sql(sql4, conn)
#print(data4.head(100))

#sns.displot(data4['Rating'], hist=True)

#plt.show()

sql5 = "SELECT App, sum(cast(REPLACE(REPLACE(Installs,'+', ''), ',','') AS INT)/1000000) as Installs FROM GooglePlayStore WHERE installs NOT like '%NaN%' GROUP BY App order by Installs desc"
data5 = pandas.read_sql(sql5, conn)


for index in data5.index:
    data5.loc[index,'Installs'] = float(data5.loc[index,'Installs'])

#data8 = data5.groupby("App")["Installs"].sum()
#data7 = data5.head(15)
#print(data5.head(15))
#name = df['car'].head(12)
#price = df['price'].head(12)
 
# Figure Size
#fig, ax = plt.subplots(figsize =(20, 8))
 
# Horizontal Bar Plot
#ax.barh(data7["App"], data7['Installs'])
 
# Remove axes splines
#for s in ['top', 'bottom', 'left', 'right']:
#    ax.spines[s].set_visible(False)
 
# Remove x, y Ticks
#ax.xaxis.set_ticks_position('none')
#ax.yaxis.set_ticks_position('none')
 
# Add padding between axes and labels
#ax.xaxis.set_tick_params(pad = 5)
#ax.yaxis.set_tick_params(pad = 10)
 
# Add x, y gridlines
#ax.grid(b = True, color ='grey',
#        linestyle ='-.', linewidth = 0.5,
#        alpha = 0.2)
 
# Show top values 
#ax.invert_yaxis()
 
# Add annotation to bars
#for i in ax.patches:
#    plt.text(i.get_width()+0.2, i.get_y()+0.5, 
#             str(round((i.get_width()), 2)),
#             fontsize = 10, fontweight ='bold',
#             color ='grey')
 
# Add Plot Title
#ax.set_title('Installs in millions',
#             loc ='left', )
 
# Add Text watermark
#fig.text(0.9, 0.15, 'Jeeteshgavande30', fontsize = 12,
#         color ='grey', ha ='right', va ='bottom',
#         alpha = 0.7)
 
# Show Plot
#plt.show()




#for index in data.index:
#    if data.loc[index,'Size'][-1]=='M':
#        data.loc[index,'Size'] = pandas.to_numeric(data.loc[index,'Size'][:len(data.loc[index,'Size']) - 1])
#    else:
#        data.loc[index,'Size'] = pandas.to_numeric(data.loc[index,'Size'][:len(data.loc[index,'Size']) - 1])/1000
#
#    if data.loc[index,'Price'][0] == '$':
#        data.loc[index,'Price'] = pandas.to_numeric(data.loc[index,'Price'][1:])
#
#    data.loc[index,'Installs'] = pandas.to_numeric(data.loc[index,'Installs'])/10000
#
#    data.loc[index,'Reviews'] = pandas.to_numeric(data.loc[index,'Reviews'])/1000

#    data.loc[index,'Rating'] = pandas.to_numeric(data.loc[index,'Rating'])




#x1 = data[["Rating", "Size", "Installs"]]
#x1 = data["Price"]
#x = sm.add_constant(x1)
#y =  data["Reviews"]
#fit = sm.OLS(y,x.astype(float)).fit()
#print(fit.summary())


#Your code ends here


#prediction = fit.predict([[1, 4.5, 100000, 100000]])
#print("Prediction: " + str(int(round(prediction[0], 0))))
#Prediction: 1130468



sql6 = "SELECT Category, ROUND(sum(cast(REPLACE(REPLACE(Installs,'+', ''), ',','') AS NUMERIC)/1000000),2) as Installs FROM GooglePlayStore WHERE installs NOT like '%NaN%' GROUP BY Category order by Installs desc"
data6 = pandas.read_sql(sql6, conn)
#for index in data5.index:
#    data6.loc[index,'Installs'] = (data6.loc[index,'Installs'])
#print(data6.head(30))


# Figure Size
#fig, ax = plt.subplots(figsize =(20, 8))
 
# Horizontal Bar Plot
#ax.barh(data6["Category"], data6['Installs'], color = "green")
 
# Remove axes splines
#for s in ['top', 'bottom', 'left', 'right']:
#    ax.spines[s].set_visible(False)
 
# Remove x, y Ticks
#ax.xaxis.set_ticks_position('none')
#ax.yaxis.set_ticks_position('none')
 
# Add padding between axes and labels
#ax.xaxis.set_tick_params(pad = 5)
#ax.yaxis.set_tick_params(pad = 10)
 
# Add x, y gridlines
#ax.grid(b = True, color ='grey',
#        linestyle ='-.', linewidth = 0.5,
#        alpha = 0.2)
 
# Show top values 
#ax.invert_yaxis()
 
# Add annotation to bars
#for i in ax.patches:
#    plt.text(i.get_width()+0.2, i.get_y()+0.5, 
 #            str(round((i.get_width()), 2)),
#             fontsize = 10, fontweight ='bold',
#             color ='grey')
 
# Add Plot Title
#ax.set_title('Installs in millions',
#             loc ='left', )
 
# Add Text watermark
#fig.text(0.9, 0.15, 'Jeeteshgavande30', fontsize = 12,
#         color ='grey', ha ='right', va ='bottom',
#         alpha = 0.7)
 
# Show Plot
#plt.show()

# Is there a correlation between downloads and ratings? (i.e. more downloads better ratings)
sql8 = "SELECT Rating, cast(REPLACE(REPLACE(Installs,'+', ''), ',','') AS NUMERIC)/1000000 as Installs FROM GooglePlayStore WHERE installs NOT like '%NaN%' AND Rating NOT like '%NaN%' order by Rating desc"
data8 = pandas.read_sql(sql8, conn)

#print(data8.head(30))

#plt.plot(data8["Rating"], data8["Installs"], "bo", c= "r")
#plt.show()

#How many downloads would we need to be on the top 10% of downloads
sql9 = "SELECT count(cast(REPLACE(REPLACE(Installs,'+', ''), ',','') AS NUMERIC)/1000) as count, cast(REPLACE(REPLACE(Installs,'+', ''), ',','') AS NUMERIC)/1000 as Installs FROM GooglePlayStore WHERE installs NOT like '%NaN%' and cast(REPLACE(REPLACE(Installs,'+', ''), ',','') AS NUMERIC)/1000 >= 100000 group by Installs order by Installs desc"
data9 = pandas.read_sql(sql9, conn)
#print(data9.head(30))
sql10 = "SELECT cast(REPLACE(REPLACE(Installs,'+', ''), ',','') AS NUMERIC) as Installs FROM GooglePlayStore WHERE installs NOT like '%NaN%' order by Installs desc"
data10 = pandas.read_sql(sql10, conn)
print(data10.head(100))
p = np.percentile(data10["Installs"], 90) # return 90th percentile, e.g median.
print(p)


# Figure Size
fig, ax = plt.subplots(figsize =(20, 8))
 
# Horizontal Bar Plot
ax.barh(data9["Installs"], data9['Installs'])
 
# Remove axes splines
for s in ['top', 'bottom', 'left', 'right']:
    ax.spines[s].set_visible(False)
 
# Remove x, y Ticks
ax.xaxis.set_ticks_position('none')
ax.yaxis.set_ticks_position('none')
 
# Add padding between axes and labels
ax.xaxis.set_tick_params(pad = 5)
ax.yaxis.set_tick_params(pad = 10)
 
# Add x, y gridlines
ax.grid(b = True, color ='grey',
        linestyle ='-.', linewidth = 0.5,
        alpha = 0.2)
 
# Show top values 
ax.invert_yaxis()
 
# Add annotation to bars
for i in ax.patches:
    plt.text(i.get_width()+0.2, i.get_y()+0.5, 
             str(round((i.get_width()), 2)),
             fontsize = 10, fontweight ='bold',
             color ='grey')
 
# Add Plot Title
ax.set_title('Installs in millions',
             loc ='left', )
 
# Add Text watermark
#fig.text(0.9, 0.15, 'Jeeteshgavande30', fontsize = 12,
#         color ='grey', ha ='right', va ='bottom',
#         alpha = 0.7)
 
# Show Plot
#plt.show()