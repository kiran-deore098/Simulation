import maths as m
import parameter as p


def chi_uniform_test(data,size,interval):
    aj,oj = m.freq_cal(data,interval)
    (b,a) = p.uniform(data)
    ej = size/interval
    v = []
    for i in oj:
        v.append((ej-i)**2/ej)
    return (aj,oj,ej,v,m.sum_c(v))

def chi_expon_test(data,size,interval):
    ai,oj = m.freq_cal(data,interval)
    lamda = p.exponential(data)
    min1 = m.min_c(data)
    ej = []
    v = []
    for i in ai:
        ej.append(p.cdf_of_exp(lamda,i)-p.cdf_of_exp(lamda,min1)) # F(x)|a<= x <= b = F(b) - F(a)
        min1 = i
    for i in zip(ej,oj):
        v.append((i[0]-i[1])**2/i[0])
    return (ai,oj,ej,v,m.sum_c(v))

def print_tab(aj,oj,ej,v,chi):
    n = len(aj)
    if(type(ej)!=type([])):
        ej = [ej for i in range(n)]
    print("{}           {}          {}          {}".format('aj','oj','ej','(ej-oj)^2/ej'))
    print("-------------------------------------------")
    for i in range(n):
        print("{}       {}      {}      {}".format(aj[i],oj[i],ej[i],v[i]))
    print("-------------------------------------------")
    print("Chi Square Value : {}".format(chi))
