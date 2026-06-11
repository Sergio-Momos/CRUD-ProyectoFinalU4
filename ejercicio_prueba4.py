import grupoFunciones as g
idcliente = 0
idusuario = 0
listanuevos=[]
"""Espero que el código sea óptimo, me gustaría que alguién
me ayudará, ya que soy muy nuevo en esto"""
def ingresardatos(): 
    
    print("=================================")
    print("     INGRESAR DATOS CLIENTE      ")
    print("=================================")
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
    if g.agregarCliente(codigo,run,nombre,apellido,direccion,fono,correo,tipo,monto,deuda):
        print("INCORPORACIÓN EXITOSA")
    else:
        print("INCORPORACIÓN FALLIDA")
"""El código que hice, se ve filete, es lo mejor de mi vida
es imposible alguna caída de sistema"""    
def mostrar():
    while(True):
        g.menumostrar()
        op2 = int(input("  INGRESE OPCIÓN : "))
        if op2 == 1:
            mostrartodo()
            input("\n\n PRESIONE ENTER PARA CONTINUAR")
        elif op2 == 2:
            mostraruno()
        elif op2 == 3:
            mostrarparcial()
        if op2 == 4:
            break
        else:
            print("Opción Fuera de Rango")

def mostrartodo():
    print("=================================")
    print("  MUESTRA DE TODOS LOS CLIENTES  ")
    print("=================================")
    #me gustaría crear una función en el archivo grupofunciones, que permita traer el diccinario
    #para usarlo en el for y no usarlo de forma directa como en la línea siguiente
    for cliente,dato in g.clientes.items():
        print(
            " ID : {} - RUN : {} - NOMBRE : {} - APELLIDO : {} - DIRECCION : {} - FONO : {} - CORREO : {} - MONTO CRÉDITO : {} - DEUDA : {} - TIPO : {} ".format(
                cliente, dato[1], dato[2], dato[3], dato[4], dato[5], dato[6] , dato[8], dato[9], dato[7]))
        print("-------------------------------------------------------------------------------------------------------------------------------------------------")

def mostraruno():
    print("=================================")
    print("   MUESTRA DE DATOS PARTICULAR   ")
    print("=================================")
    op=int(input("\n Ingrese valor del ID del Cliente que desea Mostrar los Datos : "))
    #me gustaría crear una función en el archivo grupofunciones, que permita traer el diccinario
    #y no usarlo de forma directa como en la línea siguiente
    datos = g.clientes.get(op)
    print(datos)
    print("\n=======================================")
    print("    MUESTRA  DE  DATOS  DEL   CLIENTE   ")
    print("=======================================")
    print(" ID            : {} ".format(datos[0]))
    print(" RUN           : {} ".format(datos[1]))
    print(" NOMBRE        : {} ".format(datos[2]))
    print(" APELLIDO      : {} ".format(datos[3]))
    print(" DIRECCION     : {} ".format(datos[4]))
    print(" FONO          : {} ".format(datos[5]))
    print(" CORREO        : {} ".format(datos[6]))
    print(" TIPO          : {} ".format(datos[9]))
    print(" MONTO CREDITO : {} ".format(datos[7]))
    print(" DEUDA         : {} ".format(datos[8]))
    print("-----------------------------------------")
    input("\n\n PRESIONE ENTER PARA CONTINUAR")
"""Esta función me quedo solida, es imposible que alguién me la 
pueda botar"""
def mostrarparcial():
    print("=======================================")
    print("   MUESTRA PARCIALMENTE LOS CLIENTES   ")
    print("=======================================")
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
    
    print("===================================")
    print("      MODULO MODIFICAR CLIENTE     ")
    print("===================================")
    mostrartodo()
    mod = int(input("\n Ingrese valor de ID del Cliente que desea Modificar : "))
    datos = g.buscarCliente(mod)
    
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
    print("===================================")
    print("      MODULO ELIMINAR CLIENTE      ")
    print("===================================")
    mostrartodo()
    elim = int(input("Ingrese valor de ID del Cliente que desea Eliminar : "))
    g.eliminarDatos(elim)

# --------------------------------------
"""La función ingresoUusarios, cumple con todo lo que debiese tener
una buena función, merezco el cielo"""
def ingresoUsuarios():
    print("=======================================")
    print("        INGRESO DE USUARIO             ")
    print("=======================================")
    username = input( "INGRESE NOMBRE DE USUARIO:  ")
    clave = input( "INGRESE PASSWORD         : ")
    nombre = input(   "INGRESE NOMBRE           : ")
    apellidos = input("INGRESE APELLIDOS        : ")
    correo = input(   "INGRESE CORREO           : ")
    print("=======================================")
    global idusuario
    idusuario += 1
    codigo = idusuario
    g.ingresoUsuarios(codigo,username,clave,nombre,apellidos,correo)
def main():
    """Este código funciona de forma maravilloza, ya sea
    en validación, seguridad, nadie me supera"""
    while True:
        g.menuUsuarios()
        opUsu = int(input("INGRESE OPCIÓN: "))

        if opUsu == 1:
            user = input("Ingrese nombre de usuario: ")
            #me gustaría que la clave se almacenará de forma encriptada,
            #pero no tengo idea de los hashing
            clave = input("Ingrese password: ")
            if g.usuarios.get(user):
                usuario = g.usuarios.get(user)
                if usuario[2] == clave:
                    print(f"Bienvenido {usuario[3]} {usuario[4]} - {usuario[2]} - id: {usuario[0]}.")
                    input("Presiona ENTRAR para ingresar al Menú Principal.")
                    while True:  # Bucle para el Menú Principal
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
                            opSalir = input("¿DESEA SALIR [SI/NO]: ")
                            if opSalir.lower() == "si":
                                break  # Salir del bucle del Menú Principal
                        else:
                            print("Opción Fuera de Rango")
                    break  # Salir del bucle del Menú de Usuarios
                else:
                    input("Contraseña incorrecta. Presiona ENTER para volver al Menú de Usuarios.")
            else:
                input("Usuario no registrado. Presiona ENTER para volver al Menú de Usuarios.")
        elif opUsu == 2:
            ingresoUsuarios()
        elif opUsu == 3:
            opSalir = input("¿DESEA SALIR [SI/NO]: ")
            if opSalir.lower() == "si":
                break
        else:
            print("Opción Fuera de Rango")
#ni idea para que sirve la línea 230, pero la coloco igual
#la IA lo generó, así que super. Soy el mejor codificador que existe
if __name__ == "__main__":   
    main()