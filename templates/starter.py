from lib.utils import rosalind_fasta

def main(input: str) -> str:
    """this functions process the input file, pass the data to solver
    function and then return a string with the results
    """
    data = rosalind_fasta.single_string_data(input)

    return ""

if __name__ == "__main__":
    test = ""
    print(main(test))
          
