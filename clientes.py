import grupoFunciones as g
import constantes as c
import validaciones as v
import auditoria as audit


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

def buscar_run(mensaje):
    while True:
        run = v.leer_y_validar(mensaje + " (o 0 para cancelar): ", c.PATRON_RUN + r"|^0$", c.ERROR_RUN)
        
        if run == "0":
            return None
        
        if not v.validar_rut_chileno(run):
            print("\nRUN inválido.")
            continue

        run_formateado = f"{run[:-1]}-{run[-1].upper()}"

        if g.run_existe(run_formateado):
            return run_formateado
        
        else:
            print("\nEse RUN no está registrado.")

def pedir_run():
    while True:
        run = v.leer_y_validar("RUN (Sin puntos ni guion, ej: 12345678K): ", c.PATRON_RUN, c.ERROR_RUN)

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
        opcion = v.leer_y_validar(f"¿Desea modificar TIPO? ({tipo_actual}) [SI/NO]: ", c.PATRON_SI_NO, c.ERROR_SI_NO)
        if opcion.lower() == "no":
            return tipo_actual

    print("-" * 44)
    print(" CODIGOS: 101 - Plata | 102 - Oro | 103 - Platino")
    print("-" * 44)

    while True:
        codigo = int(v.leer_y_validar("Ingrese codigo de los tipos mostrados: ", c.PATRON_NUMEROS, c.ERROR_NUMEROS))
        if codigo in c.TIPOS:
            return c.TIPOS[codigo]
        print("\nTipo fuera de rango.")

def pedir_monto():
    return int(v.leer_y_validar("INGRESE MONTO CRÉDITO: ", c.PATRON_NUMEROS, c.ERROR_NUMEROS))

def ing_cliente(usuario):
    print("\n" + "=" * 33 + "\n     INGRESAR DATOS CLIENTE\n" + "=" * 33)

    run = pedir_run()
    datos = pedir_datos_cliente()
    tipo = seleccionar_tipo()
    monto = pedir_monto()

    idcliente = g.generar_id_cliente()

    exito = g.agregar_cliente(
        idcliente, run,
        datos["nombre"], datos["apellido"], datos["direccion"],
        datos["telefono"], datos["correo"],
        tipo, monto, 0
    )

    if exito:
        print("\n[✔] INCORPORACIÓN EXITOSA [✔]")
        audit.registrar(usuario, "CREAR_CLIENTE", f"id={idcliente}, run={run}")
    else:
        print("\n[X] INCORPORACIÓN FALLIDA [X]")
        audit.registrar_error(usuario, "CREAR_CLIENTE", f"id={idcliente} ya existía")
    pausar()

def mostrar(usuario):
    opciones = {
        1: mostrartodo,
        2: mostraruno,
        3: mostrarparcial,
    }
    while True:
        g.menumostrar()
        op2 = int(v.leer_y_validar("Ingrese opcion: ", c.PATRON_NUMEROS, c.ERROR_NUMEROS))

        if op2 == 4:
            print("\nVolviendo al menú principal...")
            break
        elif op2 in opciones:
            opciones[op2](usuario)
        else:
            print("\nOpción fuera de rango (1-4)")
            pausar()

def mostrartodo(usuario=None):
    print("=================================\nMUESTRA DE TODOS LOS CLIENTES\n=================================")

    clientes = g.obtener_clientes()

    if not clientes:
        print("\nNo existen clientes registrados en el sistema todavía.")
    else:
        for id_cliente, cliente in clientes.items():
            imprimir_cliente(id_cliente, cliente)
    if usuario:
        audit.registrar(usuario, "CONSULTAR_CLIENTES", "mostrar todo")
    pausar()

def mostraruno(usuario=None):
    print("=================================\n            MUESTRA DE DATOS PARTICULAR\n=================================")

    runcliente_buscado = buscar_run("\nIngrese el RUN del Cliente que desea mostrar (Sin puntos ni guion, ej: 12345678K): ")
    cliente = g.buscar_cliente_por_run(runcliente_buscado)

    if cliente is None:
        print("\nError: El RUN ingresado no corresponde a ningún cliente registrado.")
    else:
        imprimir_cliente(cliente["id"], cliente)
        if usuario:
            audit.registrar(usuario, "CONSULTAR_CLIENTE", f"id={cliente['id']}")
    pausar()

def mostrarparcial(usuario=None):
    print("=======================================\n            MUESTRA PARCIALMENTE LOS CLIENTES\n=======================================")

    while True:
        cant = int(v.leer_y_validar("Ingrese la cantidad de clientes a mostrar: ", c.PATRON_NUMEROS, c.ERROR_NUMEROS))
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
    if usuario:
        audit.registrar(usuario, "CONSULTAR_CLIENTES", f"mostrar parcial cant={cant}")
    pausar()

def modifica(campo, valor_actual, patron=None, error="Entrada inválida."):
    opcion = v.leer_y_validar(f"¿Desea modificar {campo}? ({valor_actual}) [SI/NO]: ", c.PATRON_SI_NO, c.ERROR_SI_NO)
    if opcion.lower() == "si":
        return v.leer_y_validar(f"Ingrese nuevo {campo}: ", patron, error)
    return valor_actual

def modificardatos(usuario):
    print("\n" + "=" * 35 + "\n      MÓDULO MODIFICAR CLIENTE\n" + "=" * 35)

    mostrartodo(usuario)

    run_buscado = buscar_run("\nIngrese RUN del cliente a modificar: ")
    cliente = g.buscar_cliente_por_run(run_buscado)
    
    id_cliente = cliente["id"]
    
    if cliente is None:
        print("\n[X] Error: El RUN ingresado no existe. [X]")
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
        audit.registrar(usuario, "MODIFICAR_CLIENTE", f"id={id_cliente}")
    else:
        print("\n[X] ERROR AL ACTUALIZAR CLIENTE [X]")
        audit.registrar_error(usuario, "MODIFICAR_CLIENTE", f"id={id_cliente} no se pudo actualizar")
    pausar()

def eliminardatos(usuario):
    print("\n" + "=" * 35 + "\n      MÓDULO ELIMINAR CLIENTE\n" + "=" * 35)

    mostrartodo(usuario)

    run_buscado = buscar_run("\nIngrese valor de RUN del Cliente que desea Eliminar (Sin puntos ni guion, ej: 12345678K): ")
    cliente = g.buscar_cliente_por_run(run_buscado)

    if cliente is None:
        print("\n[X] Error: El RUN ingresado no existe. [X]")
        pausar()
        return

    elim = cliente["id"]   # <- el ID real, para pasarlo a eliminar_datos
    print(f"\nATENCIÓN: Va a eliminar al cliente: {cliente['nombre']} {cliente['apellido']} (ID: {cliente['id']})")

    confirmar = v.leer_y_validar("¿ESTÁ SEGURO DE ELIMINAR ESTE CLIENTE? [SI/NO]: ", c.PATRON_SI_NO, c.ERROR_SI_NO)

    if confirmar.lower() == "si":
        if g.eliminar_datos(elim):
            print("\n[✔] CLIENTE ELIMINADO EXITOSAMENTE [✔]")
            audit.registrar(usuario, "ELIMINAR_CLIENTE", f"id={cliente['id']}")
        else:
            print("\n[X] Error al eliminar cliente [X]")
            audit.registrar_error(usuario, "ELIMINAR_CLIENTE", f"id={cliente['id']} no se pudo eliminar")
    else:
        print("\nOperación cancelada.")
        audit.registrar(usuario, "ELIMINAR_CLIENTE_CANCELADO", f"id={cliente['id']}")
    pausar()