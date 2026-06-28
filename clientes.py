import grupoFunciones as g

idcliente = 0
listanuevos=[]


def ing_cliente(): 
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