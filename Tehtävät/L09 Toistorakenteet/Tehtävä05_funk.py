import random
def lotto():
    #ohjelmoi ratkaisusi tähän
    lotto_rivi = []
    string = ""
    for i in range(0,7):
        n = random.randint(1, 40)
        lotto_rivi.append(n)
    for n in lotto_rivi:
        string = string + str(n) + ","
    string = string.rstrip(',')
    # palauta arvottu lottorivi merkkijonona muodossa '1,3,5,10,20,33,39'
    return string