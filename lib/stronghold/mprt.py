from re import compile
from typing import Pattern

N_glycosilation_motif = compile("N[^P][ST][^P]")

def find_motif(motif: Pattern, peptide: str) -> list[int] | None:
    result = []
    i = 0
    while i < len(peptide):
        m  = motif.search(peptide,i)
        if not m: break

        result.append(m.start()+1)
        i = m.start()+1

    return result  if result else None

def main(input: str) -> str:
    names = []
    peptides = []

    for segment in input.split(">")[1:]:
        names.append(segment.split("|")[1])

        peptide = [l for l in segment.splitlines() if "sp" not in l]
        peptides.append(''.join(peptide))
    
    res: list[str] = []
    for name, peptide in zip(names,peptides):
        motif_positions = find_motif(N_glycosilation_motif,peptide)
        if not motif_positions:
            continue
        
        pos = ' '.join(str(i) for i in motif_positions)
        res.append(f"{name}\n{pos}\n")
    
    return ''.join(res)

if __name__ == "__main__":
    test_string = "NASAAAAAANASA"
    print(find_motif(N_glycosilation_motif,test_string))
