# Ejercicio: Calcular el volumen de una esfera
import math # Importamos math para usar PI y potencias
radio = float(input("Radio de la esfera: ")) # Entrada del radio
volumen = (4/3) * math.pi * (radio ** 3) # Fórmula: (4/3)*PI*r^3
print(f"El volumen de la esfera es: {volumen}") # Resultado final