from translation import lookup_codon, translation
from transcription import transcription 

def reverse_complement(dna: str):
    lookup = {'A':'T', 'T':'A', 'G':'C', 'C':'G'}
    return ''.join([lookup[c] for c in reversed(dna)])

def _find_start_codons(rna: str) -> list[int]:
    idxs = []
    for i in range(len(rna)):
        try:
            codon = rna[i:i+3]
            if lookup_codon(codon) == "M":
                idxs.append(i)
        except KeyError:
            continue

    return idxs

def _get_orfs(rna: str, proteins: set[str]) -> None:
    for i in _find_start_codons(rna):
        protein = translation(rna[i:])
        if protein[-1] == "X":
            proteins.add(protein[:-1])
    

def possible_proteins(dna: str) -> set[str]:
    """Return all the candidate proteins from the open reading frames
    of a given dna strand.
    """
    rna = transcription(dna)
    rna_complement = transcription(reverse_complement(dna))

    proteins= set()

    _get_orfs(rna,proteins)
    _get_orfs(rna_complement,proteins)

    return proteins

def main(input: str) -> str:

    dna = input.split(">")[1]
    dna = ''.join(l for l in dna.splitlines() if "Rosalind" not in l)
    proteins = possible_proteins(dna)
    return '\n'.join(proteins)

if __name__ == "__main__":
    test_input = """\
>Rosalind_99
AGCCATGTAGCTAACTCAGGTTACATGGGGATGACCCCGCGACTTGGATTAGAGTCTCTTTTGGAATAAGCCTG
AATGATCCGAGTAGCATCTCAG
"""
    print(main(test_input))
