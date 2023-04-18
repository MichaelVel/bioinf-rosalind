from constants import MONOISOTOPIC_MASS_TABLE as table

def aminoacid_weight(aminoacid: str) -> float:
    return table[aminoacid] if aminoacid in table else 0.0

def protein_weight(peptide: str) -> float:
    return sum(aminoacid_weight(a) for a in peptide)

def main(input: str) -> str:
    return str(protein_weight(input))


if __name__ == "__main__":
    test = "SKADYEK"
    print(main(test))
