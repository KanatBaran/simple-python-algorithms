# listemiz
liste = [34, 26, 38, 5, 42, 11, 3, 15, 28, 12]

for x in range(len(liste)):
    for y in range(len(liste)):
        if liste[x] < liste[y]:

            data = liste[y]
            liste[y] = liste[x]
            liste[x] = data


for z in liste:
    print(z)
