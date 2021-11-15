import os
import random as rd

lotto_rivi = []
lotto_filename = "lotto.txt"
lotto_file = open(lotto_filename, "w")

# randomly generates a list of 7 unique numbers between 1 and 40
def arvo():
    arvottu_lista = []
    while True:
        rand_int = rd.randint(1, 40)
        # if random number is unique append it to the list
        if(arvottu_lista.count(rand_int) == 0):
            arvottu_lista.append(rand_int)
        # if list contains 7 elements return the list
        if(len(arvottu_lista) == 7):
            return arvottu_lista
            
# writes randomly generated list into a file
def write_file(rand_list):
    for num in rand_list:
        lotto_file.write(str(num) + "\n")


generated_list = arvo()
write_file(generated_list)
lotto_file.close()

