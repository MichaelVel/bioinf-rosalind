from typing import Iterable

def motif_in_all(motif: str, dna_strings: Iterable[str]) -> bool:
    return all(motif in dna_seq for dna_seq in dna_strings)

def common_motif(short_seq: str, comp_seq: Iterable[str] , length: int) -> str | None:
    for i in range(len(short_seq) - length + 1):
        motif = short_seq[i:i+length]
        if motif_in_all(motif, comp_seq): 
            return motif
    return None

def longest_shared_motif(dna_strings: Iterable[str]) -> str:
    short_seq, *comp_seq = sorted(dna_strings, key=len)
    l, r = 0, len(short_seq) + 1

    while l+1 < r:
        mid = (l+r) // 2
        if common_motif(short_seq, comp_seq, mid):
            l=mid
        else:
            r=mid

    lsm = common_motif(short_seq, comp_seq, l)
    return lsm if lsm else ""


def main(input: str) -> str:
    dna_strings = []

    for segment in input.split(">")[1:]:
        dna = [l for l in segment.splitlines() if "Rosalind" not in l]
        dna_strings.append(''.join(dna))

    return longest_shared_motif(dna_strings)

if __name__ == "__main__":
    INPUT_TEST="""\
>Rosalind_1
GATTACA
>Rosalind_2
TAGACCA
>Rosalind_3
ATACA"""

    print(main(INPUT_TEST))


