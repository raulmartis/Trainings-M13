def casting():
    print("Anem a crear un programa que faci casting de diferents tipus de dades en aquest cas dos float, que es sumin entre ells i retorni un valor entern")
    num1 = float(input("Introdueix el primer nombre decimal (float): "))  # Demana a l'usuari que introdueixi el primer nombre decimal
    num2 = float(input("Introdueix el segon nombre decimal (float): "))  # Demana a l'usuari que introdueixi el segon nombre decimal
    suma = num1 + num2  # Suma els dos nombres decimals # Emmagatzema el resultat a la variable "suma"
    print("La suma dels dos nombres decimals és:", suma) # Mostra la suma a l'usuari per pantalla
    print("Ara farem el casting de la suma a un valor enter (int)") # Indica a l'usuari que es farà el casting
    suma_enter = int(suma)  # Converteix la suma a un valor enter
    print("La suma convertida a enter és:", suma_enter)  # Mostra el resultat a l'usuari

if __name__ == "__main__":
    casting()
    
    