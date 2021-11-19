from my_module import MyFuncClass

def test_should_be_1():
    obj = MyFuncClass()
    assert(obj.get_attribute() == 1)
