# kullanicidan sayi alalim
sayi = input("Sayi giriniz: ")

sayi2 = int(sayi)
ters = 0

for x in sayi:
    kalan = sayi2 % 10
    sayi2 = sayi2 - kalan
    sayi2 = sayi2 // 10

    ters = kalan + (ters*10)

if int(sayi) == ters:
    print("{} sayisi Palindrom sayidir.".format(sayi))
else:
    print("{} sayisi palindrom sayi degildir.".format(sayi))

