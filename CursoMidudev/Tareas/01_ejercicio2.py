# Ejercicio 2: Calculadora Simple
# Pide al usuario dos numeros y una operacion (+,-,*,/)
# Realiza la operacion y muestra el resultado

numero_a = int(input("Ingres un numero: "))
numero_b = int(input(("Ingrese un numero: ")))
operacion = int(
    input("""Ingrese una operacion:
1. Suma
2. Resta
3. Multiplicacion
4. Division
""")
)
if operacion == 1:
    print(f"La suma de los numeros {numero_a} + {numero_b} = {numero_a + numero_b}. ")
elif operacion == 2:
    print(f"La resta de los numeros {numero_a} - {numero_b} = {numero_a - numero_b}")
elif operacion == 3:
    print(
        f"La Multiplicacion de los numeros {numero_a} * {numero_b} = {numero_a * numero_b}."
    )
elif operacion == 4:
    print(
        f"La division de los numeros {numero_a} / {numero_b} = {numero_a / numero_b}. "
    )
else:
    print("Operaicon no valida")
