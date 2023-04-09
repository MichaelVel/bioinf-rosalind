
def find_motif(adn: str, motif: str) -> list[int]:
    positions = []

    for i in range(len(adn)-len(motif)+1):
        if adn[i:i+len(motif)] == motif:
            positions.append(i+1)

    return positions

def main(input: str) -> str:
    adn, motif = input.splitlines()
    return ' '.join(map(lambda x: str(x), find_motif(adn,motif)))


if __name__ == "__main__":
    input = "GATATATGCATATACTT\nATAT"
    print(main(input))
