class b:
    def se(self,age):
        self.age=age
        print(self.age)
class a(b):
    def ce(self,age):
        
        self.age=age 
        print(self.age)

   

obj=a()
obj=b()
obj.age=9
obj.ce(8)

