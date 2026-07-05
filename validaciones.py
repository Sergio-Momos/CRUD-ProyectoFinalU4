import re

#NO BORRAR NI MODIFICAR ESTA FUNCION EL 60% DEL CODIGO DEPENDE SOLAMENTE DE ESTO 
def leer_y_validar(mensaje, patron=None, error="Entrada inválida."):
    while True:
        try:
            entrada = input(mensaje).strip()
            if not entrada: 
                print("\n No dejes campos vacíos.")
                continue
            if len(entrada) > 30:
                print("Error: El texto no puede superar los 30 caracteres.")
                continue
            if patron and not re.match(patron, entrada): 
                print(f"\n {error}")
                continue
            return entrada
        except (KeyboardInterrupt, EOFError):
            print("\n\n Interrupción detectada. Por favor, ingresa los datos correctamente.")
            continue 

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