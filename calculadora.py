n1 = float(input("Introduce tu primer numero: "))
n2 = float(input("Introduce tu segundo numero: "))

opcion = 0
while True:
    print("""
    1) Sumar los dos numeros
    2) Restar los dos numeros 
    3) Multiplicar los dos numeros 
    4) Dividir los dos numeros
    5) Cambiar los numeros elejidos
    6) Cerrar calculadora
    """)

    opcion = int(input("Elegir una opcion: "))

    if opcion == 1:
        print (" ")
        print("RESULTADO: La suma de" ,n1,"+",n2,"es igual",n1+n2)
    elif opcion == 2:
        print (" ")
        print("RESULTADO: La resta de" ,n1,"-",n2,"es igual",n1-n2)
    elif opcion == 3:
        print (" ")
        print("RESULTADO: La multiplicacion de" ,n1,"*",n2,"es igual",n1*n2)
    elif opcion == 4:
        print (" ")
        print("RESULTADO: La division de" ,n1,"/",n2,"es igual",n1/n2)
    elif opcion == 5:
        n1 = float(input("Introduce tu primer numero: "))
        n2 = float(input("Introduce tu segundo numero: "))
    elif opcion == 6:
            break
    else:
            print("Opcion Incorrecta")

