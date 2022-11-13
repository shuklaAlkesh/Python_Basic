l=[]
while True:
        n= int(input('''
                    1 . Push Element
                    2.  pop Element
                    3.  peek operation
                    4.  display list
                    5.  Exit
                '''))
        if n == 1:
            t= input("Enter the value :-")
            l.append(t)
            print(l)
        elif n == 2:
            if len(l)==0:
                print("Empty list")
            else:
                t = l.pop()
                print(t)
                print(l)
        elif n == 3:
            if len(l) == 0:
                print(l)
            else:
                print("Last element",l[-1])
        elif n == 4:
            print("display stack",l)
        elif n == 5:
               break;
        else:
            print("INVALID OPTION......")



