nombre_negatiu = False

for _ in range(10):
    nombre = int(input("Introdueix un nombre: "))
    if nombre < 0:
        nombre_negatiu = True

if nombre_negatiu:
    print("Hi havia almenys un nombre negatiu")
else:
    print("No hi ha cap nombre negatiu")
7

