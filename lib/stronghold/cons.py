
class ProfileMatrix:
    consensus_str = None

    def __init__(self, matrix: list[str], m, n):
        self.matrix = {
            "A": [0 for _ in range(n)], 
            "C": [0 for _ in range(n)], 
            "G": [0 for _ in range(n)], 
            "T": [0 for _ in range(n)], 
        }

        if any(map(lambda s: len(s) != n, matrix)):
            print(list(map(lambda s: len(s), matrix)))
            raise Exception("len of strings doesn't match.")
        
        for ADN_string in matrix:
            for i, nucleotide in enumerate(ADN_string):
                self.matrix[nucleotide][i] += 1

    
    def consensus(self) -> str:
        if self.consensus_str:
            return ''.join(self.consensus_str)

        self.consensus_str = []
        keys = self.matrix.keys()

        for counts in zip(*self.matrix.values()):
            nucleotide, _ = max(zip(keys,counts), key = lambda c: c[1])
            self.consensus_str.append(nucleotide)

        return ''.join(self.consensus_str)

    def __str__(self) -> str:
        repr_str = [self.consensus(),]

        for key, val in self.matrix.items():
            repr_str.append(f"{key}: " + ' '.join(map(lambda c: str(c), val)))

        return '\n'.join(repr_str)


def main(input: str) -> str:
    matrix = []

    for segment in input.split(">")[1:]:
        dna = [l for l in segment.splitlines() if "Rosalind" not in l]
        matrix.append(''.join(dna))

    profile_matrix = ProfileMatrix(matrix, len(matrix), len(matrix[0]))
    return str(profile_matrix)

TEST_INPUT = """\
>Rosalind_1
ATCCAGCT
>Rosalind_2
GGGCAACT
>Rosalind_3
ATGGATCT
>Rosalind_4
AAGCAACC
>Rosalind_5
TTGGAACT
>Rosalind_6
ATGCCATT
>Rosalind_7
ATGGCACT
"""

if __name__ == "__main__":
    print(main(TEST_INPUT))
    

