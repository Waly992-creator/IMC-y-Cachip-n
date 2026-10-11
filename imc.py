"""Calculadora de IMC (índice de masa corporal).

Uso:
    python imc.py <peso_en_kg> <altura_en_metros>
Ejemplo:
    python imc.py 70 1.75
"""
import sys


def clasificar(imc):
    if imc < 18.5:
        return "bajo peso"
    if imc < 25:
        return "peso normal"
    if imc < 30:
        return "sobrepeso"
    return "obesidad"


if len(sys.argv) != 3:
    print("Uso: python imc.py <peso_en_kg> <altura_en_metros>")
    sys.exit(1)

try:
    peso = float(sys.argv[1])
    altura = float(sys.argv[2])
except ValueError:
    print("Error: el peso y la altura deben ser números. Ejemplo: python imc.py 70 1.75")
    sys.exit(1)

if peso <= 0 or altura <= 0:
    print("Error: el peso y la altura deben ser mayores que cero.")
    sys.exit(1)

imc = peso / altura ** 2
print(f"Tu IMC es {imc:.1f}: {clasificar(imc)}.")
