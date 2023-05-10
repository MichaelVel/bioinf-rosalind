# ROSALIND-CLI

The Rosalind-CLI is a Python package designed to help you solve exercises 
from the [ROSALIND](https://rosalind.info/problems/locations/) project. 
With this tool, you can easily download, manage, test, and submit your 
solutions to Rosalind's bioinformatics challenges directly from the 
command line.

## Installation

The project is build using [poetry](https://python-poetry.org/), to get 
started clone this repository and run

```
poetry install
```

## Usage

Once the package is installed, you can use the `rosalind-cli` command 
to interact with the package.

First of all you would need to create a workspace, run the following command
from anywhere you want to install the workspace:

```
rosalind-cli init example-workspace.
cd example-workspace
```

This command will create a directory with the following structure:

```
example-workspace/
├── config.py
├── data/
├── output/
├── solutions/
├── templates/
│   ├── solution_template.py
│   └── test_template.py
└── tests/
```

Now we are almost ready to start solving the challenges. But before, we first 
need to login to the page, the following command will prompt you to insert your
username and your password:

```
rosalind-cli login
```
If you don't want to login you can always download the challenge data and manually
run your solution with the `run` command, see the command reference below to see
how to do it. 

To start solving exercises you should run the command `create`, for example if you 
want to solve the [dna](https://rosalind.info/problems/dna/) exercise you would 
run:

```
rosalind-cli create dna
tree solutions
solutions/
└── dna.py
```

This command creates a file in the solutions folder with the id name, by default
uses the template `solution_template.py`, but you can create your own templates 
for use in the `create` command. See the  command referece for more information
about this feature.

Every solution should have a function main with the following signature:

```python 
# templates/solution_template.py
def main(input: str) -> str:
    """this functions process the input file, pass the data to solver
    function and then return a string with the results
    """
    data = ""

    return ""
```

Then you could modify the file in solutions to solve the challenge, for example 
a solution for the `dna` exercise could be:

```python
# solutions/dna.py

from collections import Counter

def counter_solution(adn: str) -> str:
    counter = Counter(adn)
    return f"{counter['A']} {counter['C']} {counter['G']} {counter['T']}"
    
def main(input: str) -> str:
    return counter_solution(input)
```

You can test you solution using the command `test`:

```
rosalind-cli test dna
```
This command creates a test file in the tests directory with the example data
from the page exercise. You can extend this file to make more test if you want:

```python
# tests/dna.py
from solutions import dna

class TestClass:
    def test_answer(self):
        """ For some kind of problems the template has some problems, in 
        particular when testing results given in floating point, the test 
        will fail and is necessary to modify the test in the testing 
        directory"""
  
        data: str = "AGCTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGTGGATTAAAAAAAGAGTGTCTGATAGCAGC"
        expected: str = "20 12 17 21"

        result: str = dna.main(data)
        assert expected == result

```

Finally, when your solutions pass the test you can submit your solution: 

```
rosalind-cli submit dna
Congratulations, correct Answer!!       # If your solutions was correct
```

## Command Reference

### `rosalind-cli` 
    #TODO: ## Complete the reference to this command

### `rosalind-cli init [DIRNAME]` 
    #TODO: ## Complete the reference to this command

### `rosalind-cli login` 
    #TODO: ## Complete the reference to this command

### `rosalind-cli create [OPTIONS] <exercise_id>` 
    #TODO: ## Complete the reference to this command

### `rosalind-cli test [OPTIONS] <exercise_id>`
    #TODO: ## Complete the reference to this command

### `rosalind-cli submit [OPTIONS] <exercise_id>`
    #TODO: ## Complete the reference to this command

### `rosalind-cli run [OPTIONS] <exercise_id> <input_file_path>`
    #TODO: ## Complete the reference to this command

### `rosalind-cli get [OPTIONS] <data_source> <input_file_path>`
    #TODO: ## Complete the reference to this command

