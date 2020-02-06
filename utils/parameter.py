import sys
import maths as m

def uniform(data):
    mean,var = m.mean_c(data),m.variance(data)
    b = (2*mean+np.sqrt(12*var))/2
    return b,2*mean-b


def exponential(data):
    lamb=(1/mean_c)
    return lamb

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
