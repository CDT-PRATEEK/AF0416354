class A:
    def show(self):
        print("this is show method")

class B(A):
    def demo(self):
        print("this is single inheritance")

class C(A):
    print("this is multilevel inheritance")

class D(B,C):
    print("This is hybrid inheritance")


obj = C()
obj.show()
obj.demo()