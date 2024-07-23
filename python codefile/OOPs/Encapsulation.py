# Access modifiers -> __attribute => private
                      
#                     _attribute => protected


class A:
    name = "abc"   # public attribuTe
    __Age = 21     # private attribuTe

class B(A):
    def show(self):
        print("this is show method", self.name)

obj = B()
obj.show()