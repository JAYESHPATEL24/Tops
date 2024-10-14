class A : 
    def fun(self):
        print("Class A")
        
class B(A):
    def fun(self):
        super().fun() # super method (similar to scope resoution operator in c++)
        print("Class B")
        
obj = B()

obj.fun()