# Calcular el área lateral de un cilindro
import math # Para usar la constante PI
radio = float(input("Radio del cilindro: ")) # Radio de la base
altura_c = float(input("Altura del cilindro: ")) # Altura total
area_lat = 2 * math.pi * radio * altura_c # Fórmula: 2 * PI * r * h
print(f"El área lateral es: {area_lat}") # Salida del cálculo