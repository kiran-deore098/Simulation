import sys
import maths as m
from numpy import exp,sqrt

def uniform(data):
    mean,var = m.mean_c(data),m.variance_c(data)
    b = (2*mean+sqrt(12*var))/2
    a = 2*mean-b
    print(b,a)
    return b,a


def exponential(data):
    lamb=(1/m.mean_c(data))
    return lamb

def cdf_of_exp(lamda,x):
    cdf = 1-exp(-lamda*x)
    #print(cdf)
    return cdf

def normal(data):
    return

def log_normal(data):
    return

def poission(data):
    return

def gamma(data):
    return

def weibull(data):
    return 

#print(uniform([1,2,3,4]))
