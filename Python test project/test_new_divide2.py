from ops import divide
import pytest

def test_division_zero_division_error():  
    with pytest.raises(ZeroDivisionError) as excinfo:  
        divide(1, 0)  
    assert str(excinfo.value) == "Division by zero is not allowed!" 
