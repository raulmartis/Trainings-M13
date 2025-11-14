def nombrenegatiu():
    nombre_negatiu = False # Variable per rastrejar si hi ha algun nombre negatiu

    for i in range(10): # Bucle per demanar 10 nombres a l'usuari
        nombre = int(input("Introdueix un nombre: ")) # Sol·licita un nombre a l'usuari
    if nombre < 0: # Comprova si el nombre és negatiu
        nombre_negatiu = True # Actualitza la variable si hi ha un nombre negatiu

    if nombre_negatiu: # Comprova si hi ha hagut algun nombre negatiu
        print("Hi havia almenys un nombre negatiu") # Imprimeix el missatge corresponent
    else:   # Si no hi ha hagut cap nombre negatiu
        print("No hi ha cap nombre negatiu") # Imprimeix el missatge corresponent

if __name__ == "__main__":
    nombrenegatiu()
