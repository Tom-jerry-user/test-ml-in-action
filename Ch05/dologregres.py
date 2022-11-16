import logRegres

dataarr, labelmat = logRegres.loadDataSet()
logRegres.gradAscent(dataarr, labelmat)
