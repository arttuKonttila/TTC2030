import random
lotto_rivi = []
def lotto():
    for i in range(0,7):
        n = random.randint(1, 40)
        lotto_rivi.append(n)
    for n in lotto_rivi:
        printed = []
        printed.append(n)
        print(str(n) + ",", end="")
lotto()

