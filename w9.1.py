import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
from sklearn.cluster import KMeans
 
x = [1, 2, 3, 4, 5]
y = [1, 2, 7, 8, 9]
 
X = [[1, 1], [2, 2], [3, 7], [4, 8], [5, 9]]
 
#kmeans is the algorithm we described
kmeans = KMeans(n_clusters = 2)
groups = kmeans.fit_predict(X)

plt.scatter(x, y, c=groups)
#plt.show()

#create 3 custers from points.



x = [1, 2, 3, 4, 5,6,7,8,9]
y = [8, 9, 8.5, 1, 2,1.5,12,13.5,12.5]
 
X = [[1, 8], [2, 9], [3, 8.5], [4, 1], [5, 2], [6,1.5], [7,12], [8,13.5], [9,12.5]]
 
#kmeans is the algorithm we described
kmeans = KMeans(n_clusters = 3)
groups = kmeans.fit_predict(X)

plt.scatter(x, y, c=groups)
#plt.show()


data = pd.read_csv("C:\\Users\\Roman\\Desktop\\data analysis\\marketing.csv")
kmeans = KMeans(n_clusters = 3)
data = data[["V1","V2","V3", "V4", "V5", "V6"]]
#print(data)
groups = kmeans.fit_predict(data)


data['Group'] = groups
#print(data)

#print(data[data['Group'] == 0])

group0 =data[data['Group'] == 0] 
group1 =data[data['Group'] == 1] 
group2 =data[data['Group'] == 2] 

#print(group0)
#print(group1)
#print(group2)

print("Group 0")
print("V1")
print(group0['V1'].mean())
print("V2")
print(group0['V2'].mean())
print("V3")
print(group0['V3'].mean())
print("V4")
print(group0['V4'].mean())
print("V5")
print(group0['V5'].mean())
print("V6")
print(group0['V6'].mean())



print("Group 1")
print("V1")
print(group1['V1'].mean())
print("V2")
print(group1['V2'].mean())
print("V3")
print(group1['V3'].mean())
print("V4")
print(group1['V4'].mean())
print("V5")
print(group1['V5'].mean())
print("V6")
print(group1['V6'].mean())


print("Group 2")
print("V1")
print(group2['V1'].mean())
print("V2")
print(group2['V2'].mean())
print("V3")
print(group2['V3'].mean())
print("V4")
print(group2['V4'].mean())
print("V5")
print(group2['V5'].mean())
print("V6")
print(group2['V6'].mean())





import yfinance as yf