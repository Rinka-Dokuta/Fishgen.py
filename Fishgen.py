import random

def fishing():
    num = random.randrange(0, 100)
    if num < 33:
        print("you caught a carp!")
        return "carp"
    elif num < 66:
        print("you caught a woodskip!")
        return "woodskip"
    elif num < 99:
        print("you caught a Catfish!")
        return "catfish"
    else:
        print("you caught nothing")
        return "nothing"
    
print(fishing(), "added to your inventory!")
