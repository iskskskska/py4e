list=[]
while True:
    x=input("Enter number:")
    try:
        if x=='done':
            print ("largest number=", max(list))
            print ("smallest number=", min(list))
            break
        y=int(x)
        list.append(y)
    except:
        print('invalid input')
