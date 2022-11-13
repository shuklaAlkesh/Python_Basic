# inheritance process
class A:
    def ClassA(self):
        print("Class A is called ")


class B:
    def ClassB(self):
        print("Class B is called ")


class C(A,B):
    def ClassC(self):
        print("Class B is called ")


obj = C()
obj.ClassA()
obj.ClassB()
obj.ClassC()