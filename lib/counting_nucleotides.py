
from typing import Counter


def raw_solution(adn: str) -> str:
    counter = {"A": 0, "C": 0, "G": 0, "T": 0}

    for nucleotid in adn:
        if nucleotid not in counter: continue
        counter[nucleotid] += 1

    return f"{counter['A']} {counter['C']} {counter['G']} {counter['T']}"

def counter_solution(adn: str) -> str:
    counter = Counter(adn)
    return f"{counter['A']} {counter['C']} {counter['G']} {counter['T']}"
    
def main(input: str) -> str:
    return counter_solution(input)


if __name__ == "__main__":
    test = "AGCTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGTGGATTAAAAAAAGAGTGTCTGATAGCAGC"
    sol = main(test)
    print(sol)
    
