# multiple inheritance
class A : 
    def fun(self):
        print("Class A")
        
class B:
    def fun(self):
        super().fun() # super method (similar to scope resoution operator in c++)
        print("Class B")
        
class C(B,A):
    def fun(self):
        super().fun() 
        print("Class C")

obj = C()

obj.fun()