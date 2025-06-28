#sayiyi alalim
sayi = int(input("Sayi giriniz: "))
# unutmayın!!! input ile alinan degerler string olduğundan cast islemi ile int tipine dönüştürülmesi gerekmetdir.

#girilen sayinin modunu alarak kalani buluyoruz
kalan = sayi % 2

#sayini 2'e bolumunda kalan 0 ise sayimiz cif degilse tektir.
if sayi < 0:
    print("pozitif sayi giriniz.")
else:
    if kalan == 0:
        print("{} sayiniz cifttir.".format(sayi))
    else:
        print("{} sayiniz tektir.".format(sayi))

