enim = input("Anna etunimi: ")
snim = input("Anna sukunimi: ")
i = 0
a = len(snim) - 1
while i < len(enim):
    print(enim[0], end ="")
    i += 1
    if i == len(enim):
        print(" ", end="")
        for p in snim:
            print(snim[a], end ="")
            a -= 1