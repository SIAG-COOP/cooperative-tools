#!/usr/bin/env python3

"""
Herramienta base cooperativa
Parte del proyecto SIAG COOP

Este script sirve como plantilla para futuras herramientas cooperativas.
Incluye:
- función principal
- parámetros opcionales
- estructura preparada para ampliación
"""

import argparse

def greet_coop(name="Cooperativa"):
    print(f"🤝 ¡Hola, {name}! Esta herramienta está lista para colaborar.")

def main():
    parser = argparse.ArgumentParser(description="Herramienta base cooperativa.")
    parser.add_argument("-n", "--name", help="Nombre de la cooperativa", default="Cooperativa")
    args = parser.parse_args()

    greet_coop(args.name)

if __name__ == "__main__":
    main()
