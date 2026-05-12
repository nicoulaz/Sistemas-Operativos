# Ejercicio: Distancia entre dos puntos en un plano 3D (Página 100)
import math
# Pedimos coordenadas del primer punto
x1 = float(input("x1: "))
y1 = float(input("y1: "))
z1 = float(input("z1: "))
# Pedimos coordenadas del segundo punto
x2 = float(input("x2: "))
y2 = float(input("y2: "))
z2 = float(input("z2: "))
# Fórmula de distancia euclidiana en 3D
dist = math.sqrt((x2-x1)**2 + (y2-y1)**2 + (z2-z1)**2)
print(f"La distancia entre los puntos es: {dist}") # Salida