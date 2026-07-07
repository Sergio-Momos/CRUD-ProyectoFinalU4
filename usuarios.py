import grupoFunciones as g
import pass_validacion as seguridad
import auditoria as audit
from getpass import getpass
import validaciones as v
import constantes as c

def ing_usuario():
    username = v.leer_y_validar("Username: ", c.PATRON_USER, c.ERROR_USER)

    if not username:
        return

    if username in g.usuarios:
        print("Usuario ya existe.")
        audit.registrar_error(username, "REGISTRO_USUARIO", "username ya existente")
        return

    clave_hash, salt = seguridad.validar_contra()

    if not clave_hash:
        return

    nombre = v.leer_y_validar("Nombre: ", c.PATRON_NOMBRE, c.ERROR_SOLO_LETRAS)

    if not nombre:
        return

    apellidos = v.leer_y_validar("Apellidos: ", c.PATRON_NOMBRE, c.ERROR_SOLO_LETRAS)

    if not apellidos:
        return

    correo = v.leer_y_validar("Correo: ", c.PATRON_CORREO, c.ERROR_SOLO_LETRAS)

    if not correo:
        return

    if g.correo_existe(correo):
        print("Correo ya registrado.")
        audit.registrar_error(username, "REGISTRO_USUARIO", "correo ya existente")
        return

    codigo = g.generar_id_usuario()
    g.ingreso_usuarios(
        codigo,
        username,
        clave_hash,
        salt,
        nombre,
        apellidos,
        correo
    )
    audit.registrar(username, "REGISTRO_USUARIO", f"codigo={codigo}, correo={correo}")
    print("Usuario registrado correctamente.")

def login():
    intentos = 0
    while intentos < 3:
        username = v.leer_y_validar("Username: ", c.PATRON_USER, c.ERROR_USER)
        if not username: return None

        password = seguridad.contra_input("Ingrese contraseña: ")
        if not password: return None

        usuario = g.usuarios.get(username)
        if not usuario or usuario["clave"] != seguridad.encriptar_password(password, usuario["salt"]):
            print(f"Error: Inicio de sesion fallido. Te quedan {2 - intentos} intentos.")
            audit.registrar_error(username, "LOGIN", f"intento {intentos + 1}/3 fallido")
            intentos += 1
            continue

        print("Login exitoso.")
        audit.registrar(username, "LOGIN", "exitoso")
        return usuario

    print("\n[ERROR]: Has superado el límite de 3 intentos permitidos.")
    audit.registrar_error(username, "LOGIN", "bloqueado tras 3 intentos fallidos")
    return None