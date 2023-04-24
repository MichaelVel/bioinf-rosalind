from typing import Counter


TEST_DATA = ( 
"""\
>Rosalind_6404
CCTGCGGAAGATCGGCACTAGAATAGCCAGAACCGTTTCTCTGAGGCTTCCGGCCTTCCC
TCCCACTAATAATTCTGAGG
>Rosalind_5959
CCATCGGTAGCGCATCCTTAGTCCAATTAAGTCCCTATCCAGGCGCTCCGCCGAAGGTCT
ATATCCATTTGTCAGCAGACACGC
>Rosalind_0808
CCACCCTCGTGGTATGGCTAGGCATTCAGGAACCGGAGAACGCTTCAGACCAGCCCGGAC
TGGGAACCTGCGGGCAGTAGGTGGAAT
""")

def fasta_parse(input: str) -> dict[str,str]:
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

def gc(dna: str) -> float:
    frequencies = Counter(dna)
    return (frequencies["C"] + frequencies["G"]) / frequencies.total()

def max_str(data: dict[str,str]) -> tuple[str,float]:
    max_record = ("",0.0)

    for name, dna in data.items():
        gc_freq = gc(dna)
        if gc_freq > max_record[1]:
            max_record = (name,gc_freq)

    return max_record

def main(input: str) -> str:
    parsed = fasta_parse(input)
    max_record = max_str(parsed)

    return f"{max_record[0]}\n{max_record[1]*100}"

if __name__ == "__main__":
    print(main(TEST_DATA))
