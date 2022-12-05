import logRegres

dataarr, labelmat = logRegres.loadDataSet()
# # print logRegres.gradAscent(dataarr, labelmat)
# weights = logRegres.gradAscent(dataarr, labelmat)
# logRegres.plotBestFit(weights.getA())
logRegres.multiTest()