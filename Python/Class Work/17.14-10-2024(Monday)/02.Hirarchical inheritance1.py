class A:
    l = []
    def funlist(self):
        n = int(input("Enter a number of elements in list : "))
        
        for i in range(n):
            e = int(input("Enter a  Element : "))
            self.l.append(e)            
    
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
        print(f"List: {self.l}")
        print("DESCENDING Order:")
        
        for i in range(len(self.l)):
            for j in range(i+1, len(self.l)):
                if self.l[i] < self.l[j]:
                    self.l[i], self.l[j] = self.l[j], self.l[i]
                    
        print(self.l)
        
oc = C()
ob = B()

oc.funlist()
oc.desc()

ob.asc()