import re
import grupoFunciones as g
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

        except Exception as error:
            print(f"Error inesperado: {error}")
            return None

def ing_usuario():
    global idusuario
    print("\n" + "=" * 35)
    print("       INGRESO DE USUARIO")
    print("=" * 35)
    username = leer_y_validar(
        "USERNAME: ",
        r"^[a-zA-Z0-9_]+$",
        "Solo letras, números y guión bajo."
    )
    if not username:
        return

    # Validar usuario duplicado
    if g.usuarios.get(username):
        print("Ese usuario ya existe.")
        return

    clave = leer_y_validar("CLAVE: ")
    if not clave:
        return

    nombre = leer_y_validar(
        "NOMBRE: ",
        r"^[a-zA-ZáéíóúÁÉÍÓÚñÑ\s]+$",
        "Solo letras y espacios."
    )
    if not nombre:
        return

    apellidos = leer_y_validar(
        "APELLIDOS: ",
        r"^[a-zA-ZáéíóúÁÉÍÓÚñÑ\s]+$",
        "Solo letras y espacios."
    )
    if not apellidos:
        return

    correo = leer_y_validar(
        "CORREO: ",
        r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$",
        "Formato de correo incorrecto."
    )
    if not correo:
        return

    try:
        idusuario += 1
        codigo = idusuario

        g.ingreso_usuarios(
            codigo,
            username,
            clave,
            nombre,
            apellidos,
            correo
        )

        print("=" * 35)
        print("Registro exitoso.")
        print("=" * 35)

    except Exception as error:
        print(f"Error al guardar datos: {error}")
        
        



def login():
    user = input("Ingrese nombre de usuario: ")
    clave = input("Ingrese password: ")

    usuario = g.usuarios.get(user)

    if not usuario:
        input("Usuario no registrado. ENTER para volver.")
        return None

    if usuario[2] != clave:
        input("Contraseña incorrecta. ENTER para volver.")
        return None

    return usuario


