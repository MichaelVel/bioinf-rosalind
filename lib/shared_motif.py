from typing import Iterable

def motif_in_all(motif: str, dna_strings: Iterable[str]) -> bool:
    return all(motif in dna_seq for dna_seq in dna_strings)

def shared_motif(dna_strings: Iterable[str]) -> str:
    short_seq, *comp_seq = sorted(dna_strings, key=len)
    motif = ""

    for i, _ in enumerate(short_seq):
        for j, _ in enumerate(short_seq, start=i):
            c_motif = short_seq[i:j+1]
            if motif_in_all(c_motif, comp_seq) and len(c_motif) > len(motif):
                motif = c_motif

    return motif


def main(input: str) -> str:
    dna_strings = []

    for segment in input.split(">")[1:]:
        dna = [l for l in segment.splitlines() if "Rosalind" not in l]
        dna_strings.append(''.join(dna))

    return shared_motif(dna_strings)

if __name__ == "__main__":
    INPUT_TEST="""\
>Rosalind_1
GATTACA
>Rosalind_2
TAGACCA
>Rosalind_3
ATACA"""

    print(main(INPUT_TEST))


