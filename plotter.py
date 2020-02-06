import utils.reader as r
import utils.maths as m
import utils.show as s
import sys

if __name__=='__main__':
    try:
        assert(len(sys.argv)>=2)
    except:
        r.usage()
        sys.exit(-1)
    res = r.command(sys.argv[1:])
    try:
        ls = r.read_csv(res["filename"])
        s.scatter(ls)
        x_coord,y_coord = m.freq_cal(ls,res["interval"])
        s.histogram(x_coord,y_coord,"range","freq")
    except:
        r.usage()
        sys.exit(-1)
    
