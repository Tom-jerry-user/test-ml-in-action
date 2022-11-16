import kNN
import numpy as np
import matplotlib
import matplotlib.pyplot as plt

# group, labels = kNN.createDataSet()
# t = kNN.classify0([1, 1], group, labels, 3)
# print(t)
# datingDataMat, datingLabels = kNN.file2matrix("datingTestSet2.txt")
# print(datingDataMat, datingLabels)
# fig = plt.figure()
# ax = fig.add_subplot(111)
# ax.scatter(datingDataMat[:, 1], datingDataMat[:, 0], 15.0 * np.array(datingLabels), 15.0 * np.array(datingLabels))
# plt.show()

# normMat, ranges, minVals = kNN.autoNorm(datingDataMat)
# print(normMat)
# kNN.datingClassTest()

# kNN.classifyPerson()
# ivect = kNN.img2vector('testDigits/0_13.txt')
kNN.handwritingClassTest()
