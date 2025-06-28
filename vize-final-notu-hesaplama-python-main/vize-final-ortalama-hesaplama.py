#vize notu
vize_notu = float(input("Vize notunuzu girin: "))

#final notu
final_notu = float(input("Final notunuzu girin: "))

vize_notu = vize_notu * 0.40
final_notu = final_notu * 0.60
ort = vize_notu+final_notu

print("Ortalamaniz: {}".format(ort))

if ort >= 60.0:
    print("Tebrikler geçtiniz!")
elif ort >= 55:
    print("Sartli geçtiniz.")
else:
    print("Maalesef kaldiniz.")