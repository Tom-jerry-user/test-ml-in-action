import feedparser

import bayes

# listposts, listclasses = bayes.loadDataSet()
# myvocablist = bayes.createVocabList(listposts)
# bayes.setOfWords2Vec(myvocablist, listposts[0])
# bayes.setOfWords2Vec(myvocablist, listposts[3])
# trainmat = []
# for postindoc in listposts:
#     trainmat.append(bayes.setOfWords2Vec(myvocablist, postindoc))
# p0v, p1v, pab = bayes.trainNB0(trainmat, listclasses)
# p0v1, p1v1, pab1 = bayes.trainNB1(trainmat, listclasses)
# bayes.testingNB()
# for i in range(10):
#     print "no.%d" % (i + 1), bayes.spamTest()
ny = feedparser.parse('https://newyork.craigslist.org/stp/index.rss')
sf = feedparser.parse('https://sfbay.craigslist.org/stp/index.rss')
vocablist, psf, pny = bayes.localWords(ny, sf)
