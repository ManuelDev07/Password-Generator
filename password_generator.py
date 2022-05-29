#Generador de Contraseñas:
import string
import random

#Se almacenan en una lista todos los caractéres Alfabéticos(minúscula y mayúscula), numéricos y especiales:
alf = string.ascii_letters
numc = string.digits
spc = "!@#$%^&*()"

chars = list(alf + numc + spc)


def generar(chars):
    '''
    Función que agregará de manera aleatoria a una lista una determinada cantidad de 
    caracteres que indicará el usuario, revolverá su contenido y por útlimo mostrará
    la nueva contraseña.
    Parámetros:
    chars: lista que contiene todos los caracteres que podrán formar parte de la contraseña.
    '''
    n = int(input("Ingrese la longitud que quiere para su contraseña: "))

    random.shuffle(chars)
    new_pswrd = []

    for i in range(n):
        char = random.choice(chars)
        new_pswrd.append(char)
    
    random.shuffle(new_pswrd)
    final = "".join(new_pswrd)

    return final

print(generar(chars))
