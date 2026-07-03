import grupoFunciones as g
import constantes as c
import validacion_CL as v

idcliente = 0

def pausar():
    input("PRESIONE ENTER PARA CONTINUAR...")

def imprimir_cliente(id_cliente, cliente):
    campos = [
        ("ID", id_cliente),
        ("RUN", cliente["run"]),
        ("NOMBRE", cliente["nombre"]),
        ("APELLIDO", cliente["apellido"]),
        ("DIRECCIÓN", cliente["direccion"]),
        ("FONO", cliente["telefono"]),
        ("CORREO", cliente["correo"]),
        ("MONTO CRÉDITO", cliente["monto"]),
        ("DEUDA", cliente["deuda"]),
        ("TIPO", cliente["tipo"]),
    ]
    print(" - ".join(f"{etiqueta}: {valor}" for etiqueta, valor in campos))
    print("-" * 150)


def pedir_id(mensaje, error="El ID debe ser numérico."):
    return int(v.leer_y_validar(mensaje, c.PATRON_NUMEROS, error))


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
        "nombre": v.leer_y_validar("INGRESE NOMBRE   : ", c.PATRON_NOMBRE, c.ERROR_SOLO_LETRAS),
        "apellido": v.leer_y_validar("INGRESE APELLIDO : ", c.PATRON_NOMBRE, c.ERROR_SOLO_LETRAS),
        "direccion": v.leer_y_validar("INGRESE DIRECCIÓN: "),
        "telefono": v.leer_y_validar("INGRESE TELÉFONO : ", c.PATRON_TELEFONO, c.ERROR_TELEFONO),
        "correo": v.leer_y_validar("INGRESE CORREO   : ", c.PATRON_CORREO, c.ERROR_CORREO),
    }


def seleccionar_tipo(tipo_actual=None):
    """
    Pide un código de tipo de cliente y devuelve su nombre.
    Si se pasa tipo_actual, primero pregunta si se desea modificar;
    si la respuesta es "no", devuelve el tipo actual sin más preguntas.
    """
    if tipo_actual is not None:
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
        codigo = pedir_id("Ingrese Código de Tipo: ", c.ERROR_NUMEROS)
        if codigo in c.TIPOS:
            return c.TIPOS[codigo]
        print("\nTipo fuera de rango.")


def pedir_monto():
    return int(v.leer_y_validar("INGRESE MONTO CRÉDITO: ", c.PATRON_NUMEROS, c.ERROR_NUMEROS))


def ing_cliente():
    print("\n" + "=" * 33 + "\n     INGRESAR DATOS CLIENTE\n" + "=" * 33)

    run = pedir_run()
    datos = pedir_datos_cliente()
    tipo = seleccionar_tipo()
    monto = pedir_monto()

    global idcliente
    idcliente += 1

    exito = g.agregar_cliente(
        idcliente, run,
        datos["nombre"], datos["apellido"], datos["direccion"],
        datos["telefono"], datos["correo"],
        tipo, monto, 0
    )

    print("\n[✔] INCORPORACIÓN EXITOSA [✔]" if exito else "\n[X] INCORPORACIÓN FALLIDA [X]")
    pausar()


def mostrar():
    opciones = {
        1: mostrartodo,
        2: mostraruno,
        3: mostrarparcial,
    }
    while True:
        g.menumostrar()
        op2 = pedir_id("INGRESE OPCIÓN: ", c.ERROR_NUMEROS)

        if op2 == 4:
            print("\nVolviendo al menú principal...")
            break
        elif op2 in opciones:
            opciones[op2]()
        else:
            print("\nOpción fuera de rango (1-4)")
            pausar()


def mostrartodo():
    print("=================================\nMUESTRA DE TODOS LOS CLIENTES\n=================================")

    clientes = g.obtener_clientes()

    if not clientes:
        print("\nNo existen clientes registrados en el sistema todavía.")
    else:
        for id_cliente, cliente in clientes.items():
            imprimir_cliente(id_cliente, cliente)
    pausar()


def mostraruno():
    print("=================================\n            MUESTRA DE DATOS PARTICULAR\n=================================")

    idcliente_buscado = pedir_id("\nIngrese el ID del Cliente que desea mostrar: ")
    cliente = g.buscar_cliente(idcliente_buscado)

    if cliente is None:
        print("\nError: El ID ingresado no corresponde a ningún cliente registrado.")
    else:
        imprimir_cliente(idcliente_buscado, cliente)
    pausar()


