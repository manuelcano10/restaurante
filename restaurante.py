total = 0
contplate = 0
countdog = 0
counthamburguer = 0
countpoteiro = 0
while True:
    numberpeople = int (input("Ingrese el numero de personas"))
    for i in range(0, numberpeople):
        option = input ("Ingrese plato")
        if option == "hamburguesa":
            total += 10000
            counthamburguer +=1
        elif option == "perro":
            total += 8000
            countdog +=1
        elif option == "salchipapa":
            total += 6000
            countpoteiro +=1
 
            #inside while
            closeprogram = input ("Desea continuar 'Si , 'No'")
            if closeprogram != 'Si':
                break

            #outside while
            tip = input("Desea dejar propinas Si-No")
            if counthamburguer >2 or countdog >2 or countpoteiro >2:
                total = total * 0.95
            if total > 2000:
                total = total * 0.90
            if tip == "Si":
                total = total * 1.10



