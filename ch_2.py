class Vec:
    def __init__(self,labels,function):
        self.D = labels
        self.f = function

def scalar_vector_mult(alpha,v):
    return [alpha*el for el in v]

def segment(pt1,pt2):
    return [[(i/100*x)+((1-i/100)*y) for x,y in zip(pt1,pt2)] for i in range(100)]

def zero_vec(D):
    return Vec(D,{d:0 for d in D})

def setitem(v, d, val): v.f[d] = val

def getitem(v, d): return v.f[d] if d in v.f else 0

def scalar_mul(v,alpha):
    return Vec(v.D, {d:val*alpha for d,val in v.f.items()})

def add_vec(u, v):
    return Vec(u.D, {d:getitem(u,d)+getitem(v,d) for d in u.f.keys()})

def neg_vec(v):
    return Vec(v.D, {d:-val for d,val in v.f.items()})

def list_dot(u,v): return sum([ui+vi for ui,vi in zip(u,v)])

def dot_product_list(needle,haystack):
    return [list_dot(needle,haystack[k:len(needle)+k]) for k in range(len(haystack)-len(needle))]

def list2vec(L): return Vec({a for a in range(len(L))},{a:b for a,b in enumerate(L)})

def triangular_solve_n(rowlist,b):
    D = rowlist[0].D
    n = len(D)
    assert D == set(range(n))
    x = zero_vec(D)
    for i in reversed(range(n)):
        x[i] = (b[i] - rowlist[i])/rowlist[i][i]
    return x

def create_voting_dict(strlist):
    vlist = strlist[:]
    for n in range(len(vlist)): vlist[n] = vlist[n].split(' ')[3:-1]
    return {strlist[i].split(' ')[0]:[int(vlist[i][a]) for a in range(len(vlist[i]))] for i in range(len(strlist))}

def create_dems(strlist):
    dems = set()
    for i in range(len(strlist)):
            if strlist[i].split(' ')[1] == 'D': dems.add(strlist[i].split(' ')[0])
    return dems

def policy_compare(sen_a,sen_b,voting_dict):
    return sum([a*b for a,b in zip(voting_dict[sen_a],voting_dict[sen_b])])

def most_similar(sen, voting_dict):
    closest = -1
    cIdx = -1
    for key in voting_dict:
        dot = policy_compare(sen,key,voting_dict)
        if dot > closest and key != sen:
            closest = dot
            cIdx = key
    return cIdx

def least_similar(sen, voting_dict):
    farthest = 1000000000
    cIdx = 10000000000
    for key in voting_dict:
        dot = policy_compare(sen,key,voting_dict)
        if dot < farthest and key != sen:
            farthest = dot
            cIdx = key
    return cIdx

def find_average_similarity(sen, sen_set, voting_dict):
    dot_total = 0
    num_dots = 0
    for other in sen_set:
        if other != sen:
            dot_total += sum([a*b for a,b in zip(voting_dict[sen],voting_dict[other])])
            num_dots += 1
    return dot_total/num_dots

def find_average_record(sen_set, voting_dict):
    avg_record = [0] * [len(a) for a in voting_dict.values()][0]
    for sen in sen_set:
        for i in range(len(avg_record)):
            avg_record[i] += voting_dict[sen][i]
    for i in range(len(avg_record)):
        avg_record[i] /= len(sen_set)

    return avg_record

def bitter_rivals(voting_dict):
    maxUnlike = 1000000000
    for sen1 in voting_dict:
        for sen2 in voting_dict:
            dot = policy_compare(sen1,sen2,voting_dict)
            if dot < maxUnlike:
                maxUnlike = dot
                rivals = {sen1,sen2}
    return rivals
