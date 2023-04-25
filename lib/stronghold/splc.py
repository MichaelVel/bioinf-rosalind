from translation import translation
from transcription import transcription

# I don't quite like the solution yet, but don't want to expend to much time 
# changing it, for now i will leave as is, but maybe in the future should
# try another aproach.
def _splicing_simple_solution(p: str, intr: list[str]) -> str:
    for intron in sorted(intr):
        p = p.replace(intron, "", 1)
    return p

def splicing(precursor: str, introns: list[str]) -> str:
    """
    take a RNA string an a list of introns and return the concatenate
    exons.
    """
    return _splicing_simple_solution(precursor, introns)


def main(input: str) -> str:
    data = []
    for s in input.split(">")[1:]:
        data.append(''.join(x for x in s.split() if "Rosalind" not in x))

    precursor, *introns = [transcription(dna) for dna in data]
    m_RNA = splicing(precursor, introns)          

    return translation(m_RNA)[:-1]

if __name__ == "__main__":
    test = """\
>Rosalind_10
ATGGTCTACATAGCTGACAAACAGCACGTAGCAATCGGTCGAATCTCGAGAGGCATATGGT
CACATGATCGGTCGAGCGTGTTTCAAAGTTTGCGCCTAG
>Rosalind_12
ATCGGTCGAA
>Rosalind_15
ATCGGTCGAGCGTGT
"""
    
    result = main(test)
    expected = "MVYIADKQHVASREAYGHMFKVCA"
    print(main(test))
    print("result == expected: ", result == expected)
    
    
