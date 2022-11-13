class bikeshop:

    def __init__(self, n):
        self.stock = n

    def Display(self):
        print("Total stock available: ", self.stock)

    def rent(self, n):
        if n < 0:
            print("Enter the positive value or greater than zero ")
        elif n > self.stock:
            print("Enter the value (less than stock")
        else:
            self.stock = self.stock - n
            print("Total price ", n * 200)
            print("Total bikes available : ", self.stock)


while True:
    ui = int(input('''
        1. Display stocks
        2. rent a bike
        3. Exit       
    
    '''))
    obj = bikeshop(100)
    if ui == 1:
        obj.Display()
    elif ui == 2:
        n = int(input("Enter the number of bike you want to rent "))
        obj.rent(n)
    else:
        print("THANkS FOR USING BIKE RENTAL SYSTEM ")
        break
