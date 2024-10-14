class A:
    def fun(self):
        a = int(input("Enter a number : "))
        b = int(input("Enter a number : "))
        self.a = a
        self.b = b    
    
class B(A):
    def add(self):
        print(f"Addition : {self.a+self.b}")
        
class C(A):
    def sub(self):
        print(f"Subtraction : {self.a-self.b}")
        
oc = C()
ob = B()

oc.fun()
oc.sub()

ob.fun()
ob.add()