from math import sqrt
import math

'''

max_c :: [integer] -> integer

[1,2,31,23,1,2,3] -> 31

'''

def max_c(collection):
    max_elem = collection[0]
    for i in collection[1:]:
        if i>max_elem:
            max_elem = i
    return max_elem

def min_c(collection):
    min_elem = collection[0]
    for i in collection[1:]:
        if i<min_elem:
            min_elem = i
    return min_elem

def sum_c(collection):
    sum_v=0.0
    for i in collection:
        sum_v=sum_v +float(i)
    return sum_v

def mean_c(collection):
    '''  mean_v=0.0
    count=1
    for i in collection:
        mean_v+=float(i)
        i+=1
    '''
    return sum_c(collection)/float(len(i))
'''

variance = sum(xi-mean)**2/n

'''
def variance_c(collection):
    mean = mean_c(collection)
    variance_v = sum_c(list(map(lambda x:(x-mean)**2,collection)))/n
    return variance_v

def standard_deviation(collection):
    st_v=sqrt(variance_v(collection))
    return st_v


def freq_cal(collection,interval):
    min_v = min_c(collection)
    max_v = max_c(collection)
    step = float(max_v - min_v)/float(interval)
    x_coord=[]
    y_coord=[]
    prev=min_v
    min_v+=step
    while(min_v<=max_v):
        x_coord.append(min_v)
        min_v+=step
    if(collection[-1]==x_coord[-1]):
        x_coord.append(1234345667676)
    for i in x_coord:
        count=0
        for k in collection:
            if(k>=prev and k<i):
                count+=1
        prev=i
        y_coord.append(count)
    return (x_coord,y_coord)

#freq_cal([1,3,1,2,4,5,6,7,1,2,4,7,8],5)

