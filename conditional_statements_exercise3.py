print ("Translating your scores to grades...")
try:
    score= float(input("Enter score:"))
    if score <0.0:
        print ("bad score")
    elif score == 0.0:
        print ("Grade = F")
    elif score < 0.6:
        print ("Grade = F")
    elif score >= 0.6:
        print ("Grade = D")
    elif score >= 0.7:
        print ("Grade = C")
    elif score >= 0.8:
        print ("Grade = B")
    elif score >= 0.9:
        print ('Grade = A')
    elif score == 1.0:
        print ('Grade = A')
    elif score > 1.0:
        print ("bad score")
except:
    print('bad score')
