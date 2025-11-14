def positiuonegatiu():
    num = float(input("Introdueix un nombre: ")) # Demanem a l'usuari que introdueixi un nombre
    if num >= 0: # Comprovem si el nombre és positiu o negatiu amb la condició (if else)
        print("El nombre és positiu.")
    else: # Si no és positiu, és negatiu
        print("El nombre és negatiu.") # Mostrem missatge si el nombre és negatiu

if __name__ == "__main__":
    positiuonegatiu()
