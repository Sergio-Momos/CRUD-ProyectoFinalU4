import grupoFunciones as g
import re
import constantes as c
import validacion_CL as v
idcliente = 0
listanuevos=[]

def pausar():
    input("PRESIONE ENTER PARA CONTINUAR...")

def validar_rut_chileno(rut):
    try:
        cuerpo = rut[:-1]
        digito_verificador = rut[-1].upper()
        if not cuerpo.isdigit():
            return False

        if len(cuerpo) < 7 or len(cuerpo) > 8:
            return False

        suma = sum(
            int(digito) * (i % 6 + 2)
            for i, digito in enumerate(reversed(cuerpo))
        )

        resto = 11 - (suma % 11)

        if resto == 11:
            dv_esperado = "0"
        elif resto == 10:
            dv_esperado = "K"
        else:
            dv_esperado = str(resto)

        return digito_verificador == dv_esperado

    except (ValueError, IndexError):
        return False

def pedir_run():
    while True:
        run = v.leer_y_validar(
            "RUN (Sin puntos ni guion, ej: 12345678K): ",
            c.PATRON_RUN,
            "Formato incorrecto."
        )

        if not v.validar_rut_chileno(run):
            print("\nRUN inválido.")
            continue

        run_formateado = f"{run[:-1]}-{run[-1].upper()}"

        if g.run_existe(run_formateado):
            print("\nEse RUN ya está registrado.")
            continue

        return run_formateado
    

def pedir_datos_cliente():
    return {
        "nombre": v.leer_y_validar(
            "INGRESE NOMBRE   : ",
            c.PATRON_NOMBRE,
            c.ERROR_SOLO_LETRAS
        ),
        "apellido": v.leer_y_validar(
            "INGRESE APELLIDO : ",
            c.PATRON_NOMBRE,
            c.ERROR_SOLO_LETRAS
        ),
        "direccion": v.leer_y_validar("INGRESE DIRECCIÓN: "),
        "telefono": v.leer_y_validar(
            "INGRESE TELÉFONO : ",
            c.PATRON_TELEFONO,
            c.ERROR_TELEFONO
        ),
        "correo": v.leer_y_validar(
            "INGRESE CORREO   : ",
            c.PATRON_CORREO,
            c.ERROR_CORREO
        )
    }

def pedir_tipo_cliente():
    tipos = {
        101: "Plata",
        102: "Oro",
        103: "Platino"
    }

    print("-" * 44)
    print(" CODIGOS: 101 - Plata | 102 - Oro | 103 - Platino")
    print("-" * 44)

    while True:
        codigo = int(v.leer_y_validar(
            "Ingrese Código de Tipo: ",
            c.PATRON_NUMEROS,
            c.ERROR_NUMEROS
        ))

        if codigo in tipos:
            return tipos[codigo]

        print("\nTipo fuera de rango.")

def pedir_monto():
    monto = v.leer_y_validar(
        "INGRESE MONTO CRÉDITO: ",
        c.PATRON_NUMEROS,
        c.ERROR_NUMEROS
    )
    return int(monto)    

def ing_cliente():
    print("\n" + "=" * 33 + "\n     INGRESAR DATOS CLIENTE\n" + "=" * 33)

    run = pedir_run()
    datos = pedir_datos_cliente()
    tipo = pedir_tipo_cliente()
    monto = pedir_monto()

    global idcliente
    idcliente += 1

    exito = g.agregar_cliente(
        idcliente,
        run,
        datos["nombre"],
        datos["apellido"],
        datos["direccion"],
        datos["telefono"],
        datos["correo"],
        tipo,
        monto,
        0
    )

    print("\n[✔] INCORPORACIÓN EXITOSA [✔]" if exito else "\n[X] INCORPORACIÓN FALLIDA [X]")

    pausar()
    

def mostrar():
    while True:
        g.menumostrar()
        op2 = int(
            v.leer_y_validar(
                "INGRESE OPCIÓN: ",
                c.PATRON_NUMEROS,
                c.ERROR_NUMEROS
            )
        )
        if op2 == 1:
            mostrartodo()
        elif op2 == 2:
            mostraruno()
        elif op2 == 3:
            mostrarparcial()
        elif op2 == 4:
            print("\nVolviendo al menú principal...")
            break
        else:
            print("\nOpción fuera de rango (1-4)")
            pausar()


