from constants import CODON_TABLE

def lookup_codon(codon: str) -> str:
    return CODON_TABLE[codon] if codon in CODON_TABLE else ""

def translation(adn: str) -> str:
    seq = []
    for i in range(0,len(adn),3):
        codon = adn[i:i+3]
        aminoacid = lookup_codon(codon)
        
        seq.append(aminoacid)

        if aminoacid == 'X': 
            break

    return ''.join(seq)

def main(input: str) -> str:
    protein = translation(input)
    return protein if protein[-1] != 'X' else protein[:-1]


if __name__ == "__main__":
    test = "AUGGCCAUGGCGCCCAGAACUGAGAUCAAUAGUACCCGUAUUAACGGGUGA"
    print(main(test))
