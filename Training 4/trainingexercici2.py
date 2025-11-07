nota10 = False

while True:
    nota = int(input("Introdueix una nota (0-10) o -1 per acabar: "))
    if nota == -1:
        break
    if nota == 10:
        nota10 = True

if nota10:
    print("Hi ha hagut alguna nota que té un 10")
else:
    print("No hi ha cap 10")

