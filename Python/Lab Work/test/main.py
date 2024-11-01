from task import hello

class A:
    def __init__(self):
        self.a = 50
        hello = hello.__get__(self, A)  # Bind the method to the instance
        hello()

obj = A()
