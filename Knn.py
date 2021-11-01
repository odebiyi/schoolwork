# Example of kNN implemented from Scratch in Python
# By Jason Brownlee
#http://machinelearningmastery.com/tutorial-to-implement-k-nearest-neighbors-in-python-from-scratch/

import csv
import random
import math
import operator
import matplotlib.pyplot as plt

def loadDataset(filename, split, trainingSet=[] , testSet=[]):
	with open(filename, 'r') as csvfile:
	    lines = csv.reader(csvfile)
	    dataset = list(lines)
	    for x in range(len(dataset)-1):
	        for y in range(4):
	            dataset[x][y] = float(dataset[x][y])
	        if random.random() < split:
	            trainingSet.append(dataset[x])
	        else:
	            testSet.append(dataset[x])


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

def getResponse(neighbors):
	classVotes = {}
	for x in range(len(neighbors)):
		response = neighbors[x][-1]
		if response in classVotes:
			classVotes[response] += 1
		else:
			classVotes[response] = 1
	sortedVotes = sorted(classVotes.items(), key=operator.itemgetter(1), reverse=True)
	return sortedVotes[0][0]

def getAccuracy(testSet, predictions):
	correct = 0
	for x in range(len(testSet)):
		if testSet[x][-1] == predictions[x]:
			correct += 1
	return (correct/float(len(testSet))) * 100.0
	
def main():
	# prepare data
	splits = [0.85,0.8,0.75,0.7,0.65]
	sorted(splits)
	accuracy_vs_splits = []

	for split in splits:

		trainingSet=[]
		testSet=[]
		loadDataset('iris.csv', split, trainingSet, testSet)
		print('Train set: ' + repr(len(trainingSet)))
		print('Test set: ' + repr(len(testSet)))
		# generate predictions
		predictions=[]
		k = 10
		for x in range(len(testSet)):
			neighbors = getNeighbors(trainingSet, testSet[x], k)
			result = getResponse(neighbors)
			predictions.append(result)
			print('> predicted=' + repr(result) + ', actual=' + repr(testSet[x][-1]))
		accuracy_vs_splits.append(getAccuracy(testSet, predictions))
		print('Accuracy: ' + repr(getAccuracy(testSet, predictions)) + '%')
		print('Split: ' + str(split) )
	
	k_values = [x for x in range(5, 55, 5)]

	accuracy_vs_k = []

	for k in k_values:
		split=0.85
		trainingSet=[]
		testSet=[]
		loadDataset('iris.csv', split, trainingSet, testSet)
		print('Train set: ' + repr(len(trainingSet)))
		print('Test set: ' + repr(len(testSet)))
		# generate predictions
		predictions=[]
		
		for x in range(len(testSet)):
			neighbors = getNeighbors(trainingSet, testSet[x], k)
			result = getResponse(neighbors)
			predictions.append(result)
			print('> predicted=' + repr(result) + ', actual=' + repr(testSet[x][-1]))
		accuracy_vs_k.append(getAccuracy(testSet, predictions))
		print('Accuracy: ' + repr(getAccuracy(testSet, predictions)) + '%')
		print('K-value: ' + str(k) )
	plt.figure(1)
	plt.plot(k_values, accuracy_vs_k, 'ro')
	plt.xlabel("K-values")
	plt.ylabel("Accuracy")
	plt.title("K vs Accuracy with split= "+str(split))
	plt.figure(2)
	plt.plot(splits, accuracy_vs_splits)
	plt.xlabel("Splits")
	plt.ylabel("Accuracy")
	plt.title("Split vs Accuracy with K=10")

	plt.show()	
main()
