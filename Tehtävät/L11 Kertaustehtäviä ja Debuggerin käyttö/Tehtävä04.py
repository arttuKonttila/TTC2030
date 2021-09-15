i = 0
points = [1, 2, 3, 4, 5]
tulos = 0
while i < len(points):
    points[i] = int(input("Give points:"))
    tulos += points[i]
    i += 1
tulos = tulos - max(points)
tulos = tulos - min(points)
print(tulos)

