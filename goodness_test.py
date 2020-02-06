import utils.reader as r
import utils.chi_square_test as c
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
        if res["option"]=="u":
            res = c.chi_uniform_test(ls,len(ls),res["interval"])
            '''print("Ai")
            for i in res[0]:
                print(i)
            print()
            print("Observed Freq")
            for i in res[1]:
                print(i)
            print()
            print("Chi Square Value ")
            print(res[-1])'''
            c.print_tab(res[0],res[1],res[3],res[4])
        elif res["option"] == "e":
            res = c.chi_expon_test(ls,len(ls),res["interval"])
            '''print("Ai")
            for i in res[0]:
                print(i)
            print()
            print("Observed Freq")
            for i in res[1]:
                print(i)
            print()
            print("Chi Square Value ")
            print(res[-1])'''
            c.print_tab(res[0],res[1],res[2],res[3],res[4])
        else:
            usage()

        #print_tab(res[0],res[1],res[3])
        #print("Chi Square Value : {}".format(res[4]))
    except:
        r.usage()
        sys.exit(-1)
    
