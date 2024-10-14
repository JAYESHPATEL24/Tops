# Hybrid inheritance
class A : 
    def fun(self):
        print("Class A")
        
class B(A):
    def fun(self):
        super().fun() # super method (similar to scope resoution operator in c++)
        print("Class B")
        
class C(A):
    def fun(self):
        super().fun() 
        print("Class C")
        
class D(C,B):
    def fun(self): 
        super().fun()
        print("Class D")

obj = D()

obj.fun()