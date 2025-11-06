def main():
    print("Anem a fer un programa on introduirem per teclat tres paraules i ens retorni una frase completa amb les paraules introduïdes")
    paraula1 = input("Introdueix la primera paraula: ")  # Demana a l'usuari que introdueixi la primera paraula
    paraula2 = input("Introdueix la segona paraula: ")  # El mateix per a la segona paraula
    paraula3 = input("Introdueix la tercera paraula: ")  # El mateix per a la tercera paraula
    frase_completa = paraula1 + " " + paraula2 + " " + paraula3  # Combina les tres paraules en una sola frase

    print("La frase completa és:", frase_completa)  # Mostra la frase completa a l'usuari

if __name__ == "__main__":
    main()

