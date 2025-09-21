def change():
    expense = float(input("Ingresar gasto:\n"))
    money = float(input("Dinero recibido\n"))
    vuelto = int(round((money - expense) * 100))

    print("")
    print("Vuelto")
    print("")
    print("Pesos:")
    print(vuelto // 100)
    print("Centavos:")
    print(vuelto % 100)

