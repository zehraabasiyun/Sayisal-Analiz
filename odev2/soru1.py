x_alt = 2
x_ust = 4

for i in range(4):
    x = (x_alt + x_ust) / 2

    fonksiyon = x ** 3 - 2 * x ** 2 - 5
    fonksiyon2 = x_alt ** 3 - 2 * x_alt ** 2 - 5

    if fonksiyon * fonksiyon2 < 0:
        x_ust = x
    else:
        x_alt = x

hata = (x_ust - x_alt) / 2 ** (i+1)

print("bulunan kök: ", x)
print(f"f({x}) = {fonksiyon}")
print("hata: ", hata)
print("iterasyon sayısı: ", i + 1)