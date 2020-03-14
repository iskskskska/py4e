x = int(input("Enter a number:"))
list=[]
while True:
    x=input("Enter number:")
    try:
        if x=='done':
            print("sum=",sum(list))
            count=0
            for thing in list:
                count=count+1
            print("count=",count)
            print("average=",(sum(list)/count))
            break
        y=int(x)
        list.append(y)
    except:
        print('invalid input')
print('yehey!')
