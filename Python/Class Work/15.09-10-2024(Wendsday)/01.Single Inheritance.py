class A:
    def fun1(self):
        print("Hello")
        
class B(A):
    def fun2(self):
        print("Beatiful")

obj = B()
obj.fun1()
obj.fun2()