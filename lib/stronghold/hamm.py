
def hamming_distance(s: str, t: str) -> int:
    return sum(1 for (s1,t1) in zip(s,t) if s1 != t1)

def main(input: str) -> str:
    s,t = input.splitlines()
        
    if len(s) != len(t):
        raise Exception("Input of different sizes")

    return str(hamming_distance(s,t))

if __name__ == "__main__":
    input = "GAGCCTACTAACGGGAT\nCATCGTAATGACGGCCT"
    print(main(input))

