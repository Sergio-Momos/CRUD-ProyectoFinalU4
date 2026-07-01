clientes = {}
usuarios = {}
def menuprincipal():
    print("""================================
M E N Ú  P R I N C I P A L   
================================
1.- (C) INGRESAR         
2.- (R) MOSTRAR          
3.- (U) MODIFICAR        
4.- (D) ELIMINAR         
5.-     Salir            
================================""")

def menumostrar():
    print("""================================
M E N Ú  M O S T R A R     
================================
1.- MOSTRAR TODO         
2.- MOSTRAR UNO          
3.- MOSTRAR PARCIAL      
4.- VOLVER               
================================""")

def menu_usuarios():
    print("""================================
M E N Ú  U S U A R I O S     
================================
1.-  INICIAR SESIÓN      
2.-  REGISTRAR USUARIO   
3.-  Salir               
================================""")

def agregar_cliente(codigo, run, nombre, apellido, direccion, fono, correo, tipo, monto, deuda):
    if codigo in clientes:
        return False

    cliente = {
        "id": codigo,
        "run": run,
        "nombre": nombre,
        "apellido": apellido,
        "direccion": direccion,
        "telefono": fono,
        "correo": correo,
        "tipo": tipo,
        "monto": monto,
        "deuda": deuda
    }
    clientes[codigo] = cliente
    return True

def run_existe(run):
    for cliente in clientes.values():
        if cliente["run"] == run:
            return True
    return False

#getter: Retorna el dic de clientes
def obtener_clientes():
    return clientes

def buscar_cliente(id):
    return clientes.get(id)

def actualizar_cliente(id_cliente, nuevos_datos):
    if id_cliente not in clientes:
        return False

    clientes[id_cliente] = nuevos_datos
    return True

def eliminar_datos(id_cliente):
    if id_cliente not in clientes:
        return False

    del clientes[id_cliente]
    return True

def ingreso_usuarios(codigo, username, clave, salt, nombre, apellidos, correo):
    usuarios[username] = {
        "codigo": codigo,
        "username": username,
        "clave": clave,
        "salt": salt,
        "nombre": nombre,
        "apellidos": apellidos,
        "correo": correo
    }