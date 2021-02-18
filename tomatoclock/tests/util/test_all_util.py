import pytest
from util.all_util import is_integer_num
from util.all_util import exit_program


class TestIsIntegerNum:
    def test_input_is_integer(self):
        result = is_integer_num(10)
        assert result == True
        

    def test_input_is_string(self):
        result = is_integer_num("10")
        assert result == False
        
        
    def test_input_is_float_and_decimal_is_zero(self):
        result = is_integer_num(10.0)
        assert result == True
        
        
    def test_input_is_float_and_decimal_not_zero(self):
        result = is_integer_num(10.1)
        assert result == False


def test_exit_program():
    with pytest.raises(SystemExit):
        exit_program()
        
