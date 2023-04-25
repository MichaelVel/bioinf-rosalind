from re import template


def rabbit_population(n: int, m: int) -> int:
    """ Calculate the total number of pair of rabbits that will remain afer the n-th 
    month if all rabbits live for m months."""
    generations = [1,1]
    count = 2

    while count < n:
        deaths_on_n = 0
        
        if count in (m,m+1):
            deaths_on_n = 1
        if count > m+1:
            deaths_on_n = generations[-(m+1)]
        
        generations.append(generations[-2] + generations[-1] - deaths_on_n)
        count += 1

    print(generations)
    return generations[n-1]

def main(input: str) -> str:
    n, m = input.split(" ")
    return str(rabbit_population(int(n), int(m)))

if __name__ == "__main__":
    print(main("89 19"))
