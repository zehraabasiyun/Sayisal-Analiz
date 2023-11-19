x_alt = 1
x_ust = 2
n = 0 #iterasyon sayısı

while (x_ust - x_alt) / 2**n > 0.000001: #hata 10^-6 olana kadar devam et
    x = (x_alt + x_ust) / 2
    fonksiyon = x ** 3 + 4 * x ** 2 - 10
    fonksiyon2 = x_alt ** 3 + 4 * x_alt ** 2 - 10

    if fonksiyon * fonksiyon2 < 0:
        x_ust = x
    else:
        x_alt = x
    n += 1

hata = (x_ust - x_alt) / 2 ** n

print("bulunan kök: ", x)
print(f"f({x}) = {fonksiyon}")
print("hata: ", hata)
print("iterasyon sayısı: ", n)