"""
Explain method overloading and overriding in python
"""
class A:
    def description(self):
        return "Hello"


class B(A):
    # Here B class overrides the description method of A class
    # def description(self):
    #     return "World"

    def description(self):
        print(super().description())
        return "Python"


def addition(a, b, c=0):
    return a + b + c

addition(2, 3)
addition(1, 2, 3)