def mostrarparcial():
    print("=======================================\n            MUESTRA PARCIALMENTE LOS CLIENTES\n=======================================")

    while True:
        cant = pedir_id("\nIngrese la Cantidad de Clientes a Mostrar : ", c.ERROR_NUMEROS)
        if cant <= 0:
            print("\nPor favor, ingrese un número mayor a 0.")
            continue
        break

    diccionario_clientes = g.obtener_clientes()

    if not diccionario_clientes:
        print("\nNo existen clientes registrados en el sistema todavía.")
    else:
        for id_cliente, cliente in list(diccionario_clientes.items())[:cant]:
            imprimir_cliente(id_cliente, cliente)
    pausar()


def modifica(campo, valor_actual, patron=None, error="Entrada inválida."):
    opcion = v.leer_y_validar(
        f"¿Desea modificar {campo}? ({valor_actual}) [SI/NO]: ",
        c.PATRON_SI_NO,
        c.ERROR_SI_NO
    )
    if opcion.lower() == "si":
        return v.leer_y_validar(f"Ingrese nuevo {campo}: ", patron, error)
    return valor_actual


def modificardatos():
    print("\n" + "=" * 35 + "\n      MÓDULO MODIFICAR CLIENTE\n" + "=" * 35)

    mostrartodo()

    id_cliente = pedir_id("\nIngrese ID del cliente a modificar: ", c.ERROR_NUMEROS)
    cliente = g.buscar_cliente(id_cliente)

    if cliente is None:
        print("\n[X] Error: El ID ingresado no existe. [X]")
        pausar()
        return

    print(f"\nCliente seleccionado:\nID  : {cliente['id']}\nRUN : {cliente['run']}\n")

    nuevos_datos = {
        "id": cliente["id"],
        "run": cliente["run"],
        "nombre": modifica("NOMBRE", cliente["nombre"], c.PATRON_NOMBRE, c.ERROR_SOLO_LETRAS),
        "apellido": modifica("APELLIDO", cliente["apellido"], c.PATRON_NOMBRE, c.ERROR_SOLO_LETRAS),
        "direccion": modifica("DIRECCIÓN", cliente["direccion"]),
        "telefono": modifica("TELÉFONO", cliente["telefono"], c.PATRON_TELEFONO, c.ERROR_TELEFONO),
        "correo": modifica("CORREO", cliente["correo"], c.PATRON_CORREO, c.ERROR_CORREO),
        "tipo": seleccionar_tipo(cliente["tipo"]),
        "monto": int(modifica("MONTO CRÉDITO", str(cliente["monto"]), c.PATRON_NUMEROS, c.ERROR_NUMEROS)),
        "deuda": int(modifica("DEUDA", str(cliente["deuda"]), c.PATRON_NUMEROS, c.ERROR_NUMEROS)),
    }

    if g.actualizar_cliente(id_cliente, nuevos_datos):
        print("\n[✔] CLIENTE MODIFICADO CON ÉXITO [✔]")
    else:
        print("\n[X] ERROR AL ACTUALIZAR CLIENTE [X]")
    pausar()


def eliminardatos():
    print("\n" + "=" * 35 + "\n      MÓDULO ELIMINAR CLIENTE\n" + "=" * 35)

    mostrartodo()

    elim = pedir_id("\nIngrese valor de ID del Cliente que desea Eliminar: ")
    cliente = g.buscar_cliente(elim)

    if cliente is None:
        print("\n[X] Error: El ID ingresado no existe. [X]")
        pausar()
        return

    print(f"\nATENCIÓN: Va a eliminar al cliente: {cliente['nombre']} {cliente['apellido']} (ID: {cliente['id']})")

    confirmar = v.leer_y_validar("¿ESTÁ SEGURO DE ELIMINAR ESTE CLIENTE? [SI/NO]: ", c.PATRON_SI_NO, c.ERROR_SI_NO)

    if confirmar.lower() == "si":
        if g.eliminar_datos(elim):
            print("\n[✔] CLIENTE ELIMINADO EXITOSAMENTE [✔]")
        else:
            print("\n[X] Error al eliminar cliente [X]")
    else:
        print("\nOperación cancelada.")
    pausar()