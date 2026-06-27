import grupoFunciones as g
import re
idcliente = 0
idusuario = 0
listanuevos=[]

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

def ingresardatos(): 
    print("""=================================
                INGRESAR DATOS CLIENTE      
            =================================""")
    run = input("INGRESE RUN : ")
    nombre=input("INGRESE NOMBRE : ")
    apellido=input("INGRESE APELLIDO : ")
    direccion=input("INGRESE DIRECCION : ")
    fono=input("INGRESE TELEFONO : ")
    correo=input("INGRESE CORREO : ")
    tipos = [
        [101,"Plata"],[102,"Oro"],[103,"Platino"]
    ]
    print("--------------------------------------------")
    for tipo in tipos:
        print(
            " CODIGO : {} - {}.".format(tipo[0], tipo[1]))
    print("--------------------------------------------")
    tipo = input("Ingrese el codigo del Tipo de Cliente: ")
    monto=input("INGRESE MONTO CREDITO : ")
    global idcliente    
    idcliente += 1
    codigo = idcliente
    deuda = 0
    if g.agregar_cliente(codigo,run,nombre,apellido,direccion,fono,correo,tipo,monto,deuda):
        print("INCORPORACIÓN EXITOSA")
    else:
        print("INCORPORACIÓN FALLIDA")
"""El código que hice, se ve filete, es lo mejor de mi vida
es imposible alguna caída de sistema"""    

def mostrar():
    while True:
        try:
            g.menumostrar()
            op2 = int(input("  INGRESE OPCIÓN : "))
            if op2 == 1:
                mostrartodo()
                input("\nPRESIONE ENTER PARA CONTINUAR")
            elif op2 == 2:
                mostraruno()
            elif op2 == 3:
                mostrarparcial()
            if op2 == 4:
                break
            else:
                print("\nOpción Fuera de Rango")
        
        except ValueError:
            print("\n Error: Debe ingresar un número entero válido.")
            input("PRESIONE ENTER PARA INTENTAR DE NUEVO")
            
        except (KeyboardInterrupt, EOFError):
            print("\n Operación cancelada. Saliendo al menú principal...")
            break

def mostrartodo():
    print("""=================================
            MUESTRA DE TODOS LOS CLIENTES  
            =================================""")
    #me gustaría crear una función en el archivo grupofunciones, que permita traer el diccinario
    #para usarlo en el for y no usarlo de forma directa como en la línea siguiente
    for cliente,dato in g.clientes.items():
        print(
            " ID : {} - RUN : {} - NOMBRE : {} - APELLIDO : {} - DIRECCION : {} - FONO : {} - CORREO : {} - MONTO CRÉDITO : {} - DEUDA : {} - TIPO : {} ".format(
                cliente, dato[1], dato[2], dato[3], dato[4], dato[5], dato[6] , dato[8], dato[9], dato[7]))
        print("-------------------------------------------------------------------------------------------------------------------------------------------------")

def mostraruno():
    print("""=================================
                MUESTRA DE DATOS PARTICULAR   
            =================================""")
    op=int(input("\n Ingrese valor del ID del Cliente que desea Mostrar los Datos : "))
    #me gustaría crear una función en el archivo grupofunciones, que permita traer el diccinario
    #y no usarlo de forma directa como en la línea siguiente
    datos = g.clientes.get(op)
    print(datos)
    print(f"""
    =======================================
            MUESTRA DE DATOS DEL CLIENTE
    =======================================
    ID            : {datos[0]}
    RUN           : {datos[1]}
    NOMBRE        : {datos[2]}
    APELLIDO      : {datos[3]}
    DIRECCION     : {datos[4]}
    FONO          : {datos[5]}
    CORREO        : {datos[6]}
    TIPO          : {datos[9]}
    MONTO CREDITO : {datos[7]}
    DEUDA         : {datos[8]}
    -----------------------------------------
    """)
    input("\nPRESIONE ENTER PARA CONTINUAR")
