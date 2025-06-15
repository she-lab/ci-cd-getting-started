from src.main import add,sub

def test_add_function():
    assert add(2,3)==5
    assert add(0,0)==0
    assert add(5,5)==10

def test_sub_function():
    assert sub(5,3)==2
    assert sub(0,0)==0
    assert sub(10,5)==5