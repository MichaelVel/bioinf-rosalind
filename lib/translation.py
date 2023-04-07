from itertools import islice

CODON_TABLE = { # 'X' represent stop codon
    "UUU": "F",  "UCU": "S",  "UAU": "Y",  "UGU": "C",
    "UUC": "F",  "UCC": "S",  "UAC": "Y",  "UGC": "C",
    "UUA": "L",  "UCA": "S",  "UAA": "X",  "UGA": "X",
    "UUG": "L",  "UCG": "S",  "UAG": "X",  "UGG": "W",
    
    "CUU": "L",  "CCU": "P",  "CAU": "H",  "CGU": "R",
    "CUC": "L",  "CCC": "P",  "CAC": "H",  "CGC": "R",
    "CUA": "L",  "CCA": "P",  "CAA": "Q",  "CGA": "R",
    "CUG": "L",  "CCG": "P",  "CAG": "Q",  "CGG": "R",

    "AUU": "I",  "ACU": "T",  "AAU": "N",  "AGU": "S",
    "AUC": "I",  "ACC": "T",  "AAC": "N",  "AGC": "S",
    "AUA": "I",  "ACA": "T",  "AAA": "K",  "AGA": "R",
    "AUG": "M",  "ACG": "T",  "AAG": "K",  "AGG": "R",

    "GUU": "V",  "GCU": "A",  "GAU": "D",  "GGU": "G",
    "GUC": "V",  "GCC": "A",  "GAC": "D",  "GGC": "G",
    "GUA": "V",  "GCA": "A",  "GAA": "E",  "GGA": "G",
    "GUG": "V",  "GCG": "A",  "GAG": "E",  "GGG": "G",
}

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
