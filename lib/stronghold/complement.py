COMP_TABLE = {"A": "T", "C": "G", "G": "C", "T": "A"}

def raw_solution(adn: str) -> str:
    s_comp = []
    for nucleotid in reversed(adn):
        if nucleotid not in COMP_TABLE: continue
        s_comp.append(COMP_TABLE[nucleotid])
    
    return ''.join(s_comp)

def comprehesion_solution(adn: str) -> str:
    return ''.join(COMP_TABLE[n] for n in reversed(adn) if n in COMP_TABLE)


def main(input: str) -> str:
    return comprehesion_solution(input)


if __name__ == "__main__":
    test = "AAAACCCGGT"
    sol = main(test)
    print(sol)
    
