from src.math_operations import add, sub

def test_add():
    assert add(2,3) == 5
    assert add(-1, 1) == 0
    
def test_sub():
    assert sub(5, 3) == 2
    assert sub(10, 3) == 7
    assert sub(6, 10) == -4
    assert sub(5, 25) == -20