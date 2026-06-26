clientes = {}
usuarios = {}
def menuprincipal():
    print("================================")
    print("   M E N Ú  P R I N C I P A L   ")
    print("================================")
    print("       1.- (C) INGRESAR         ")
    print("       2.- (R) MOSTRAR          ")
    print("       3.- (U) MODIFICAR        ")
    print("       4.- (D) ELIMINAR         ")
    print("       5.-     Salir            ")
    print("================================")

def menumostrar():
    print("================================")
    print("     M E N Ú  M O S T R A R     ")
    print("================================")
    print("       1.- MOSTRAR TODO         ")
    print("       2.- MOSTRAR UNO          ")
    print("       3.- MOSTRAR PARCIAL      ")
    print("       4.- VOLVER               ")
    print("================================")

def menuUsuarios():
    print("================================")
    print("   M E N Ú  U S U A R I O S     ")
    print("================================")
    print("       1.-  INICIAR SESIÓN      ")
    print("       2.-  REGISTRAR USUARIO   ")
    print("       3.-  Salir               ")
    print("================================")

def agregarCliente(codigo,run,nombre,apellido,direccion,fono,correo,tipo,monto,deuda):
    try:
        #no tengo la menor idea si el código lo almaceno de forma óptima
        cliente = [codigo,run,nombre,apellido,direccion,fono,correo,tipo,monto,deuda]
        clientes[codigo]=cliente
    except:
        return False
    return True
def buscarCliente(mod):
    datos = clientes.get(mod)
    print(datos) #Plasmar en el informe, como evitar que se caiga la aplicación con valor NONE
    return datos
def modificarDatos(mod,listanuevos):
    clientes[mod]=listanuevos #siento que el código esta incompleto, que miedo

def eliminarDatos(elim):
    del clientes[elim] #siento que esto se va a caer, que miedo

def ingresoUsuarios(codigo,username,clave,nombre,apellidos,correo):
    #creo que este código podría ser mejorado, help me!!!
    usuario = [codigo,username,clave,nombre,apellidos,correo]
    usuarios[username] = usuario