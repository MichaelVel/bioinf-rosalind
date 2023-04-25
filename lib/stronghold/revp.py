from orf import reverse_complement

Sites = list[tuple[int,int]]

def is_reverse_palindrome(dna:str) -> bool:
    return dna == reverse_complement(dna)

def _search_in_range(dna: str, start: int, to: int, sites: Sites) -> None:
    for i in range(4,to+1):
        if is_reverse_palindrome(dna[start:start+i]):
            sites.append((start+1,i))

def restriction_sites(dna: str) -> Sites:
    sites = []
    for i, _ in enumerate(dna):
        window_size = min(12, len(dna)-i)
        _search_in_range(dna, i, window_size, sites)

    return sites

def main(input: str) -> str:
    dna = input.split(">")[1]
    dna = ''.join(l for l in dna.splitlines() if "Rosalind" not in l)
    
    return '\n'.join(f"{p} {l}" for p, l in restriction_sites(dna))


if __name__ == "__main__":
    test = ">Rosalind_24\nTCAATGCATGCGGGTCTATATGCAT"
    print(main(test))
