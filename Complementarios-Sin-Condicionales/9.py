# Ejercicio: Intercambiar el valor de dos variables
a = input("Valor de A: ") # Primera entrada
b = input("Valor de B: ") # Segunda entrada
auxiliar = a # Guardamos A en una caja temporal
a = b # Pasamos el valor de B a A
b = auxiliar # Pasamos el valor temporal (A original) a B
print(f"Ahora A vale: {a} y B vale: {b}") # Mostramos el cambio