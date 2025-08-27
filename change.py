def change():
    expense = 23.75
    money = 100
    vuelto=round((money-expense)*100)
    print("Ingresar gasto:")
    print(expense)
    print("Dinero recibido")
    print(money)
    print("")
    print("Vuelto")
    print("")
    print("Pesos:")
    print(vuelto//100)
    print("Centavos:")
    print(vuelto%100)
change()

