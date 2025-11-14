def edats():
        edat = int(input("Introdueix la teva edat: "))  # Demanem a l'usuari que introdueixi la seva edat
        if edat >= 18:
                print("Ets major d'edat.")  # Mostrem missatge si l'usuari és major d'edat
    
        else:
                print("Ets menor d'edat.")  # Mostrem missatge si l'usuari és menor d'edat
if __name__ == "__main__":
    edats()

