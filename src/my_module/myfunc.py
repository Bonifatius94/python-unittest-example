"""A class providing a test function"""

class MyFuncClass:
    """A test class"""
    my_attribute: int = 1

    def get_attribute(self):
        """A test function, always returning 1"""
        return self.my_attribute

    def set_attribute(self, new_value: int):
        """A test function, always returning 1"""
        self.my_attribute = new_value
