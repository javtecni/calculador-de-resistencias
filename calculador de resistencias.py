#Este es un pequeño programa hecho por mi, Javier Alberto Hernandez, es original no es copiado, es un poco extenso debido a que solo use lo que conocia en el momento, lo que son las condicionales.
print ("""                     ***************calculador de resistencias*************""")
print("""              


                        NOTA: por favor ingresar los colores en minusculas


""")



#variables de primera franja
compara = "cafe"
compara2 = "rojo"
compara3 = "naranja"
compara4 = "amarillo"
compara5 = "verde"
compara6 = "azul"
compara7 = "violeta"
compara8 = "gris"
compara9 = "blanco"
compara10 = "negro"
tolerancia5 = "dorado"
tolerancia10 = "plateado"


primerdato = print("ingrese color primera franja")


primera_franja = input()

while primera_franja != compara and primera_franja != compara2 and primera_franja != compara3 and primera_franja != compara4 and primera_franja != compara5 and primera_franja != compara6 and primera_franja != compara7 and primera_franja != compara8 and primera_franja != compara9 and primera_franja != compara10:
    print("error ingrese el color correcto")
    primerdato = print("ingrese color primera franja")
    primera_franja = input()

    if primera_franja == compara and primera_franja == compara2 and primera_franja == compara3 and primera_franja == compara4 and primera_franja == compara5 and primera_franja == compara6 and primera_franja == compara7 and primera_franja == compara8 and primera_franja == compara9 and primera_franja == compara10:
       print

if primera_franja == compara: 
   primera_franja = 1
if primera_franja == compara2: 
   primera_franja = 2
if primera_franja == compara3: 
   primera_franja = 3
if primera_franja == compara4: 
   primera_franja = 4
if primera_franja == compara5: 
   primera_franja = 5
if primera_franja == compara6: 
   primera_franja = 6
if primera_franja == compara7: 
   primera_franja = 7
if primera_franja == compara8: 
   primera_franja = 8
if primera_franja == compara9: 
   primera_franja = 9
if primera_franja == compara10: 
   primera_franja = 0
 
        
primerdato = print("ingrese color segunda franja")
segunda_franja = input()

while segunda_franja != compara and segunda_franja != compara2 and segunda_franja != compara3 and segunda_franja != compara4 and segunda_franja != compara5 and segunda_franja != compara6 and segunda_franja != compara7 and segunda_franja != compara8 and segunda_franja != compara9 and segunda_franja != compara10:
    print("error ingrese el color correcto")
    primerdato = print("ingrese color segunda franja")
    segunda_franja = input()

    if segunda_franja == compara and segunda_franja == compara2 and segunda_franja == compara3 and segunda_franja == compara4 and segunda_franja == compara5 and segunda_franja == compara6 and segunda_franja == compara7 and segunda_franja == compara8 and segunda_franja == compara9 and segunda_franja == compara10:
       print

if segunda_franja == compara: 
   segunda_franja = 1
if segunda_franja == compara2: 
   segunda_franja = 2
if segunda_franja == compara3: 
   segunda_franja = 3
if segunda_franja == compara4: 
   segunda_franja = 4
if segunda_franja == compara5: 
   segunda_franja = 5
if segunda_franja == compara6: 
   segunda_franja = 6
if segunda_franja == compara7: 
   segunda_franja = 7
if segunda_franja == compara8: 
   segunda_franja = 8
if segunda_franja == compara9: 
   segunda_franja = 9
if segunda_franja == compara10: 
   segunda_franja = 0

primerdato = print("ingrese color tercera franja")
tercera_franja = input()

while tercera_franja != compara and tercera_franja != compara2 and tercera_franja != compara3 and tercera_franja != compara4 and tercera_franja != compara5 and tercera_franja != compara6 and tercera_franja != compara7 and tercera_franja != compara8 and tercera_franja != compara9 and tercera_franja != compara10:
    print("error ingrese el color correcto")
    primerdato = print("ingrese color segunda franja")
    tercera_franja = input()

    if tercera_franja == compara and tercera_franja == compara2 and tercera_franja == compara3 and tercera_franja == compara4 and tercera_franja == compara5 and tercera_franja == compara6 and tercera_franja == compara7 and tercera_franja == compara8 and tercera_franja == compara9 and tercera_franja == compara10:
       print

if (tercera_franja == compara):
    tercera_franja = 10 * (primera_franja * 10 + segunda_franja)
    
if (tercera_franja == compara2):
    tercera_franja = 100 * (primera_franja * 10 + segunda_franja)

if (tercera_franja == compara3):
    tercera_franja = 1000 * (primera_franja * 10 + segunda_franja)
    
if (tercera_franja == compara4):
    tercera_franja = 10000 * (primera_franja * 10 + segunda_franja)

if (tercera_franja == compara5):
    tercera_franja = 100000 * (primera_franja * 10 + segunda_franja)
    
if (tercera_franja == compara6):
    tercera_franja = 1000000 * (primera_franja * 10 + segunda_franja)
    
if (tercera_franja == compara7):
    tercera_franja = 10000000 * (primera_franja * 10 + segunda_franja)
    
if (tercera_franja == compara8):
    tercera_franja = 100000000 * (primera_franja * 10 + segunda_franja)

if (tercera_franja == compara9):
    tercera_franja = 1000000000 * (primera_franja * 10 + segunda_franja)
    
if (tercera_franja == compara10):
    tercera_franja = 1 * (primera_franja * 10 + segunda_franja)


primerdato = print("ingrese color franja de tolerancia")
cuarta_franja = input()

while cuarta_franja != tolerancia5 and cuarta_franja != tolerancia10:
    print("error ingrese el color correcto")
    primerdato = print("ingrese color franja de tolerancia")
    cuarta_franja = input()

    if cuarta_franja == tolerancia5 and cuarta_franja == tolerancia10:
       print

if cuarta_franja == tolerancia5: 
   cuarta_franja = "5% +/-"
if cuarta_franja == tolerancia10: 
   cuarta_franja = "10% +/-"
    
    
print ("el valor de la resistencia es " , tercera_franja , "ohm" ,"con una tolerancia del", cuarta_franja )
print()
print()

    

      









