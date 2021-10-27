#try rakenteella voi napata sen itse kutsuman TypeErrorin ja toteuttaa koodia sen perusteella
def isthiszero(num):
        if(num == 0):
            return True
        elif(type(num) == int or type(num) == float):
            return False
        else:
            raise TypeError
    

try:
    isthiszero("jiijweji")
except TypeError:
    print("Input was not a number")