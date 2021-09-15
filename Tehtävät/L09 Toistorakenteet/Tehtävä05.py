import random
def lotto():
    i = 0
    lotto_rivi = random.randrange(range(1, 40), 7)
    for num in lotto_rivi:
        print(num, end ="")
lotto()

