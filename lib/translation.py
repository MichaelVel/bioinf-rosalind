from .constants import CODON_TABLE 

def lookup_codon(codon: str) -> str:
    return CODON_TABLE[codon]

def translation(adn: str) -> str:
    seq = []
    for i in range(0,len(adn),3):
        codon = adn[i:i+3]
        aminoacid = lookup_codon(codon)
        
        if aminoacid == 'X': break

        seq.append(aminoacid)

    return ''.join(seq)

def main(input: str) -> str:
    return translation(input)


if __name__ == "__main__":
    test = "AUGGCCAUGGCGCCCAGAACUGAGAUCAAUAGUACCCGUAUUAACGGGUGA"
    print(main(test))
