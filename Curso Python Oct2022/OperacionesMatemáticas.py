# EJEMPLO 2. Operaciones Matemáticas

# Importar una librería de funciones matemáticas
import math as m

# ENTRADA DE DATOS
# Declarar o crear las variables
número_1 = float(input("Escribe el 1er número: "))
número_2 = float(input("Escribe el 2do número: "))
# Declarar una constante: Elemento que no cambia su valor
PI = 3.1416

# PROCESOS (Cálculos y/o Operaciones Matemáticas y Lógicas)
suma = número_1 + número_2
resta = número_1 - número_2

potencia_1 = número_1 ** número_2
potencia_2 = pow(número_1, número_2)
cuadrado = número_1 ** 2
cubo = pow(número_2, 3)

raíz_cuadrada_1 = m.sqrt(9)
raíz_cuadrada_2 = pow(9, 1/2)
raíz_cúbica = pow(27, 1/3)

módulo_residuo = número_1 % número_2

# SALIDA DE DATOS
print("La suma es =", round(suma, 2)) # Argumentos o Parámetros
print('La suma es = ' + str(suma)) # CONCATENACIÓN: Unión de dos o más textos
# Convertir un tipo de dato en otro tipo de dato (CASTEO)
print(f"La suma es = {suma}") # f: formateo texto

print("La potencia1 es =", potencia_1)
print("La potencia2 es =", potencia_2)
