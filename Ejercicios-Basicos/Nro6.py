# Calcular la hipotenusa usando el Teorema de Pitágoras
import math # Importamos math para usar la raíz cuadrada
cateto_a = float(input("Largo del cateto A: ")) # Entrada cateto A
cateto_b = float(input("Largo del cateto B: ")) # Entrada cateto B
hipotenusa = math.sqrt(cateto_a**2 + cateto_b**2) # Fórmula de Pitágoras
print(f"La hipotenusa es: {hipotenusa}") # Resultado final