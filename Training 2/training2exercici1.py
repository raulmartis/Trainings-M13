def main(): #Definim la funció principal que s'anomena "main""
    print ("Anem a calcular l'àrea d'un quadrat") #Mostra un missatge inicial per a l'usuari i el que es farà
    costat = float(input("Introdueix la longitud del costat del quadrat: ")) # Aquí el que estem fent és crear un input per a que l'usuari introdueixi la longitud del costat del quadrat
    area = costat * costat # Ara calculem l'àrea del quadrat multiplicant el costat per si mateix multiplicant la variable "costat" dues vegades
    print("L'àrea del quadrat és:", int(area)) #Mostra el resultat de l'àrea del quadrat convertit a enter per evitar decimals "int (area)"
if __name__ == "__main__": # Comprovem si aquest fitxer s'està executant com a programa principal
    main() 

    

