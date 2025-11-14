def comprovació():
    nota10 = False # Variable per rastrejar si hi ha alguna nota 10

    while True: # Bucle infinit fins que l'usuari introdueixi -1 
        nota = int(input("Introdueix una nota (0-10) o -1 per acabar: ")) # Sol·licita una nota a l'usuari
        if nota == -1: #   Condició per sortir del bucle
            break # Sortir del bucle
        if nota == 10: # Comprova si la nota és 10  
            nota10 = True # Actualitza la variable si hi ha una nota 10
        if nota10: # Comprova si hi ha hagut alguna nota 10
            print("Hi ha hagut alguna nota que té un 10") # Imprimeix el missatge corresponent
        else: # Si no hi ha hagut cap nota 10
            print("No hi ha cap 10") # Imprimeix el missatge corresponent

if __name__ == "__main__":
    comprovació()   
