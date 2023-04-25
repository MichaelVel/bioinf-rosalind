def prob_offspring_dominant_phenotype(k:int, m: int, n: int) -> float:
    N = k + m + n

    # p(two heterozygous) 
    p2het = (m/N) * ((m-1)/(N-1)) 
    # p(one heterozygous + one homozygous recessive)
    p_het_hom = (m/N)*(n/(N-1)) + (n/N)*(m/(N-1))
    # p(two homozygous recessive)
    p2hom = (n/N) * ((n-1)/(N-1))

    return 1 - (p2het*(1/4) + p_het_hom*(1/2) + p2hom)

def main(input: str) -> str:
    k,m,n = input.split(" ")
        
    sol = prob_offspring_dominant_phenotype(int(k),int(m),int(n))
    return str(sol)

if __name__ == "__main__":
    input = "28 17 27"
    print(main(input))

