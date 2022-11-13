l=[]
while True:
        n= int(input('''
                    1 . push Element in queue
                    2.  pop Element in queue
                    3.  front operation 
                    4.  rear operation
                    5.  display list
                    6.  Exit
                '''))
        if n == 1:
            t= input("Enter the value :-")
            l.append(t)
            print(l)
        elif n == 2:
            if len(l) == 0:
                print("Empty list")
            else:
                del l[0]
                print(l)
        elif n == 3:
            if len(l) == 0:
                print(l)
            else:
                print("front element",l[0])
        elif n == 4:
            if len(l) == 0:
                print("Empty list")
            else:
                print("rear element",l[-1])
        elif n == 5:
                print("display Queue",l)
        elif n == 6:
               break;
        else:
            print("INVALID OPTION......")



