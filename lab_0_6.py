def dict2list(dct, keylist): return [dct[k] for k in keylist]
def list2dict(L, keylist): return {keylist[i]:L[i] for i in range(len(keylist))}
def listrange2dict(L): return {i:L[i] for i in range(len(L))}

#0.6.6
def makeInverseIndex(strlist):
    invIndex = {}
    strlist = list(enumerate(strlist))
    for line in strlist:
        words = line[1].split()
        for word in words:
            if word in invIndex: invIndex[word].add(line[0] + 1)
            else: invIndex[word] = {line[0] + 1}

    return invIndex
      
#0.6.7
def orSearch(inverseIndex, query):
    results = set({})
    for word in query:
        if word in inverseIndex: results = results | inverseIndex[word]

    return results

#0.6.8
def andSearch(inverseIndex, query):
    results = [];
    for word in query:
        if word in inverseIndex: results.append(inverseIndex[word])
        else: results.append(set())

    finalSet = set()
    if (len(results)):
        finalSet = results[0]
        for x in results:
            finalSet = finalSet & x

    return finalSet
