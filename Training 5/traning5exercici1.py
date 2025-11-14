from time import sleep
def area(): #Definim la funció principal que s'anomena "main""
    print ("Anem a calcular l'àrea d'un quadrat") #Mostra un missatge inicial per a l'usuari i el que es farà
    print("area")
    costat = float(input("Introdueix la longitud del costat del quadrat: ")) # Aquí el que estem fent és crear un input per a que l'usuari introdueixi la longitud del costat del quadrat
    area = costat * costat # Ara calculem l'àrea del quadrat multiplicant el costat per si mateix multiplicant la variable "costat" dues vegades
    print("L'àrea del quadrat és:", int(area)) #Mostra el resultat de l'àrea del quadrat convertit a enter per evitar decimals "int (area)"
def operacions():
    print("Anem a calcular la multiplicació, divisió i resta de dos nombres enters")
    print("operacions")
    num1 = int(input("Introdueix el primer nombre enter: ")) # Aquí el que estem fent és crear un input per a que l'usuari introdueixi el primer nombre enter
    num2 = int(input("Introdueix el segon nombre enter: ")) # Aquí el mateix per al segon número enter
    # Ara calculem la multiplicació, divisió i resta
    multiplicacio = num1 * num2 # Aquí estem calculant la multiplicació de dos nombres enters. Això ho fa calculant els valors que haurem escrit
    divisio = num1 / num2 # Aquí estem calculant la divisió de dos nombres enters. Tot aixo funciona perquè almacenem els valors en les variables num1 i num2
    resta = num1 - num2 # El mateix procediment farem per a la resta dels dos nombres enters
    # Mostrem els resultats a l'usuari 
    print("La multiplicació és:", multiplicacio) #Mostra el resultat de la multiplicació a la consola. Això el que fa es que cride a la variable i doni resultat a la operació que s'ha fet.
    print("La divisió és:", divisio) # El mateix per a la divisió
    print("La resta és:", resta) # I finalment per a la resta
def frase():
    print("frase")
    print("Anem a fer un programa on introduirem per teclat tres paraules i ens retorni una frase completa amb les paraules introduïdes")
    paraula1 = input("Introdueix la primera paraula: ")  # Demana a l'usuari que introdueixi la primera paraula
    paraula2 = input("Introdueix la segona paraula: ")  # El mateix per a la segona paraula
    paraula3 = input("Introdueix la tercera paraula: ")  # El mateix per a la tercera paraula
    frase_completa = paraula1 + " " + paraula2 + " " + paraula3  # Combina les tres paraules en una sola frase
    print("La frase completa és:", frase_completa)  # Mostra la frase completa a l'usuari
def casting():
    print("Anem a crear un programa que faci casting de diferents tipus de dades en aquest cas dos float, que es sumin entre ells i retorni un valor entern")
    print("casting")
    num1 = float(input("Introdueix el primer nombre decimal (float): "))  # Demana a l'usuari que introdueixi el primer nombre decimal
    num2 = float(input("Introdueix el segon nombre decimal (float): "))  # Demana a l'usuari que introdueixi el segon nombre decimal
    suma = num1 + num2  # Suma els dos nombres decimals # Emmagatzema el resultat a la variable "suma"
    print("La suma dels dos nombres decimals és:", suma) # Mostra la suma a l'usuari per pantalla
    print("Ara farem el casting de la suma a un valor enter (int)") # Indica a l'usuari que es farà el casting
    suma_enter = int(suma)  # Converteix la suma a un valor enter
    print("La suma convertida a enter és:", suma_enter)  # Mostra el resultat a l'usuari   
def edats():
        print("edats")
        edat = int(input("Introdueix la teva edat: "))  # Demanem a l'usuari que introdueixi la seva edat
        if edat >= 18:
                print("Ets major d'edat.")  # Mostrem missatge si l'usuari és major d'edat
        else:
                print("Ets menor d'edat.")  # Mostrem missatge si l'usuari és menor d'edat
def numeros():
    print("numeros")
    num1 = float(input("Introdueix el primer nombre: "))  # Demanem el primer nombre
    num2 = float(input("Introdueix el segon nombre: "))   # Demanem el segon nombre
    num3 = float(input("Introdueix el tercer nombre: "))   # Demanem el tercer nombre
    if num1 > num2 and num1 > num3: # amb (if and) podem afegir més d'una condició i ens facilita comparar més valors
        print("El nombre major és:", num1)  # Mostrem el primer nombre si és el major
    elif num2 > num1 and num2 > num3: # Comprovem si el segon nombre és major que els altres dos
        print("El nombre major és:", num2)  # Mostrem el segon nombre si és el major
    else:
        print("El nombre major és:", num3)  # Mostrem el tercer nombre si és el major
def positiuonegatiu():
    print("positiuonegatiu")
    num = float(input("Introdueix un nombre: ")) # Demanem a l'usuari que introdueixi un nombre
    if num >= 0: # Comprovem si el nombre és positiu o negatiu amb la condició (if else)
        print("El nombre és positiu.")
    else: # Si no és positiu, és negatiu
        print("El nombre és negatiu.") # Mostrem missatge si el nombre és negatiu
    
