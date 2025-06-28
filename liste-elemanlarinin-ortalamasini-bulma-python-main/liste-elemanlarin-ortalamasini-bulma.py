#bir liste olusturalim
print("Oncelikle liste olusturun.")

eleman_sayisi = int(input("Listeniz eleman sayisi: "))

liste = []
toplam = 0

for x in range(eleman_sayisi):
    eleman = int(input("{}.elemani gir: ".format(x+1)))
    liste.append(eleman)
    toplam += eleman

print("\n#LISTENIZ#\n{}".format(liste))

print("elemanlarin toplami: {}, Ortalamasi: {}".format(toplam,toplam//eleman_sayisi))

