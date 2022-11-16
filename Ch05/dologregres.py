import logRegres

dataarr, labelmat = logRegres.loadDataSet()
print logRegres.gradAscent(dataarr, labelmat)
