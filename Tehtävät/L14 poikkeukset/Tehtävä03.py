#try rakenteella voi napata sen itse kutsuman TypeErrorin ja toteuttaa koodia sen perusteella
def isthiszero(num):
        if(num == "0" or num == 0):
            return True
        elif(num != 0 or num != "0"):
            return False
        else:
            raise TypeError
    

try:
    isthiszero("jiijweji")
except TypeError:
    print("Input was not a number")