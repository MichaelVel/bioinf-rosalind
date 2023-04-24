
# [AA-AA, AA-Aa, AA-aa, Aa-Aa, Aa-aa, aa-aa]
CG_Tuple = tuple[int,int,int,int,int,int]

def expected_offspring(couples_by_gen: CG_Tuple) -> float:
    """Return the expected number of offspring displaying the dominant phenotype
    in the next generation assuming two offspring per couple.
    """
    n = 0.0
    n += sum( x*2 for x in couples_by_gen[:3])
    n += couples_by_gen[3] * 2 * (3/4)
    n += couples_by_gen[4] * 2 * (1/2)

    return n

def main(input: str) -> str:
    couples_by_gen = tuple(int(x) for x in input.split())
    res = expected_offspring(couples_by_gen)
    return str(res)

if __name__ == "__main__":
    input = "1 0 0 1 0 1"
    print(main(input))
