Condicionales if
dato=int(input("Ingrese un numero: "))
if dato > 0:
    print("El numero es positivo")
elif dato < 0:
    print("El numero es negativo")
else:
    print("El numero es cero")

#un if
if dato % 2 == 0:
    print("El numero es par")

#if else
if dato % 2 == 0:
    print("El numero es par")
else:
    print("El numero es impar")

# if elif else
if dato > 0:
    print("El numero es positivo")  
elif dato < 0:
    print("El numero es negativo")  
elif dato == 0:
    print("El numero es cero")
else:
    print("El numero es cero")
