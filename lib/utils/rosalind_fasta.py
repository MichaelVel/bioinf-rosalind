
def single_string_data(input: str) -> str:
    """ Takes a multiline input string in Rosalind FASTA format, and return 
    only the data. 

    Example: 
    
    >Rosalind_6404
    CCTG
    TCCC

    Output:
    CCTGTCC

    """
    data = input.split(">")[1]
    data  = ''.join(l for l in data.splitlines() if "Rosalind" not in l)
    return data

def list_data(input: str) -> list[str]:
    """ Takes a multiline input string in Rosalind FASTA format, and return 
    a list with the data. 

    Example: 
    
    >Rosalind_6404
    CCTG
    TCCC
    >Rosalind_2507
    AATCTCCC

    Output:
    [CCTGTCC, AATCTCCC]

    """
    data = []
    for s in input.split(">")[1:]:
        data.append(''.join(x for x in s.split() if "Rosalind" not in x))
    return data


def map_data(input: str) -> dict[str,str]:
    """ Takes a multiline input string in Rosalind FASTA format, and return 
    a dict with the name, and data. 

    Example: 
    
    >Rosalind_6404
    CCTG
    TCCC
    >Rosalind_2507
    AATCTCC

    Output:
    {
      Rosalind_6404: CCTGTCC, 
      Rosalind_2507: AATCTCC,
    }

    """
    parsed = {}

    for entry in input.split(">")[1:]:
        name, dna = "", ""

        for line in entry.splitlines():
            if line.startswith("Rosalind"):
                name = line
            else:
                dna += line

        parsed[name] = dna

    return parsed
