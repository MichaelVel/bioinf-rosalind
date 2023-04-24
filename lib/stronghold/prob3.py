from math import comb

def binompdf(n, p, r):
    return  comb(n, r) * p**r * (1-p)**(n - r)

def binomcdf(n, p, r):
    return sum(binompdf(n,p,i) for i in range(r+1))

def probability(k, N):
    """Given two integers k,N return the probability of at least N AaBb 
    organisms will belong to the k-th generation. The root is an organism
    that has a genotype AaBb, every organism mate with a AaBb, and always 
    have 2 childs.
    """

    n = 2**k
    p = 1/4 

    return  1 - binomcdf(n, p, N-1)

if __name__ == "__main__":
    print(probability(2,1))
