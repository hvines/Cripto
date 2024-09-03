import sys

def cifrar_cesar(texto, corrimiento):
    resultado = ""

    # Iterar sobre cada carácter en el texto
    for char in texto:
        # Comprobar si es una letra mayúscula
        if char.isupper():
            # Aplicar el corrimiento y mantener en el rango de A-Z
            resultado += chr((ord(char) + corrimiento - 65) % 26 + 65)
        # Comprobar si es una letra minúscula
        elif char.islower():
            # Aplicar el corrimiento y mantener en el rango de a-z
            resultado += chr((ord(char) + corrimiento - 97) % 26 + 97)
        else:
            # Si no es una letra, se mantiene sin cambios
            resultado += char

    return resultado

# Capturar los argumentos de la línea de comandos
if len(sys.argv) != 3:
    print("Uso: python3 cesar.py <texto> <corrimiento>")
    sys.exit(1)

# El primer argumento es el texto y el segundo el corrimiento
texto = sys.argv[1]
corrimiento = int(sys.argv[2])

# Cifrar el texto
texto_cifrado = cifrar_cesar(texto, corrimiento)

# Mostrar el resultado
print(texto_cifrado)
