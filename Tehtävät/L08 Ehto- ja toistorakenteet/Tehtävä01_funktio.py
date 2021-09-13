ika = int(input("Syötä ikäsi: "))
def kerro3(ika):
    if ika < 13:
        return "child"
    elif ika > 12 and ika < 20:
        return "teen"
    elif ika > 19 and ika < 66:
        return "adult"
    else:
        return "senior"
output = kerro3(ika)
print(output)