def raw_solution(adn: str) -> str:
    return adn.replace("T", "U")

def transcription(adn: str) -> str:
    return raw_solution(adn)
    
def main(input: str) -> str:
    return raw_solution(input)


if __name__ == "__main__":
    test = "GATGGAACTTGACTACGTAAATT"
    sol = main(test)
    print(sol)
    
