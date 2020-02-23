#########################################################################
# author: WAGNER Nicolas                                                #
# date : 11/06/2018 (mm/dd/yyyy)										#
# mail: nicolas.wagner@uca.fr 										    #
# 																		#
# How to run me: "python titanic.py <pathToCsvTitanicFile>"				#
#########################################################################

import sys
import random as rd
from sklearn.neighbors import KNeighborsClassifier

FILE = sys.argv[1]
DELIMITER = ","
SPLITTRAIN = 0.7
NBK = 10

class dataset:

	header = []
	data = []
	classes = []
	className = ""

	def __init__(self, inputPath,delimiter):
		inputFile = open(inputPath,'r')

		"""
			Create the Header
		"""
		self.header = inputFile.readline().replace('\r','').replace('\n','').split(delimiter)
		
		"""
			Create the data
		"""
		for lines in inputFile.readlines():
			line = lines.replace('\n','').replace('\r','').split(delimiter)
			self.data.append(line)

		"""
			Don't forget to close the opened files
		"""
		inputFile.close()

	def getData(self):
		return [[b for b in a ] for a in self.data]

	def getClasses(self):
		return [int(a) for a in self.classes]

	def getDataSize(self):
		return len(self.data)

	def getNbHead(self):
		return len(self.header)

	def printHead(self):
		sys.stdout.write("***** Header *****\n%s\n"%(" | ".join(self.header)))

	def printData(self,nbLines=10):
		sys.stdout.write("***** Data %d first lines *****\n"%(nbLines))
		for i in range(nbLines):
			sys.stdout.write("%s\n"%(" | ".join([str(a) for a in self.data[i]])))

	def printClasses(self,nbLines=10):
		sys.stdout.write("***** Classes %s, %d first lines *****\n"%(self.className, nbLines))
		for i in range(nbLines):
			sys.stdout.write("%s\n"%(str(self.classes[i])))

	def removeFeatures(self,indFeatHead, indFeatData):
		"""
			Remove column in header with indices:
		"""
		self.header = [self.header[i] for i in range(len(self.header)) if i not in indFeatHead]

		"""
			Remove column in data with indices:
		"""
		self.data = [[example[i] for i in range(len(example)) if i not in indFeatData]  for example in self.data]


	def removeMissingValues(self):
		self.data = [example for example in self.data if '' not in example]

	def replaceNominalValues(self,ind,replacement):
		for i in range(len(self.data)):
			self.data[i][ind] = replacement[self.data[i][ind]]

	# def replaceStringToInt(self,inds):
	# 	for i in range(len(self.data)):
	# 		for j in inds:
	# 			self.data[i][j] = int(self.data[i][j])

	def replaceStringToFloat(self):
		for i in range(len(self.data)):
			self.data[i] = [float(a) for a in self.data[i]]

	def exctractClass(self,classInd):
		self.className = self.header.pop(classInd)
		for i in range(len(self.data)):
			self.classes.append(self.data[i][classInd])
			self.data[i] = [self.data[i][j] for j in range(len(self.data[i])) if j != classInd]

	def splitTrainTest(self,pourcTrain=0.7):
		nbTrain = int(pourcTrain*len(self.data))
		listInds = range(len(self.data))
		trainInds = rd.sample(listInds,nbTrain)

		trainData = [self.data[i] for i in range(len(self.data)) if i in trainInds]
		testData = [self.data[i] for i in range(len(self.data)) if i not in trainInds]
		trainClass = [int(self.classes[i]) for i in range(len(self.classes)) if i in trainInds]
		testClass = [int(self.classes[i]) for i in range(len(self.classes)) if i not in trainInds]

		return trainData,trainClass,testData,testClass

	@staticmethod
	def computeresults(pred,real): # Need to be completed
		TPR = {}
		FPR = {}
		listClasses = list(set(real))
		for cla in listClasses:

			nbTP = len([pred[i] for i in range(len(pred)) if pred[i]==cla and pred[i]==real[i]])
			nbRealCla = len([a for a in real if a == cla])
			nbFP = len([pred[i] for i in range(len(pred)) if pred[i]==cla and pred[i]!=real[i]])
			nbRealNotCla = len([a for a in real if a != cla])

			TPR[cla] = float(nbTP)/float(nbRealCla)
			FPR[cla] = float(nbFP)/float(nbRealNotCla)

			sys.stdout.write("Class %d: TPR=%f and FPR=%f\n"%(cla,TPR[cla],FPR[cla]))



"""
	Start running
"""
print "\n *** Readind and precomputing %s ***\n"%(FILE)

# Create the dataset from CSV file titanic
dataset = dataset(FILE,DELIMITER)
# remove the feature we don't need (PassengerId, Name, Ticket and Cabin), you can choose different ones
dataset.removeFeatures([0,3,8,10],[0,3,4,9,11])
# remove examples with missing values
print "size of data before removing missing values: %d"%(dataset.getDataSize())
dataset.removeMissingValues()
print "size of data after removing missing values: %d"%(dataset.getDataSize())
# replace nominal values by a number
dataset.replaceNominalValues(2,{'male':"1",'female':"0"}) #sex
dataset.replaceNominalValues(7,{'S':"1",'C':"0",'Q':"2"}) #embarked
# replace string values by float
dataset.replaceStringToFloat()
# exctract class from data:
dataset.exctractClass(0)
print "\nThe dataset:\n"
dataset.printHead()
dataset.printData()
dataset.printClasses()

print "\n *** Split data set, pourc of train = %f ***"%(SPLITTRAIN)

trainData,trainClass,testData,testClass = dataset.splitTrainTest(SPLITTRAIN)

for k in range(1,NBK):

	print "\n*** KNN classifier, k=%s ***"%(k)

	neigh = KNeighborsClassifier(n_neighbors=k)
	neigh.fit(trainData, trainClass) 

	dataset.computeresults(neigh.predict(testData),testClass)

