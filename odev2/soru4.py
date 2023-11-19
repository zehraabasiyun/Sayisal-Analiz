x = 1
e = 2.718281828459045235360287471352662497757247

for i in range(4):
    f_x = 4 * e ** (-0.5 * x) - x
    f_x_turev = -2 * e ** (-0.5 * x) - 1
    x = x - (f_x/f_x_turev)

print("bulunan kök: ", x)
print("iterasyon sayısı: ",i + 1)