#try rakenteella voi napata sen itse kutsuman TypeErrorin ja toteuttaa koodia sen perusteella
def isfloat(num):
    try:
        float(num)
        return True
    except ValueError:
        return False

def isint(num):
    try:
        int(num)
        return True
    except ValueError:
        return False

def isthiszero(num):
    if(isfloat(num) == True or isint(num) == True):
        if(isfloat(num) == True):
            num = float(num)
            if(num == 0):
                return True
            elif(num != 0):
                return False
        elif(isint(num) == True):
            num = int(num)
            if(num == 0):
                return True
            elif(num != 0):
                return False 
    else:
        raise TypeError
    
try:
    print(isthiszero(input("Gibe number: ")))
except TypeError:
    print("Input was not a number")