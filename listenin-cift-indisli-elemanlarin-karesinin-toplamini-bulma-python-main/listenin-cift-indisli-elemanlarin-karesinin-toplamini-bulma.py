#liste olusturualim
liste = [2,7,5,18,10]

toplam = 0

for x in range(0,len(liste),2):
    print("{}.elemani: {}".format(x,liste[x]))
    toplam += liste[x]**2

print("Sonuc: {}".format(toplam))

