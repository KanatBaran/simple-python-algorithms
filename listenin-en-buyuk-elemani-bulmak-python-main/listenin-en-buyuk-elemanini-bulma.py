#liste olsuturalim
liste = [34,26,38,5,42,11,3,15,28,12]

buyuk = liste[0]

for x in liste:
    if x > buyuk:
        buyuk = x

print("En buyuk eleman: {}".format(buyuk))