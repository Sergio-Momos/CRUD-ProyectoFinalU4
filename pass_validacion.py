import re
import sys
import hashlib
import secrets

# msvcrt solo existe en Windows; termios/tty solo en sistemas POSIX
# (Linux/Mac). Ambos son librerías ESTÁNDAR de Python (no requieren
# 'pip install'), por lo que no se agrega ninguna dependencia externa.
if sys.platform == "win32":
    import msvcrt
else:
    import termios
    import tty


def leer_tecla():
    """
    Lee un solo carácter desde el teclado sin necesidad de presionar Enter,
    de forma multiplataforma. Retorna el carácter como bytes, o b'' si
    fue una tecla especial que debe ignorarse (flechas, F1-F12, etc.).
    """
    if sys.platform == "win32":
        char = msvcrt.getch()
        if char in (b'\x00', b'\xe0'):  # teclas especiales (flechas, F1, etc.)
            msvcrt.getch()
            return b''
        return char
    else:
        fd = sys.stdin.fileno()
        config_original = termios.tcgetattr(fd)
        try:
            tty.setraw(fd)
            char = sys.stdin.read(1)
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, config_original)
        return char.encode("utf-8", errors="ignore")

def procesar_tecla(char, contra):
    if not char:
        return contra, False

    if char in (b'\r', b'\n'):
        return contra, True

    if char in (b'\x03', b'\x1a'):
        return None, True

    if char in (b'\x08', b'\x7f'):
        if contra:
            contra = contra[:-1]
            print("\b \b", end="", flush=True)
        return contra, False

    try:
        letra = char.decode("utf-8")
    except UnicodeDecodeError:
        return contra, False

    if letra.isprintable():
        contra += letra
        print("*", end="", flush=True)

    return contra, False

def contra_input(prompt):
    print(prompt, end="", flush=True)
    contra = ""

    while True:
        char = leer_tecla()
        contra, terminar = procesar_tecla(char, contra)

        if contra is None:
            print("\nNo use comandos de teclado")
            return None

        if terminar:
            print()
            return contra


def validar_longitud(password):
    # Se agregó también un mínimo (antes solo existía el máximo),
    # para no permitir contraseñas demasiado cortas como "Aa1!".
    if len(password) < 8:
        return "La contraseña debe tener un mínimo de 8 caracteres."
    if len(password) > 15:
        return "La contraseña debe tener un máximo de 15 caracteres."
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
    validaciones = [validar_longitud, validar_mayuscula, validar_minuscula, validar_numero, validar_especial]

    while True:
        password1 = contra_input("Ingrese contraseña: ")
        if password1 is None:
            continue

        password2 = contra_input("Confirme contraseña: ")
        if password2 is None:
            continue

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