"""A class providing a test function"""

class MyFuncClass:
    """A test class"""
    my_attribute: int = 1

    def get_attribute(self):
        """A test function for getting the attribute value"""
        return self.my_attribute

    def set_attribute(self, new_value: int):
        """A test function for setting the attribute value"""
        self.my_attribute = new_value
