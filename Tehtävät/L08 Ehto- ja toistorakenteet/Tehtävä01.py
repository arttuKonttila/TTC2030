ika = int(input("Syötä ikäsi: "))
if ika < 13:
    print("child")
elif ika > 12 and ika < 20:
    print("teen")
elif ika > 19 and ika < 66:
    print("adult")
else:
    print("senior")