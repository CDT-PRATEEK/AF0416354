# self is a reference to the instance of the class from which it is called

class Student:
    name = "xyz"            # attributes
    age = 0
    def study(self):        # method
        print("Study 3 hours")
        self.sleep()

    def sleep(self):
        print("Sleep 1 hour")

obj = Student()             # object
obj.study()