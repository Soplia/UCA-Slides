import sys
import random as rd
import numpy as np
from sklearn.cluster import DBSCAN
from sklearn import metrics
from sklearn.datasets.samples_generator import make_blobs
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

FILE = "pokemon.csv";
DELIMITER = ","
SPLITTRAIN = 0.7
NBK = 10

#此处为标准化处理
def standar_scaler(points):
    p = StandardScaler().fit_transform(points)
    return p

class dataset:
    header = []
    data = []
    classes = []
    className = ""

    def __init__(self, inputPath, delimiter):
        inputFile = open(inputPath, 'r', encoding='UTF-8')

        """
            Create the Header
        """
        self.header = inputFile.readline().replace('\r', '').replace('\n', '').split(delimiter)

        """
            Create the data
        """
        for lines in inputFile.readlines():
            line = lines.replace('\n', '').replace('\r', '').split(delimiter)
            self.data.append(line)

        """
            Don't forget to close the opened files
        """
        inputFile.close()

    def getData(self):
        return [[b for b in a] for a in self.data]

    def getClasses(self):
        return [int(a) for a in self.classes]

    def getDataSize(self):
        return len(self.data)

    def getNbHead(self):
        return len(self.header)

    def printHead(self):
        sys.stdout.write("***** Header *****\n%s\n" % (" | ".join(self.header)))

    def printData(self, nbLines=10):
        sys.stdout.write("***** Data %d first lines *****\n" % (nbLines))
        for i in range(nbLines):
            sys.stdout.write("%s\n" % (" | ".join([str(a) for a in self.data[i]])))

    def printClasses(self, nbLines=10):
        sys.stdout.write("***** Classes %s, %d first lines *****\n" % (self.className, nbLines))
        for i in range(nbLines):
            sys.stdout.write("%s\n" % (str(self.classes[i])))

    def removeFeatures(self, indFeatHead, indFeatData):
        """
            Remove column in header with indices:
        """
        self.header = [self.header[i] for i in range(len(self.header)) if i not in indFeatHead]

        """
            Remove column in data with indices:
        """
        self.data = [[example[i] for i in range(len(example)) if i not in indFeatData] for example in self.data]

    def removeMissingValues(self):
        self.data = [example for example in self.data if '' not in example]

    def replaceNominalValues(self, ind, replacement):
        for i in range(len(self.data)):
            self.data[i][ind] = replacement[self.data[i][ind]]

    # inds 是要进行整型转换的属性的列值
    def replaceStringToInt(self,inds):
    	for i in range(len(self.data)):
    		for j in inds:
    			self.data[i][j] = int(self.data[i][j])

    #难到说这里的float能够自动进行判断是否能够进行转换
    def replaceStringToFloat(self):
        for i in range(len(self.data)):
            self.data[i] = [float(a) for a in self.data[i]]

    # 将一条记录的类型与数据进行分离，这时候data已经进行了更新
    def exctractClass(self, classInd):
        self.className = self.header.pop(classInd)
        for i in range(len(self.data)):
            self.classes.append(self.data[i][classInd])
            self.data[i] = [self.data[i][j] for j in range(len(self.data[i])) if j != classInd]

    def splitTrainTest(self, pourcTrain=0.7):
        nbTrain = int(pourcTrain * len(self.data))
        listInds = range(len(self.data))
        trainInds = rd.sample(listInds, nbTrain)

        trainData = [self.data[i] for i in range(len(self.data)) if i in trainInds]
        testData = [self.data[i] for i in range(len(self.data)) if i not in trainInds]
        trainClass = [int(self.classes[i]) for i in range(len(self.classes)) if i in trainInds]
        testClass = [int(self.classes[i]) for i in range(len(self.classes)) if i not in trainInds]

        return trainData, trainClass, testData, testClass

    @staticmethod
    def computeresults(pred, real):  # Need to be completed
        TPR = {}
        FPR = {}
        listClasses = list(set(real))
        for cla in listClasses:
            nbTP = len([pred[i] for i in range(len(pred)) if pred[i] == cla and pred[i] == real[i]])
            nbRealCla = len([a for a in real if a == cla])
            nbFP = len([pred[i] for i in range(len(pred)) if pred[i] == cla and pred[i] != real[i]])
            nbRealNotCla = len([a for a in real if a != cla])

            TPR[cla] = float(nbTP) / float(nbRealCla)
            FPR[cla] = float(nbFP) / float(nbRealNotCla)

            sys.stdout.write("Class %d: TPR=%f and FPR=%f\n" % (cla, TPR[cla], FPR[cla]))

    def DisDatabase(self, str):
        print("\n" + str + " The dataset:");
        dataset.printHead()
        dataset.printData()

"""
	Start running
"""
print("*** Readind and precomputing %s ***" % (FILE))
# Create the dataset from CSV file titanic
dataset = dataset(FILE, DELIMITER)

# remove the feature we don't need (Number 0| Name 1| Type_1 2| Type_2 3|
# Generation 11| isLegendary 12| Color 13| hasGender 14| Pr_Male 15| Egg_Group_1 16 | Egg_Group_2 17|
# Body_Style 22)
dataset.removeFeatures([0,1,2,3,11,12,13,14,15,16,17,18,22], [0,1,2,3,11,12,13,14,15,16,17,18,22])
dataset.DisDatabase("After Remove");

# remove examples with missing values ,
print("size of data before removing missing values: %d" % (dataset.getDataSize()))
dataset.removeMissingValues()
print("size of data after removing missing values: %d" % (dataset.getDataSize()))

dataset.replaceStringToFloat();

#转换成numpy array
X = np.array(dataset.data)
#类簇的数量
n_clusters = 5
point = standar_scaler(X)
#现在把数据和对应的分类书放入聚类函数中进行聚类
cls = KMeans(n_clusters).fit(point)
#X中每项所属分类的一个列表
##print("cls.labels:\n",cls.labels_)



#画图
markers = ['^', 'x', 'o', '*', '+']
for i in range(n_clusters):
  members = cls.labels_ == i
  plt.scatter(X[members, 0], X[members, 1], s=60, marker=markers[i], c='b', alpha=0.5)
plt.title(' ')
plt.show()

