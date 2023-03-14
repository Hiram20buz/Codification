diccionario_morse = {'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 
                     'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 
                     'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 
                     'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 
                     'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--', 
                     'Z': '--..', '0': '-----', '1': '.----', '2': '..---', 
                     '3': '...--', '4': '....-', '5': '.....', '6': '-....', 
                     '7': '--...', '8': '---..', '9': '----.'}

#cadena = "Hola, este es un mensaje de prueba"
cadena = "Hola este es un mensaje de prueba"
cadena = cadena.upper()

cadena_codificada = ""
for letra in cadena:
    if letra == " ":
        cadena_codificada += "/"
    else:
        cadena_codificada += diccionario_morse[letra] + " "

print(cadena_codificada)
