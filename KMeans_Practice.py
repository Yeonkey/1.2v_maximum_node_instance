import pandas as pd
import numpy as np
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
import seaborn as sns
from random import *

Coordinates=[]
num = round(uniform(0, 1000),2)

def randomxy (z):
    global num
    for i in range(z):
        while num in Coordinates :
            num = round(uniform(0, 1000),2)
        Coordinates.append(num)

x=int(input("좌표수를 입력하세요"))
randomxy(z= 2 * x)

#데이타 포인트
df = pd.DataFrame(columns = ['x', 'y'])


j = 0
for i in range(x):
    df.loc[i] = [Coordinates[j], Coordinates[j+1]]
    j = j + 2

print(df.head(x))
#2D 차트로 만들
sns.lmplot(x = "x", y = "y", data=df,
           fit_reg=False, scatter_kws = {"s" : 200})

#title
plt.title('kmean plot')

#x label
plt.xlabel('x')

#y label
plt.ylabel('y')

plt.show()
#k-mean clustering

data_points = df.values


kmeans = KMeans(n_clusters = 5).fit(data_points) #n_clusters = n(n은 initial centroid)

print("\ncluster number")
print(kmeans.labels_)
#kmeans.cluster.centers_ 이게 왜 안되지..

df['cluster_num'] = kmeans.labels_

print('df')
print(df.head(x))

sns.lmplot('x', 'y', data=df, fit_reg = False,
           scatter_kws = {"s" : 150}, hue = "cluster_num")

plt.title('after kmeans clustering')
plt.show()
