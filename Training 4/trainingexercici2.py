Qualificació = [0,1,2,3,4,5,6,7,8,9,10,-1]
for Nota in Qualificació:
    if Nota > -1:
         print(Nota)
    if Nota == -1:
        print(Nota)
        break #Lleva el bucle
if max(Qualificació) == 10:
    print("Hi ha hagut alguna nota que te un 10.")
else:
    print("No hi ha cap 10.")
