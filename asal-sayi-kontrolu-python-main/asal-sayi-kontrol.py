# kullanicidan sayi alalim

sayi = int(input("Sayi gir: "))

durum = 0

if sayi > 2:
    for x in range(2,sayi):
        if (sayi % x) == 0:
            durum = 1
            break

    if durum == 1:
        print("{} sayiniz asal degildir. Cunku {} sayisina tam bolunur.".format(sayi,x))
    else:
        print("{} sayiniz asaldir.".format(sayi))
elif sayi == 2:
    print("2 Sayisi asaldir.")
else:
    print("{} sayisi asal degildir.".format(sayi))
