#没有应用到现在的数据集上
import sys
import random as rd
import numpy as np
from sklearn.cluster import DBSCAN
from sklearn import metrics
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler

FILE = "pokemon.csv";
DELIMITER = ","

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
            # self.data[i] = [self.data[i][j] for j in range(len(self.data[i])) if j != classInd]

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

def jiangzao(labels):
    # 标签中的簇数，忽略噪声（如果存在）
    clusters = len(set(labels)) - (1 if -1 in labels else 0)
    return clusters

#此处为标准化处理
def standar_scaler(points):
    p = StandardScaler().fit_transform(points)
    return p

class DBScan (object):
    """
    the class inherits from object, encapsulate the  DBscan algorithm
    """
    def __init__(self, p, l_stauts):

        self.point = p
        self.labels_stats = l_stauts

        # clf = DBSCAN(eps=0.3, min_samples=10).fit(X)
        # 其中clf就是最终的分类器，而X是输入数据。
        # eps：点之间的间距，大于这个间距的就不算一个簇了。
        # min_samples：可以算作核心点的高密度区域的最少点个数。
        self.db = DBSCAN(eps=0.2, min_samples=10).fit(self.point)

    def draw(self):
        coreSamplesMask = np.zeros_like(self.db.labels_, dtype=bool)
        coreSamplesMask[self.db.core_sample_indices_] = True
        labels = self.db.labels_
        nclusters = jiangzao(labels)

        # 输出模型评估参数，包括估计的集群数量、均匀度、完整性、V度量、
        # 调整后的兰德指数、调整后的互信息量、轮廓系数
        print('Estimated number of clusters: %d' % nclusters)
        # print("Homogeneity: %0.3f" % metrics.homogeneity_score(self.labels_stats, labels))
        # print("Completeness: %0.3f" % metrics.completeness_score(self.labels_stats, labels))
        # print("V-measure: %0.3f" % metrics.v_measure_score(self.labels_stats, labels))
        # print("Adjusted Rand Index: %0.3f"
        #       % metrics.adjusted_rand_score(self.labels_stats, labels))
        # print("Adjusted Mutual Information: %0.3f"
        #       % metrics.adjusted_mutual_info_score(self.labels_stats, labels))
        # print("Silhouette Coefficient: %0.3f"
        #       % metrics.silhouette_score(self.point, labels))
        # 绘制结果
        # 黑色被移除，并被标记为噪音。
        unique_labels = set(labels)
        colors = plt.cm.Spectral(np.linspace(0, 1, len(unique_labels)))
        for k, col in zip(unique_labels, colors):
            if k == -1:
                # 黑色用于噪声
                col = 'k'

            classMemberMask = (labels == k)

            # 画出分类点集
            xy = self.point[classMemberMask & coreSamplesMask]
            plt.plot(xy[:, 0], xy[:, 1], 'o', markerfacecolor=col,
                     markeredgecolor='k', markersize=6)

            # 画出噪声点集
            xy = self.point[classMemberMask & ~coreSamplesMask]
            plt.plot(xy[:, 0], xy[:, 1], 'o', markerfacecolor=col,
                     markeredgecolor='k', markersize=3)
        # 加标题，显示分类数
        plt.title('Estimated number of clusters: %d' % nclusters)
        plt.show()

"""
	Start running
"""
print("*** Readind and precomputing %s ***" % (FILE))
dataset = dataset(FILE, DELIMITER)

labelsTrue = dataset.exctractClass(2)
labelsTrue = dataset.classes
# remove the feature we don't need (Number 0| Name 1| Type_1 2| Type_2 3|
# Generation 11| isLegendary 12| Color 13| hasGender 14| Pr_Male 15| Egg_Group_1 16 | Egg_Group_2 17|
# Body_Style 22)
dataset.removeFeatures([0,1,2,3,11,12,13,14,15,16,17,18,22], [0,1,2,3,11,12,13,14,15,16,17,18,22])
dataset.DisDatabase("After Remove");

print("size of data before removing missing values: %d" % (dataset.getDataSize()))
dataset.removeMissingValues()
print("size of data after removing missing values: %d" % (dataset.getDataSize()))
dataset.replaceStringToFloat();

#转换成numpy array
X = np.array(dataset.data)
point = standar_scaler(X)
# 这里的labelsTrue应该是什么呢
db = DBScan(X, labelsTrue)
db.draw()
