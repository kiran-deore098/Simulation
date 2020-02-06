'''
    
    lcg :: (int,int,int,int) -> yield int

'''
def lcg(seed,modulo,increment,multiplier):
    while 1:
        seed = (seed*multiplier+increment)%modulo
        yield seed/modulo
