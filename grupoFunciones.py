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

def agregar_cliente(codigo,run,nombre,apellido,direccion,fono,correo,tipo,monto,deuda):
    try:
        #no tengo la menor idea si el código lo almaceno de forma óptima
        cliente = [codigo,run,nombre,apellido,direccion,fono,correo,tipo,monto,deuda]
        clientes[codigo]=cliente
    except:
        return False
        raise
    return True  

def buscar_cliente(mod):
    datos = clientes.get(mod)
    print(datos) #Plasmar en el informe, como evitar que se caiga la aplicación con valor NONE
    return datos

def modificar_datos(mod,listanuevos):
    clientes[mod]=listanuevos #siento que el código esta incompleto, que miedo

def eliminar_datos(elim):
    del clientes[elim] #siento que esto se va a caer, que miedo

def ingreso_usuarios(codigo, username, clave, nombre, apellidos, correo):
    usuarios[username] = {
        "codigo": codigo,
        "username": username,
        "clave": clave,
        "nombre": nombre,
        "apellidos": apellidos,
        "correo": correo
    }