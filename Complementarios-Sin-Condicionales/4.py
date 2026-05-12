# Ejercicio: Calcular el interés simple
capital = float(input("Capital inicial: ")) # Dinero depositado
tasa = float(input("Tasa de interés anual (%): ")) # Porcentaje
tiempo = float(input("Tiempo en años: ")) # Periodo
interes = (capital * tasa * tiempo) / 100 # Fórmula de interés simple
print(f"El interés generado es: {interes}") # Mostrar interés