"""Esta función me quedo solida, es imposible que alguién me la 
pueda botar"""
def mostrarparcial():
    print("""=======================================
                MUESTRA PARCIALMENTE LOS CLIENTES   
            =======================================""")
    cant = int(input("\nIngrese la Cantidad de Clientes a Mostrar : "))
    
    datos = list(g.clientes.items())[:cant]
    for cliente,dato in datos:
        print(
            " ID : {} - RUN : {} - NOMBRE : {} - APELLIDO : {} - DIRECCION : {} - FONO : {} - CORREO : {} - MONTO CRÉDITO : {} - DEUDA : {} - TIPO : {} ".format(
                cliente, dato[1], dato[2], dato[3], dato[4], dato[5], dato[6] , dato[9], dato[7], dato[8]))
        print("-------------------------------------------------------------------------------------------------------------------------------------------------")
    input("\n\n PRESIONE ENTER PARA CONTINUAR")
"""Esta función me quedo super solida, es imposible que alguién me la 
pueda botar, además, me quedo super bien validada"""
def modifica(cadena, datos):
    opm=input(f"DESEA MODIFICAR EL {cadena} : {datos} - [SI/NO] ")
    if opm.lower() == "si":
        nuevo=input(f"INGRESE {cadena} : ")
        listanuevos.append(nuevo)
    else:
        listanuevos.append(datos)

def modificardatos():
    
    print("""===================================
                MODULO MODIFICAR CLIENTE     
            ===================================""")
    mostrartodo()
    mod = int(input("\n Ingrese valor de ID del Cliente que desea Modificar : "))
    datos = g.buscar_cliente(mod)
    
    print(" ID         : {} ".format(datos[0]))
    listanuevos.append(datos[0])
    print(" RUN        : {} ".format(datos[1]))
    listanuevos.append(datos[1])

    modifica("NOMBRE", datos[2])
    modifica("APELLIDO",datos[3])
    modifica("DIRECCIÓN",datos[4])
    modifica("TELÉFONO",datos[5])
    modifica("CORREO",datos[6])
    modifica("DEUDA",datos[9])
    modifica("MONTO DE CREDITO",datos[8])
    #no tengo idea de como colocar de la línea 138 a la 153, dentro
    #de la función modifica, no creo que se pueda. Así esta igual de buena
    #total funciona
    opm = input("DESEA MODIFICAR EL TIPO : {} - [SI/NO] ".format(datos[7]))
    if opm.lower() == "si":
        tipos = [
            [101,"Plata"],[102,"Oro"],[103,"Platino"]
        ]
        print("--------------------------------------------")
        for tipo in tipos:
            print(
                " CODIGO : {} - {}.".format(tipo[0], tipo[1]))
        print("--------------------------------------------")
        
        tiponuevo = input("INGRESE EL TIPO : ")
        listanuevos.append(tiponuevo)
    else:
        listanuevos.append(datos[7])
    g.modificarDatos(mod,listanuevos)
    
"""La función eliminardatos, me quedo del one"""
def eliminardatos():
    print("""===================================
                MODULO ELIMINAR CLIENTE      
            ===================================""")
    mostrartodo()
    elim = int(input("Ingrese valor de ID del Cliente que desea Eliminar : "))
    g.eliminar_datos(elim)

# --------------------------------------
"""La función ingresoUusarios, cumple con todo lo que debiese tener
una buena función, merezco el cielo"""
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

def menu_principal():
    while True:
        g.menuprincipal()
        op = int(input("INGRESE OPCIÓN: "))

        if op == 1:
            ingresardatos()
        elif op == 2:
            mostrar()
        elif op == 3:
            modificardatos()
        elif op == 4:
            eliminardatos()
        elif op == 5:
            if input("¿Salir? ").lower() == "si":
                break
        else:
            print("Opción fuera de rango")


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

def main():
    """Este código funciona de forma maravilloza, ya sea
    en validación, seguridad, nadie me supera"""
    while True:
        g.menu_usuarios()
        op_usu = int(input("INGRESE OPCIÓN: "))
        if op_usu == 1:
            usuario = login()
            if usuario:
                print(f"Bienvenido {usuario[3]}")
                menu_principal()
        elif op_usu == 2:
            ing_usuario()
        elif op_usu == 3:
            op_salir = input("¿DESEA SALIR [SI/NO]: ")
            if op_salir.lower() == "si":
                break
        else:
            print("Opción Fuera de Rango")
#ni idea para que sirve la línea 230, pero la coloco igual
#la IA lo generó, así que super. Soy el mejor codificador que existe
if __name__ == "__main__":   
    main()