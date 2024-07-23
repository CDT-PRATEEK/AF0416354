# Polymorphism can be performed by meThod overloading and method overriding.

# Python does not support method overriding

def sum(a,b,c=0):
    print(a+b+c)

sum(10,20,30)
sum(10,20)

# Polymorphism with inheritance:

''' Polymorphism lets us define methods in the child class that have the same name as the methods in the parent class.
In inheritance, the child class inherits the methods from the parent class. However, it is possible to modify a method
in a child class that it has inherited from the parent class. This is particularly useful in cases where the method inherited
from the parent class doesn't quite fit the child class. In such cases, we re-implement the method in the child class. 
This process of re-implementing a method in the child class is known as Method Overriding.'''


class Bird:
    def intro(self):
        print("There are many types of birds")
    def flight(self):
        print("most birds can fly but some cannot")

class Sparrow(Bird):    # reimplementing Bird method to overload it by inheritance
    def flight(self):
        print("i can fly")

class Ostrich(Bird):
    def flight(self):
        print("I cannot fly")

obj = Sparrow()
obj.flight()

obj1 = Ostrich()
obj1.flight()
    
