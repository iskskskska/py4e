print ("Computing for your Pay...")
try:
    hours = int(input("Enter number of hours:"))
    rate = int(input("Enter rate:"))
    if hours <= 40:
        print (hours*rate)
    elif hours >40:
        print (400+((hours-40)*(rate*1.5)))
except:
    print('Error, please enter numeric input')
