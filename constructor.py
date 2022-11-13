class DemoClass:
    a = 10

    def __init__(self):  # this is used to define constructor
        print("Welcome Alkesh to python programming")

    def show(self):
        print(self.a)

    def show1(self, a, b):
        print(a + b)


obj = DemoClass()
obj.show()
obj.show1(20, 30)
