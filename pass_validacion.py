import re
import hashlib
from getpass import getpass
import secrets

def validar_longitud(password):
    if len(password) > 15:
        return "La contraseña debe tener un maximo de 15 caracteres."
    return None


def validar_mayuscula(password):
    if not re.search(r"[A-Z]", password):
        return "Debe tener una mayúscula."
    return None


def validar_minuscula(password):
    if not re.search(r"[a-z]", password):
        return "Debe tener una minúscula."
    return None


def validar_numero(password):
    if not re.search(r"\d", password):
        return "Debe tener un número."
    return None


def validar_especial(password):
    patron = r"[ñÑ!@#$%^&*(),.?\":{}|<>_\-+=/\\[\];']"
    if not re.search(patron, password):
        return "Debe tener un carácter especial."
    return None

def generar_salt():
    return secrets.token_hex(16)

def encriptar_password(password, salt):
    combinado = password + salt
    return hashlib.sha256(combinado.encode()).hexdigest()


def validar_contra():
    validaciones = [
        validar_longitud,
        validar_mayuscula,
        validar_minuscula,
        validar_numero,
        validar_especial
    ]

    while True:
        password1 = getpass("Ingrese contraseña: ")
        password2 = getpass("Confirme contraseña: ")
        if password1 != password2:
            print("Las contraseñas no coinciden.")
            continue

        for validar in validaciones:
            error = validar(password1)
            if error:
                print(error)
                break
        else:
            salt = generar_salt()
            hash_pw = encriptar_password(password1, salt)
            return hash_pw, salt