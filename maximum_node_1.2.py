from sklearn.datasets import make_blobs
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import random as r

######각 군집별 정점 개수 저장하는 배열
G0 = []
G1 = []
G2 = []
G3 = []
G4 = []
G5 = []
G6 = []
G7 = []
G8 = []
G9 = []
######
x = []
w = []
#x는 정점배열, w 는 표준편차 배열
for i in range(5):
    randX = r.randrange(50, 150)
    randY = 200 - randX
    x.append(randX)
    x.append(randY)

for i in range(10):
    randW = r.randrange(10, 60)
    w.append(randW)


z = [[200, 200], [400, 400], [600, 600], [800, 800], [200, 500], [200, 800], [500, 800], [500, 200], [800, 200], [800, 500]]
#z는 initial centroid

#x = 정점수, center = initial centroid, std = 표준편차, center_box = 표 크기
X, y = make_blobs(x, centers = z, cluster_std = w, center_box = (0.0, 1000.1000))
#print(X) # 정점에 대한 정보
#print(y) # 각 정점에 대한 클러스터링 넘버
rgb = np.array(['b', 'g', 'r', 'c', 'm', 'y', 'k', 'k', 'k', 'k']) # centers값이 변경되면 색 값도 넣어줘야함
plt.scatter(X[:, 0], X[:, 1], color = rgb[y])
plt.show()



for i in range (1000):
    if y[i] == 0:
        G0.append(y[i])
    if y[i] == 1:
        G1.append(y[i])
    if y[i] == 2:
        G2.append(y[i])
    if y[i] == 3:
        G3.append(y[i])
    if y[i] == 4:
        G4.append(y[i])
    if y[i] == 5:
        G5.append(y[i])
    if y[i] == 6:
        G6.append(y[i])
    if y[i] == 7:
        G7.append(y[i])
    if y[i] == 8:
        G8.append(y[i])
    if y[i] == 9:
        G9.append(y[i])


fw=open("inputfile.txt", "w")
fw.write(str(1000))
fw.write('\n')
fw.write(str(len(z)))
fw.write('\n')
fw.write(str(len(G0)) + ' ')
fw.write(str(len(G1)) + ' ')
fw.write(str(len(G2)) + ' ')
fw.write(str(len(G3)) + ' ')
fw.write(str(len(G4)) + ' ')
fw.write(str(len(G5)) + ' ')
fw.write(str(len(G6)) + ' ')
fw.write(str(len(G7)) + ' ')
fw.write(str(len(G8)) + ' ')
fw.write(str(len(G9)) + ' ')
fw.write('\n')
j = 0
while j < len(X):
    fw.write(str(X[j]) + ' ')
    fw.write(str(y[j]))
    fw.write('\n')
    j += 1
fw.close()
print("inputfile에 저장")
