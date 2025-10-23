from src.math_operations import add,sub

def test_add():
    assert add(2,3) == 5
    assert add(-1,1)== 0

def test_sub():
    assert sub(6,4)==2 
    assert sub(4,4)==0
    assert sub(10,4)==6 