#没有调通
#没有应用到现在的数据集上
# Agglomerative Hierarchical Clustering(AHC)

import sys
import pylab as pl
import random as rd
import numpy as np
from operator import itemgetter
from collections import OrderedDict,Counter
from sklearn.preprocessing import StandardScaler

#此处为标准化处理
def standar_scaler(points):
    p = StandardScaler().fit_transform(points)
    return p

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
  def replaceStringToInt(self, inds):
    for i in range(len(self.data)):
      for j in inds:
        self.data[i][j] = int(self.data[i][j])

  # 难到说这里的float能够自动进行判断是否能够进行转换
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

points = np.array(dataset.data)
points = standar_scaler(points)
print("len of points: " , len(points));

# 初始时每个点指派为单独一簇
groups = [idx for idx in range(len(points))]
# 点与点之间的距离的字典
disP2P = {}

# 计算每个点对之间的距离
for idx1,point1 in enumerate(points):
  for idx2,point2 in enumerate(points):
    if (idx1 < idx2):
      # distance = pow(abs(point1[0]-point2[0]),2) + pow(abs(point1[1]-point2[1]),2)
      distance = 0;
      # 这个地方进行了改变
      for i in range(len(point1)):
        distance += pow(abs(point1[i]-point2[i]),2)
        disP2P[str(idx1)+"#"+str(idx2)] = distance

# 按距离降序将各个点对排序
print("len of dic: " , len(disP2P));
# disP2P = OrderedDict(sorted(disP2P.iteritems(), key=itemgetter(1), reverse=True))
# 安第二个参数进行排序
disP2P = OrderedDict(sorted(disP2P.items(), key=itemgetter(1), reverse=True))
# 当前有的簇个数
groupNum = len(groups)
# 过分合并会带入噪音点的影响，当簇数减为finalGroupNum时，停止合并
finalGroupNum = int(groupNum*0.1)
while groupNum > finalGroupNum:
  # 选取下一个距离最近的点对
  twopoins,distance = disP2P.popitem()
  pointA = int(twopoins.split('#')[0])
  pointB = int(twopoins.split('#')[1])
  pointAGroup = groups[pointA]
  pointBGroup = groups[pointB]
  # 当前距离最近两点若不在同一簇中，将点B所在的簇中的所有点合并到点A所在的簇中，此时当前簇数减1
  if(pointAGroup != pointBGroup):
    for idx in range(len(groups)):
      if groups[idx] == pointBGroup:
        groups[idx] = pointAGroup
    groupNum -= 1

# 选取规模最大的3个簇，其他簇归为噪音点
wantGroupNum = 3
finalGroup = Counter(groups).most_common(wantGroupNum)
finalGroup = [onecount[0] for onecount in finalGroup]
dropPoints = [points[idx] for idx in range(len(points)) if groups[idx] not in finalGroup]
# 打印规模最大的3个簇中的点
group1 = [points[idx] for idx in range(len(points)) if groups[idx]==finalGroup[0]]
group2 = [points[idx] for idx in range(len(points)) if groups[idx]==finalGroup[1]]
group3 = [points[idx] for idx in range(len(points)) if groups[idx]==finalGroup[2]]

pl.plot([eachpoint[0] for eachpoint in group1], [eachpoint[1] for eachpoint in group1], 'or')
pl.plot([eachpoint[0] for eachpoint in group2], [eachpoint[1] for eachpoint in group2], 'oy')
pl.plot([eachpoint[0] for eachpoint in group3], [eachpoint[1] for eachpoint in group3], 'og')
# 打印噪音点，黑色
pl.plot([eachpoint[0] for eachpoint in dropPoints], [eachpoint[1] for eachpoint in dropPoints], 'ok')
pl.show()
