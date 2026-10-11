"""Cachipún (piedra, papel o tijera) contra el computador.

Uso:
    python cachipun.py <piedra|papel|tijera>
Ejemplo:
    python cachipun.py papel
"""
import random
import sys

OPCIONES = ["piedra", "papel", "tijera"]
GANA_A = {"piedra": "tijera", "papel": "piedra", "tijera": "papel"}

if len(sys.argv) != 2 or sys.argv[1].lower() not in OPCIONES:
    print("Uso: python cachipun.py <piedra|papel|tijera>")
    sys.exit(1)

jugador = sys.argv[1].lower()
computador = random.choice(OPCIONES)

print(f"Tú elegiste {jugador} y el computador eligió {computador}.")
if jugador == computador:
    print("Empate.")
elif GANA_A[jugador] == computador:
    print("¡Ganaste!")
else:
    print("Perdiste. ¡Revancha!")
