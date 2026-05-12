# Ejercicio: Calcular la velocidad final de un objeto
# Fórmula: Vf = Vi + a * t
vi = float(input("Velocidad inicial (m/s): ")) # Entrada Vi
a = float(input("Aceleración (m/s^2): ")) # Entrada aceleración
t = float(input("Tiempo (s): ")) # Entrada tiempo
vf = vi + (a * t) # Cálculo de velocidad final
print(f"La velocidad final es: {vf} m/s") # Resultado