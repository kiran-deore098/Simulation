import csv
import getopt
from sys import exit


def read_csv(filename):
    with open(filename,'r') as csvfile:
        ls = list(map(lambda x:float(x[0]),csv.reader(csvfile)))
    return ls



def read_text(filename):
    with open(filename,'r') as fp:
        ls = list(map(lambda x:float(x.strip('\n'),fp.readline())))
    return ls

'''
    li=[]
	
    for line in filename.readlines():
        li.append(float(line.strip("\n")))
print(li)'''

def usage():
    print("help menu")
    print("pass interval with -i option")
    print("pass filename with -f option")
    print("-help or -h to display help")
    print("pass distribution with -d option")

def command(sys_arg):
    try:
        opts,args = getopt.getopt(sys_arg,"hi:f:d:")
    except:
        usage()
        exit(-1)
    ret = {}
    for o,p in opts:
        if o == "-i":
            ret["interval"] = int(p)
        if o == "-f":
            ret["filename"] = p
        if o in "-h":
            usage()
        if o in "-d":
            ret["option"] = p
    return ret



