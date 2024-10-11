class A:
    _a = int(input("Enter a Number : "))
    def fun1(self):
        print("This is Fun1..!!!")
        
class B:
    _b = int(input("Enter a Number : "))
    def fun2(self):
        print("This is fun2!!!")
        
class C(A,B):
    def merger(self):
        print(f"Addition : {self._a + self._b}")
        
obj = C()
obj.fun1()
obj.fun2()
obj.merger()