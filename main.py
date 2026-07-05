import grupoFunciones as g
import clientes as c
import usuarios as u
import auditoria as audit

def validar_opcion(mensaje, minimo, maximo):
    while True:
        try:
            opcion = int(input(mensaje))

            if minimo <= opcion <= maximo:
                return opcion
            else:
                print(f"Opción fuera de rango ({minimo}-{maximo})")

        except ValueError:
            print("Debe ingresar un número válido.")

        except (KeyboardInterrupt, EOFError):
            print("\nNO intente usar comandos de teclado: Control + C / Control + Z.")

def menu_principal(usuario):
    while True:
        try:
            g.menuprincipal()
            op = validar_opcion("INGRESE OPCIÓN: ", 1, 5)
            if op == 1:
                c.ing_cliente(usuario)
            elif op == 2:
                c.mostrar(usuario)
            elif op == 3:
                c.modificardatos(usuario)
            elif op == 4:
                c.eliminardatos(usuario)
            elif op == 5:
                audit.registrar(usuario, "LOGOUT")
                break
        except Exception as error:
            audit.registrar_error(usuario, "ERROR_MENU_PRINCIPAL", error)
            print(f"Error inesperado: {error}")

def main():
    while True:
        try:
            g.menu_usuarios()
            op_usu = validar_opcion("INGRESE OPCIÓN: ", 1, 3)

            if op_usu == 1:
                usuario = u.login()
                if usuario:
                    print(f"Bienvenido {usuario['username']}")
                    menu_principal(usuario["username"])
            elif op_usu == 2:
                u.ing_usuario()

            elif op_usu == 3:
                op_salir = input("¿DESEA SALIR [SI/NO]: ")
                if op_salir.lower() == "si":
                    break

        except Exception as error:
            audit.registrar_error("SISTEMA", "ERROR_MENU_USUARIOS", error)
            print(f"Error inesperado: {error}")
if __name__ == "__main__":   
    main()