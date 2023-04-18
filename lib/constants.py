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

START_CODON = "AUG"

MONOISOTOPIC_MASS_TABLE = {
    "A":   71.03711,    # Alanine       (Ala)
    "C":   103.00919,   # Cysteine      (Cys)
    "D":   115.02694,   # Aspartic acid (Asp)
    "E":   129.04259,   # Glutamic acid (Glu)
    "F":   147.06841,   # Phenylalanine (Phe)
    "G":   57.02146,    # Glycine       (Gly)
    "H":   137.05891,   # Histidine     (His)
    "I":   113.08406,   # Isoleucine    (Ile)
    "K":   128.09496,   # Lysine        (Lys)
    "L":   113.08406,   # Leucine       (Leu)
    "M":   131.04049,   # Methionine    (Met)
    "N":   114.04293,   # Asparagine    (Asn)
    "P":   97.05276,    # Proline       (Pro)
    "Q":   128.05858,   # Glutamine     (Gln)
    "R":   156.10111,   # Arginine      (Arg)
    "S":   87.03203,    # Serine        (Ser)
    "T":   101.04768,   # Threonine     (Thr)
    "V":   99.06841,    # Valine        (Val)
    "W":   186.07931,   # Tryptophan    (Trp)
    "Y":   163.06333,   # Tyrosine      (Tyr)
}   
