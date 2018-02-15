
# coding: utf-8

# In[3]:


# Load CSV
import numpy
filename = 'pima-indians-diabetes.data.csv'
raw_data = open(filename, 'rt')
data = numpy.loadtxt(raw_data, delimiter=",")
print(data.shape)


# In[6]:


# Load CSV
import numpy
filename = 'glass.data.csv'
raw_data = open(filename, 'rt')
trainingset = numpy.loadtxt(raw_data, delimiter=",")
print(data.shape)



# In[10]:


import math
def euclideanDistance(instance1, instance2, length):
	distance = 0
	for x in range(length):
		distance += pow((instance1[x] - instance2[x]), 2)
	return math.sqrt(distance)


# In[12]:





# In[13]:


def getNeighbors(trainingSet, testInstance, k):
	distances = []
	length = len(testInstance)-1
	for x in range(len(trainingSet)):
		dist = euclideanDistance(testInstance, trainingSet[x], length)
		distances.append((trainingSet[x], dist))
	distances.sort(key=operator.itemgetter(1))
	neighbors = []
	for x in range(k):
		neighbors.append(distances[x][0])
	return neighbors


# In[29]:


import csv
import random
import math
import operator

import numpy


 
 
def euclideanDistance(instance1, instance2, length):
	distance = 0
	for x in range(length):
		distance += pow((instance1[x] - instance2[x]), 2)
	return math.sqrt(distance)
 
def getNeighbors(trainingSet, testInstance, k):
	distances = []
	length = len(testInstance)-1
	for x in range(len(trainingSet)):
		dist = euclideanDistance(testInstance, trainingSet[x], length)
		distances.append((trainingSet[x], dist))
	distances.sort(key=operator.itemgetter(1))
	neighbors = []
	for x in range(k):
		neighbors.append(distances[x][0])
	return neighbors

def main():
	# prepare data
    filename = 'glass.data.csv'
    raw_data = open(filename, 'rt')
    trainingSet = numpy.loadtxt(raw_data, delimiter=",")
    testSet=[13,1.51589,12.88,3.43,1.40,73.28,0.69,8.05,0.00,0.24,1]
    # generate predictions
    predictions=[]
    k = 5
    for x in range(len(trainingset)):
        neighbors = getNeighbors(trainingSet[x], testSet, k)
    
main()

