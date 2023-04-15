if __name__ == "__main__":
    from constants import N_CODONS_PER_AMINOACIDS
else:
    from .constants import N_CODONS_PER_AMINOACIDS


def number_codons(aminoacid: str) -> int:
    return N_CODONS_PER_AMINOACIDS[aminoacid]


def r_translation_m(protein: str, max:int) -> int:
    """ Return the number of different RNA strings from which the 
    protein could have been tranlated modulo max.
    """
    n = 1
    for aminoacid in protein:
        n *= number_codons(aminoacid)
        n %= max

    n = (n*3) % max # stop codon
    
    return n
    ##return prod(number_codons(a) for a in protein)*n_stop % max

def main(input: str) -> str:
    return str(r_translation_m(input.strip(),1_000_000))


if __name__ == "__main__":
    test = "MA"*100000
    print(r_translation_m(test,1_000_000))
