import re
import grupoFunciones as g
import pass_validacion as seguridad
from getpass import getpass
idusuario = 0

def leer_y_validar(mensaje, patron=None, error_msg="Entrada inválida."):
    while True:
        try:
            entrada = input(mensaje).strip()

            if not entrada:
                print("Error: No puedes ingresar campo vacío.")
                continue

            if patron and not re.match(patron, entrada):
                print(f"Error: {error_msg}")
                continue

            return entrada

        except (KeyboardInterrupt, EOFError):
            print("\nOperación cancelada por Control + C / Control + Z.")
            return None


def ing_usuario():
    username = leer_y_validar(
        "Username: ",
        r"^[a-zA-Z0-9_]+$",
        "Solo letras, números y guión bajo."
    )

    if not username:
        return

    if username in g.usuarios:
        print("Usuario ya existe.")
        return

    clave_hash, salt = seguridad.validar_contra()

    if not clave_hash:
        return

    nombre = leer_y_validar(
        "Nombre: ",
        r"^[a-zA-ZáéíóúÁÉÍÓÚñÑ\s]+$",
        "Solo letras y espacios."
    )

    if not nombre:
        return

    apellidos = leer_y_validar(
        "Apellidos: ",
        r"^[a-zA-ZáéíóúÁÉÍÓÚñÑ\s]+$",
        "Solo letras y espacios."
    )

    if not apellidos:
        return

    correo = leer_y_validar(
        "Correo: ",
        r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$",
        "Correo inválido."
    )

    if not correo:
        return

    codigo = len(g.usuarios) + 1
    g.ingreso_usuarios(
        codigo,
        username,
        clave_hash,
        salt,
        nombre,
        apellidos,
        correo
    )
    print("Usuario registrado correctamente.")

def login():
    username = leer_y_validar("Username: ",
        r"^[a-zA-Z0-9_]+$",
        "Solo letras, números y guión bajo.")
    if not username:
        return None
    password = getpass("Contraseña: ")
    if not password:
        return None
    usuario = g.usuarios.get(username)
    if not usuario:
        print("Usuario no existe.")
        return None
    salt = usuario["salt"]
    password_hash = seguridad.encriptar_password(password, salt)
    if usuario["clave"] != password_hash:
        print("Clave incorrecta.")
        return None
    print("Login exitoso.")
    return usuario