def imprimirnumeros():
    print("imprimirnumeros")
    for i in range(1,201): # Imprimeix els nombres parells entre 1 i 200
        if i % 2 == 0:
            print(i)
    
def nombrenegatiu():
    print("nombrenegatiu")
    nombre_negatiu = False # Variable per rastrejar si hi ha algun nombre negatiu

    for i in range(10): # Bucle per demanar 10 nombres a l'usuari
        nombre = int(input("Introdueix un nombre: ")) # Sol·licita un nombre a l'usuari
        if nombre < 0: # Comprova si el nombre és negatiu
            nombre_negatiu = True # Actualitza la variable si hi ha un nombre negatiu

    if nombre_negatiu: # Comprova si hi ha hagut algun nombre negatiu
        print("Hi havia almenys un nombre negatiu") # Imprimeix el missatge corresponent
    else:   # Si no hi ha hagut cap nombre negatiu
        print("No hi ha cap nombre negatiu") # Imprimeix el missatge corresponent 
def comprovació():
    nota10 = False # Variable per rastrejar si hi ha alguna nota 10
    print("comprovació")
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

while True:
    print("1. Calcula l'àrea d'un quadrat") #Mostra el menú d'opcions a l'usuari
    print("2. Realitza operacions bàsiques amb dos nombres enters") #Mostra el menú d'opcions a l'usuari
    print("3. Crea una frase amb tres paraules") #Mostra el menú d'opcions a l'usuari
    print("4. Fes casting de float a int") #Mostra el menú d'opcions a l'usuari
    print("5. Comprova si ets major o menor d'edat") #Mostra el menú d'opcions a l'usuari
    print("6. Troba el nombre major entre tres nombres") #Mostra el menú d'opcions a l'usuari
    print("7. Comprova si un nombre és positiu o negatiu") #Mostra el menú d'opcions a l'usuari
    print("8. Imprimeix els nombres parells entre 1 i 200") #Mostra el menú d'opcions a l'usuari
    print("9. Comprova si hi ha algun nombre negatiu entre 10 nombres") #Mostra el menú d'opcions a l'usuari
    print("10. Comprova si hi ha alguna nota 10") #Mostra el menú d'opcions a l'usuari
    print("S. Sortir") #Mostra el menú d'opcions a l'usuari
    opcio=input("Selecciona una opció: ") # Demana a l'usuari que seleccioni una opció del menú
    match opcio: # Utilitza una estructura de control "match-case" per gestionar les diferents opcions seleccionades per l'usuari
        case "1": # Crida la funció "area" si l'usuari selecciona l'opció 1
            area() # Crida la funció "area"
            sleep(3) # Pausa de 3 segons abans de tornar al menú principal
        case "2": # Crida la funció "operacions" si l'usuari selecciona l'opció 2
            operacions() # Crida la funció "operacions"
            sleep(3) # Pausa de 3 segons abans de tornar al menú principal
        case "3": # Crida la funció "frase" si l'usuari selecciona l'opció 3
            frase() # Crida la funció "frase"
            sleep(3) # Pausa de 3 segons abans de tornar al menú principal
        case "4": # Crida la funció "casting" si l'usuari selecciona l'opció 4
            casting() # Crida la funció "casting"
            sleep(3) # Pausa de 3 segons abans de tornar al menú principal
        case "5": # Crida la funció "edats" si l'usuari selecciona l'opció 5
            edats() # Crida la funció "edats"
            sleep(3) # Pausa de 3 segons abans de tornar al menú principal
        case "6": # Crida la funció "numeros" si l'usuari selecciona l'opció 6
            numeros() # Crida la funció "numeros"
            sleep(3) # Pausa de 3 segons abans de tornar al menú principal

        case "7": # Crida la funció "positiuonegatiu" si l'usuari selecciona l'opció 7
            positiuonegatiu() # Crida la funció "positiuonegatiu"
            sleep(3) # Pausa de 3 segons abans de tornar al menú principal
        case "8": # Crida la funció "imprimirnumeros" si l'usuari selecciona l'opció 8
            imprimirnumeros() # Crida la funció "imprimirnumeros"
            sleep(3)
        case "9":
            nombrenegatiu() # Crida la funció "nombrenegatiu"
            sleep(3) # Pausa de 3 segons abans de tornar al menú principal
        case "10": 
            comprovació() # Crida la funció "comprovació"
            sleep(3) # Pausa de 3 segons abans de tornar al menú principal
        case "S" | "s": # Si l'usuari selecciona "S" o "s", surt del programa
            print("Sortint del programa...") # Missatge de sortida
            break # Surt del bucle i finalitza el programa
        case _:
            print("Opció no vàlida. Si us plau, selecciona una opció vàlida.") # Missatge d'error per a opcions no vàlides
            sleep(3) # Pausa de 3 segons abans de tornar al menú principal
            


            