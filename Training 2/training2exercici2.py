def operacions():
    print("Anem a calcular la multiplicació, divisió i resta de dos nombres enters")
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
if __name__ == "__main__":
    operacions()
    
