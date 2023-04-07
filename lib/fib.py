def naive_fib(n: int, k: int) -> int:
    if n <= 2: return 1
    return naive_fib(n-1,k) + (naive_fib(n-2,k)*k)

def fib_bottom_up(n: int, k: int) -> int:
    prev = curr = 1
    i = 3
    while i <= n:
        prev, curr = curr, (prev*k) + curr
        i += 1

    return curr

def main(input: str) -> str:
    n, k = input.split(" ")
    return str(fib_bottom_up(int(n), int(k)))

if __name__ == "__main__":
    print(main("33 5"))
