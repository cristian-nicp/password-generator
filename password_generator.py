# -*- coding:utf-8 -*-
import random

message = """   
    ------------Bienvenido/a al generador de contraseñas aleatorias------------
"""


def password_generator():
    uppercase = ['A','B','C','D','E','F','G','H','I','J','K','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    lowercase = ['a','b','c','d','e','f','g','h','i','j','k','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    numbers = ['1','2','3','4','5','6','7','8','9','0']
    symbols = ['!','$','%','&','=','¡','?','¿','*','+','-','_']

    characters = uppercase + lowercase + numbers + symbols# Generamos una lista que sume simbolos, mayus, minus y núm

    password = [] 

    password_len = int(input('Escribe el número del largo de contraseña deseado: '))

    while len(password) < password_len:
        random_character = random.choice(characters)
        password.append(random_character)
    
    password = ''.join(password)# genero un string de mi lista original,todos los caracteres unidos en una sola cadena
    return password


def run():
    print(message)
    password = password_generator()
    print(f'Tu nueva contraseña es: {password}')


if __name__ == "__main__":
    run()