# Ejercicio: Convertir horas, minutos y segundos a segundos totales
h = int(input("Horas: ")) # Ingreso de horas
m = int(input("Minutos: ")) # Ingreso de minutos
s = int(input("Segundos: ")) # Ingreso de segundos
total_segundos = (h * 3600) + (m * 60) + s # Conversión total
print(f"El total de segundos es: {total_segundos}") # Salida de datos