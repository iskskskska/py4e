print ("Translating your scores to grades...")
def grade():
    if score <0.0 or score>1.0:
        print ("bad score")
    elif score >= 0.9:
        print("Grade = A")
    elif score >= 0.8:
        print("Grade = B")
    elif score >= 0.7:
        print("Grade = C")
    elif score >= 0.6:
        print ("Grade = D")
    elif score < 0.6:
        print ("Grade = F")
try:
    score= float(input("Enter score:"))
    grade()
except:
    print('bad score')
