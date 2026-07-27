"""
APUNTES PYTHON — Módulo 1: básicos (freeCodeCamp)
Ejecutar con:  python 01_basicos.py
Regla: cada concepto = un mini-ejemplo QUE CORRE + nota de una línea.
Si algo te sorprende, escribe POR QUÉ te sorprendió — eso es el apunte de oro.
"""

# --- Variables: no se declara el tipo, Python lo deduce (¡al revés que C!) ---
angulo = 90            # int
voltaje = 3.3          # float
nombre = "JARVIS"      # string

# --- f-strings: la forma moderna de mezclar texto y variables ---
print(f"{nombre} funcionando a {voltaje}V, servo en {angulo} grados")

# --- Listas: como arrays pero flexibles (crecen solas, tipos mezclados) ---
posiciones = [0, 45, 90, 135, 180]
print(posiciones[0])     # primer elemento (índice desde 0, como en C)
print(posiciones[-1])    # ¡índice negativo = desde el final! Esto en C no existe

# --- Bucle for: recorre cosas directamente, sin contador i ---
for pos in posiciones:
    print(f"moviendo servo a {pos}")

# MIS DUDAS / SORPRESAS:
# - (apunta aquí lo que te choque viniendo de MATLAB/ensamblador)


print (" Mi color favorito es ", "el azul", " y el rojo")

##

developer = 'Devin'
#Para ver qué tipo es developer, puedes usar la función type() así:
developer = 'Devin'
print(type(developer)) # <class 'str'>

#Para ver si account_balance es un entero, puedes verificarlo usando la función isinstance() así