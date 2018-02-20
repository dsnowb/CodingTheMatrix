#1.7.1
def my_filter(L, num):
    return [x for x in L if x%num]

#1.7.2
def my_lists(L):
    return [[y+1 for y in range(x)] for x in L]

#1.7.3
def my_function_composition(f,g):
    return {k:g[v] for (k,v) in f.items()} 

#1.7.4
def mySum(L):
    sum = 0
    for x in L:
        sum += x
    return sum

#1.7.5
def myProduct(L):
    prod = 1
    for x in L:
        prod *= x
    return prod

#1.7.6
def myMin(L):
    if not len(L): return 'list is empty'
    min = L[0]
    for x in L:
        if x < min: min = x
    return min

#1.7.7
def myConcat(L):
    str = ''
    for x in L:
        str += x
    return str

#1.7.8
def myUnion(L):
    union = {}
    for x in L:
        union = union | x
    return union

#1.7.12
def transform(a,b,L):
    return [x*a+b for x in L]