def mostrartodo():
    print("""=================================
MUESTRA DE TODOS LOS CLIENTES
=================================""")
    
    clientes = g.obtener_clientes()

    if not clientes:
        print("\nNo existen clientes registrados en el sistema todavía.")
    else:
        for id_cliente, cliente in clientes.items():
            print(
                f"ID: {id_cliente} - "
                f"RUN: {cliente['run']} - "
                f"NOMBRE: {cliente['nombre']} - "
                f"APELLIDO: {cliente['apellido']} - "
                f"DIRECCIÓN: {cliente['direccion']} - "
                f"FONO: {cliente['telefono']} - "
                f"CORREO: {cliente['correo']} - "
                f"MONTO CRÉDITO: {cliente['monto']} - "
                f"DEUDA: {cliente['deuda']} - "
                f"TIPO: {cliente['tipo']}"
            )
            print("-" * 150)
    pausar()

def mostraruno():
    print("""=================================
            MUESTRA DE DATOS PARTICULAR
=================================""")
    
    op = int(
        v.leer_y_validar(
            "\nIngrese el ID del Cliente que desea mostrar: ",
            c.PATRON_NUMEROS,
            "El ID debe ser numérico."
        )
    )

    datos = g.buscar_cliente(op)

    if datos is None:
        print("\nError: El ID ingresado no corresponde a ningún cliente registrado.")
    else:
        print(f"""
=======================================
MUESTRA DE DATOS DEL CLIENTE
=======================================
ID            : {datos["id"]}
RUN           : {datos["run"]}
NOMBRE        : {datos["nombre"]}
APELLIDO      : {datos["apellido"]}
DIRECCION     : {datos["direccion"]}
FONO          : {datos["telefono"]}
CORREO        : {datos["correo"]}
TIPO          : {datos["tipo"]}
MONTO CREDITO : {datos["monto"]}
DEUDA         : {datos["deuda"]}
---------------------------------------
""")

    input("\n PRESIONE ENTER PARA CONTINUAR...")

def mostrarparcial():
    print("""=======================================
            MUESTRA PARCIALMENTE LOS CLIENTES
=======================================""")

    while True:
        cant = int(
            v.leer_y_validar(
                "\nIngrese la Cantidad de Clientes a Mostrar : ",
                c.PATRON_NUMEROS,
                c.ERROR_NUMEROS
            )
        )

        if cant <= 0:
            print("\nPor favor, ingrese un número mayor a 0.")
            continue
        break

    diccionario_clientes = g.obtener_clientes()

    if not diccionario_clientes:
        print("\nNo existen clientes registrados en el sistema todavía.")

    else:
        clientes_parciales = list(diccionario_clientes.items())[:cant]

        for id_cliente, cliente in clientes_parciales:
            print(
                f"ID: {id_cliente} - "
                f"RUN: {cliente['run']} - "
                f"NOMBRE: {cliente['nombre']} - "
                f"APELLIDO: {cliente['apellido']} - "
                f"DIRECCION: {cliente['direccion']} - "
                f"FONO: {cliente['telefono']} - "
                f"CORREO: {cliente['correo']} - "
                f"MONTO CRÉDITO: {cliente['monto']} - "
                f"DEUDA: {cliente['deuda']} - "
                f"TIPO: {cliente['tipo']}"
            )
            print("-" * 150)

    pausar()

def modificar_tipo(tipo_actual):
    tipos = {
        101: "Plata",
        102: "Oro",
        103: "Platino"
    }

    opcion = v.leer_y_validar(
        f"¿Desea modificar TIPO? ({tipo_actual}) [SI/NO]: ",
        c.PATRON_SI_NO,
        c.ERROR_SI_NO
    )

    if opcion.lower() == "no":
        return tipo_actual

    print("-" * 44)
    print(" CODIGOS: 101 - Plata | 102 - Oro | 103 - Platino")
    print("-" * 44)

    while True:
        codigo = int(
            v.leer_y_validar(
                "Ingrese Código de Tipo: ",
                c.PATRON_NUMEROS,
                c.ERROR_NUMEROS
            )
        )

        if codigo in tipos:
            return tipos[codigo]

        print("\nTipo fuera de rango.")

