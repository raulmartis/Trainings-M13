
num1 = float(input("Introdueix el primer nombre: "))  # Demanem el primer nombre
num2 = float(input("Introdueix el segon nombre: "))   # Demanem el segon nombre
num3 = float(input("Introdueix el tercer nombre: "))   # Demanem el tercer nombre
if num1 > num2 and num1 > num3:
    print("El nombre major és:", num1)  # Mostrem el primer nombre si és el major
elif num2 > num1 and num2 > num3:
    print("El nombre major és:", num2)  # Mostrem el segon nombre si és el major
else:
    print("El nombre major és:", num3)  # Mostrem el tercer nombre si és el major
