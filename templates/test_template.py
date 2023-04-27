from $module import $file

class TestClass:
    def test_answer(self):
        """ For some kind of problems the template has some problems, in 
        particular when testing results given in floating point, the test 
        will fail and is necessary to modify the test in the testing 
        directory"""
  
        data: str = "$test_data"
        expected: str = "$expected"

        result: str = ${file}.main(data)
        assert expected == result