def modifica(campo, valor_actual, patron=None, error="Entrada inválida."):
    opcion = v.leer_y_validar(
        f"¿Desea modificar {campo}? ({valor_actual}) [SI/NO]: ",
        c.PATRON_SI_NO,
        c.ERROR_SI_NO
    )
    if opcion.lower() == "si":
        return v.leer_y_validar(
            f"Ingrese nuevo {campo}: ",
            patron,
            error
        )

    return valor_actual

def modificardatos():
    print("\n" + "=" * 35)
    print("      MÓDULO MODIFICAR CLIENTE")
    print("=" * 35)

    mostrartodo()

    id_cliente = int(
        v.leer_y_validar(
            "\nIngrese ID del cliente a modificar: ",
            c.PATRON_NUMEROS,
            c.ERROR_NUMEROS
        )
    )

    cliente = g.buscar_cliente(id_cliente)

    if cliente is None:
        print("\n[X] Error: El ID ingresado no existe. [X]")
        pausar()
        return

    print(f"""
Cliente seleccionado:
ID  : {cliente["id"]}
RUN : {cliente["run"]}
""")

    nuevos_datos = {
        "id": cliente["id"],
        "run": cliente["run"],
        "nombre": modifica(
            "NOMBRE",
            cliente["nombre"],
            c.PATRON_NOMBRE,
            c.ERROR_SOLO_LETRAS
        ),
        "apellido": modifica(
            "APELLIDO",
            cliente["apellido"],
            c.PATRON_NOMBRE,
            c.ERROR_SOLO_LETRAS
        ),
        "direccion": modifica(
            "DIRECCIÓN",
            cliente["direccion"]
        ),
        "telefono": modifica(
            "TELÉFONO",
            cliente["telefono"],
            c.PATRON_TELEFONO,
            c.ERROR_TELEFONO
        ),
        "correo": modifica(
            "CORREO",
            cliente["correo"],
            c.PATRON_CORREO,
            c.ERROR_CORREO
        ),
        "tipo": modificar_tipo(
            cliente["tipo"]
        ),
        "monto": int(
            modifica(
                "MONTO CRÉDITO",
                str(cliente["monto"]),
                c.PATRON_NUMEROS,
                c.ERROR_NUMEROS
            )
        ),
        "deuda": int(
            modifica(
                "DEUDA",
                str(cliente["deuda"]),
                c.PATRON_NUMEROS,
                c.ERROR_NUMEROS
            )
        )
    }

    if g.actualizar_cliente(id_cliente, nuevos_datos):
        print("\n[✔] CLIENTE MODIFICADO CON ÉXITO [✔]")
    else:
        print("\n[X] ERROR AL ACTUALIZAR CLIENTE [X]")
    pausar()


def eliminardatos():
    print("\n" + "=" * 35)
    print("      MÓDULO ELIMINAR CLIENTE")
    print("=" * 35)

    mostrartodo()

    elim = int(
        v.leer_y_validar(
            "\nIngrese valor de ID del Cliente que desea Eliminar: ",
            c.PATRON_NUMEROS,
            "El ID debe ser un número."
        )
    )

    cliente = g.buscar_cliente(elim)

    if cliente is None:
        print("\n[X] Error: El ID ingresado no existe. [X]")
        pausar()
        return

    print(
        f"\nATENCIÓN: Va a eliminar al cliente: "
        f"{cliente['nombre']} {cliente['apellido']} "
        f"(ID: {cliente['id']})"
    )

    confirmar = v.leer_y_validar(
        "¿ESTÁ SEGURO DE ELIMINAR ESTE CLIENTE? [SI/NO]: ",
        c.PATRON_SI_NO,
        c.ERROR_SI_NO
    )

    if confirmar.lower() == "si":
        eliminado = g.eliminar_datos(elim)

        if eliminado:
            print("\n[✔] CLIENTE ELIMINADO EXITOSAMENTE [✔]")
        else:
            print("\n[X] Error al eliminar cliente [X]")

    else:
        print("\nOperación cancelada.")

    pausar()