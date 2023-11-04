import numpy 

gercekDeger = numpy.cos(numpy.pi / 5)

ilkTerim = numpy.cos(0)
kesmeHatasi1 = numpy.cos(numpy.pi/5) - ilkTerim

ikiTerim = ilkTerim - (numpy.pi / 5)**2 / 2
kesmeHatasi2 = gercekDeger - ikiTerim

print("Gercek Deger: ", gercekDeger)

print("Ilk terim: ", ilkTerim)
print("Ilk terim kesme hatasi: ", kesmeHatasi1)

print("Iki terim: ", ikiTerim)
print("Iki terim kesme hatasi: ", kesmeHatasi2)
