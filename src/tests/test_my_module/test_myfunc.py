from my_module import MyFuncClass

def test_should_be_1_by_default():
    obj = MyFuncClass()
    assert(obj.get_attribute() == 1)

def test_should_be_n_after_setting_attribute_to_n():
    obj = MyFuncClass()
    obj.set_attribute(2)
    assert(obj.get_attribute() == 2)
