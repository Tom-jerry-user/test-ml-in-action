import trees
import treePlotter

# #
# myDat, labels = trees.createDataSet()
# # # trees.splitDataSet(myDat, 0, 1)
# # # print(myDat[0])
# # # trees.chooseBestFeatureToSplit(myDat)
# # myTree = trees.createTree(myDat, labels)
# # myTree
# # treePlotter.createPlot1()
# myTree = treePlotter.retrieveTree(0)
# # myTree['no surfacing'][3] = 'maybe'
# # treePlotter.createPlot(myTree)
# trees.classify(myTree, labels, [1, 0])
# trees.classify(myTree, labels, [1, 1])
# trees.storeTree(myTree, 'classifierStorage.txt')
# trees.grabTree('classifierStorage.txt')
fr = open('lenses.txt')
lensens = [inst.strip().split('\t') for inst in fr.readlines()]
lensenslabels = ['age', 'prescript', 'astigmatic', 'tearRate']
lensesTree = trees.createTree(lensens, lensenslabels)
treePlotter.createPlot(lensesTree)
