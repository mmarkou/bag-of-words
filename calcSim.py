from gensim import corpora, models, similarities

import getData

class calcSim(object):

    FirstProfileAuthor = getData.getAuthorStemmedPaper(12,458)

    SecondProfileAuthor = getData.getAuthorStemmedPaper(5,458)

    ThirdProfileAuthor = getData.getAuthorStemmedPaper(757,458)

    newPaper = getData.getStemmedPaper(458)

    documents = [FirstProfileAuthor ,SecondProfileAuthor, ThirdProfileAuthor]

    texts = [[word for word in document.lower().split()]
              for document in documents]

    texts = [[word for word in text]
              for text in texts]

    #print(texts)

    dictionary = corpora.Dictionary(texts)
    dictionary.save('C:/data/wofra/code/python/tmp/try04.dict') # store the dictionary, for future reference
    #print(dictionary.token2id)

    corpus = [dictionary.doc2bow(text) for text in texts]
    corpora.MmCorpus.serialize('C:/data/wofra/code/python/tmp/try04.mm', corpus) # store to disk, for later use
    #print(corpus)

    #---------------------------------------------
    query = [newPaper]

    qtexts = [[word for word in document.lower().split()]
              for document in query]

    qtexts = [[word for word in text]
              for text in qtexts]

    qcorpus = [dictionary.doc2bow(text) for text in qtexts]
    corpora.MmCorpus.serialize('C:/data/wofra/code/python/tmp/q.mm', qcorpus) # store to disk, for later use
    #print(qcorpus)
    #---------------------------------------------------------


    #tfidf = models.TfidfModel(corpus)

    #index = similarities.SparseMatrixSimilarity(tfidf[corpus], num_features=len(dictionary))

    #sims = index[tfidf[qcorpus]]
    #print(list(enumerate(sims)))
    index = similarities.docsim.Similarity('C:/data/wofra/code/python/tmp/tst', corpus, num_features=len(dictionary)) # build the index
    similarities = index[qcorpus]
    print similarities

    #corpus2 = corpora.MmCorpus('C:/data/wofra/code/python/tmp/try04.mm')
    #lsi = models.LsiModel(corpus2 , id2word=dictionary, num_topics=len(dictionary))

    #doc = "identifi attract research field scientist prior begin scientif career scientist oblig confront critic issu defin subject area his/her futur research conduct regardless capabl scholar erron select condemn dignifi effort result wast energi time resourc articl attempt identifi research field attract individu best knowledg topic discuss address literatur formal set problem propos solut combin characterist attract research area scholar approach compar statist model reveal popular research area comparison method propos model lead conclus trendi research area suitabl scientist secondari outcom reveal exist scientif field although emerg promis scientist start career"
    #vec_bow = dictionary.doc2bow(doc.lower().split())
    #vec_lsi = lsi[vec_bow] # convert the query to LSI space
    #print(vec_lsi)
