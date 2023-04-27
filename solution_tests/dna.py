from lib.stronghold import dna

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
