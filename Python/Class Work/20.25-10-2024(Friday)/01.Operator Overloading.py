class User:
    def __init__(self,a,b):  #Constructor
        print("Constructor Called!!!!")
        self.a = a
        self.b = b
        
    def __str__(self):
        return f"{self.a,self.b}"
    
    def __add__(self,obj):
        x = self.a + obj.a
        y = self.b + obj.b
        
        return x,y
    
    def __sub__(self,obj):
        x = self.a - obj.a
        y = self.b - obj.b
        
        return x,y
        

obj = User(40,50)
print(obj)

obj1 = User(10,20)
print(obj1)

print(f"Addition : {obj + obj1}")

print(f"Subtraction : {obj - obj1}")