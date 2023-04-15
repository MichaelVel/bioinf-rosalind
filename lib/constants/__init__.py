from collections import Counter

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

N_CODONS_PER_AMINOACIDS = Counter(CODON_TABLE.values())
