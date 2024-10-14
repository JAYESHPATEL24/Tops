class A:
    l = []
    def funlist(self):
        n = int(input("Enter a number of elements in list : "))
        
        for i in range(n):
            e = int(input("Enter a  Element : "))
            self.l.append(e)    
    
    l1 =  []
    def funlist1(self):
        n = int(input("Enter a number of elements in list : "))
        
        for i in range(n):
            e = int(input("Enter a  Element : "))
            self.l1.append(e)        
            
    
class B(A):
    def asc(self):
        print(f"List: {self.l}")
        print("ASCENDING Order:")
        
        for i in range(len(self.l)):
            for j in range(i+1, len(self.l)):
                if self.l[i] > self.l[j]:
                    self.l[i], self.l[j] = self.l[j], self.l[i]
                    
        print(self.l)  
            
        
class C(A):
    def desc(self):
        print(f"List: {self.l1}")
        print("DESCENDING Order:")
        
        for i in range(len(self.l1)):
            for j in range(i+1, len(self.l1)):
                if self.l1[i] < self.l1[j]:
                    self.l1[i], self.l1[j] = self.l1[j], self.l1[i]
                    
        print(self.l1)
        
        
class D(B,C):
    d = {}
    
    def dictonary(self):
        print(f"list 1 = {self.l}")
        print(f"list 2 = {self.l1}")
        for i in range(len(self.l)):
            self.d[self.l[i]] = self.l1[i]
        print(self.d)
        

obj = D()

obj.funlist()
obj.funlist1()
obj.asc()
obj.desc()
obj.dictonary()