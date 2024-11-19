from ops import divide  # Assuming the functions are in a file called 'your_module.py'

# Test case to check division by zero
def test_divide_by_zero():
    result = divide(10, 0)
    assert result == "Error: Division by zero is undefined", f"Expected 'Error: Division by zero is undefined', but got {result}"
