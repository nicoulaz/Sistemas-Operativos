# Convertir moneda local a moneda extranjera
soles = float(input("Cantidad en soles: ")) # Entrada en soles
tipo_cambio = float(input("Tipo de cambio actual: ")) # Valor del dólar
dolares = soles / tipo_cambio # Conversión monetaria
print(f"El equivalente en dólares es: {dolares}") # Resultado