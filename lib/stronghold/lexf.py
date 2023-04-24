from itertools import product

def lexf(chars: list[str], s: int) -> list[str]:
    return [''.join(p) for p in product(chars, repeat=s)]

def main(input: str) -> str:
    chars, s = input.split('\n', 1)
    answer = lexf(chars.split(), int(s))
    return '\n'.join(answer)

if __name__ == "__main__":
    test = "A C G T\n2"
    print(main(test))
