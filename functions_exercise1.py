print ("Computing for your Pay...")
def computepay():
    if hours <= 40:
        print ("Pay=", hours*rate)
    elif hours >40:
        print ("Pay=", 400+((hours-40)*(rate*1.5)))
hours = int(input("Enter number of hours:"))
rate = int(input("Enter rate:"))

computepay()
