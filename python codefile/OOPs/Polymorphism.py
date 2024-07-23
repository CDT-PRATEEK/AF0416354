# Polymorphism can be performed by meThod overloading and method overriding.

# Python does not support method overriding

def sum(a,b,c=0):
    print(a+b+c)

sum(10,20,30)
sum(10,20)

# Polymorphism with inheritance:

''' Polymorphism lets us define methods in the child class That have the same name as The meThods in the parenT class
. In inheritance, the child class inheriTs the methods from The parent class . however , it is possible
to modify a meThod in a child class That iT has inheriTed from The parenT clas. this is particularly useful
in cases where the method inherited from parent class doesnt quite fit the child class'''


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
    
