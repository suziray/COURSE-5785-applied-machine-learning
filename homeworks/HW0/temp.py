from matplotlib import pyplot as plt
import sys,os
import pandas as pd
def cur_file_dir():
     path = sys.path[0]
     return os.path.abspath(path)
rpath = cur_file_dir()+'/iris-data.txt'
lines = []

df = pd.read_csv(rpath, header=None)

print(df)

i = 0 
sepal_length = []
sepal_width = []
petal_length = []
petal_width = []
labels = []

while i < 150:
    sepal_length.append(round(df[0][i],2))
    sepal_width.append(round(df[1][i],2))
    petal_length.append(round(df[2][i],2))
    petal_width.append(round(df[3][i],2))
    labels.append((df[4][i]))
    i = i+1

print(labels)

color  = []
for i in range(51):
    color.append('r')
for i in range(51):
    color.append('b')
for i in range(51):
    color.append('g')

plt.figure(1)
plt.scatter(sepal_width, petal_width, c=color)
plt.xlabel('sepal width')
plt.ylabel('petal width')
plt.savefig("diagram1_1.png")

plt.figure(2)
plt.scatter(petal_width, sepal_width, c=color)
plt.xlabel('petal width')
plt.ylabel('sepal width')
plt.savefig("diagram1_2.png")

plt.figure(3)
plt.scatter(sepal_width, sepal_length, c=color)
plt.xlabel('sepal width')
plt.ylabel('sepal length')
plt.savefig("diagram2_1.png")

plt.figure(4)
plt.scatter(sepal_length, sepal_width, c=color)
plt.xlabel('sepal length')
plt.ylabel('sepal width')
plt.savefig("diagram2_2.png")

plt.figure(5)
plt.scatter(sepal_width, petal_length, c=color)
plt.xlabel('sepal width')
plt.ylabel('petal length')
plt.savefig("diagram3_1.png")

plt.figure(6)
plt.scatter(petal_length, sepal_width, c=color)
plt.xlabel('petal_length')
plt.ylabel('sepal width')
plt.savefig("diagram3_2.png")

plt.figure(7)
plt.scatter(sepal_length, petal_length, c=color)
plt.xlabel('sepal length')
plt.ylabel('petal length')
plt.savefig("diagram4_1.png")

plt.figure(8)
plt.scatter(petal_length, sepal_length, c=color)
plt.xlabel('petal length')
plt.ylabel('sepal length')
plt.savefig("diagram4_2.png")

plt.figure(9)
plt.scatter(sepal_length, petal_width, c=color)
plt.xlabel('sepal length')
plt.ylabel('petal width')
plt.savefig("diagram5_1.png")

plt.figure(10)
plt.scatter(petal_width, sepal_length, c=color)
plt.xlabel('petal width')
plt.ylabel('sepal length')
plt.savefig("diagram5_2.png")

plt.figure(11)
plt.scatter(petal_length, petal_width, c=color)
plt.xlabel('petal length')
plt.ylabel('petal width')
plt.savefig("diagram6_1.png")

plt.figure(12)
plt.scatter(petal_width, petal_length, c=color)
plt.xlabel('petal width')
plt.ylabel('petal length')
plt.savefig("diagram6_2.png")
