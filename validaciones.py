import re

def validar_numero(cadena):
    patron = r'^(\d+)?\.?\d+$'
    if not cadena or cadena == "0":
        return False
    try:
        num = float(cadena.replace(',', '.'))
    except ValueError:
        return False
    if re.match(patron, cadena.replace(',', '.')):
        return True
    else:
        return False

# Ejemplo de uso:
cadena1 = "25.5"
cadena2 = "25,5"
cadena3 = "asd.35"
cadena4 = "25...0"
cadena5 = "0"
cadena6 = ""

print(validar_numero(cadena1))  # True
print(validar_numero(cadena2))  # True
print(validar_numero(cadena3))  # False
print(validar_numero(cadena4))  # False
print(validar_numero(cadena5))  # False
print(validar_numero(cadena6))  # False
