class Superclass:
    def __init__(self, name):
        self.name = name

    def display(self):
        print(f"Hello, I am {self.name}")
        

superclass = Superclass("Super's name")

print(f"first {Superclass}")        #class itself & memory location
print(f"second {Superclass.display}")       #function itself & m.l
print(f"third {superclass.display}")        #refered to bound method
print(f"fourth {superclass}")       #different m.l compared to first
#FIXME: superclass() -> not callable
superclass.display()        #great,use function 