import grupoFunciones as g
import clientes as c
import usuarios as u

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

def menu_principal():
    while True:
        try:
            g.menuprincipal()
            op = validar_opcion("INGRESE OPCIÓN: ", 1, 5)
            if op == 1:
                c.ing_cliente()
            elif op == 2:
                c.mostrar()
            elif op == 3:
                c.modificardatos()
            elif op == 4:
                c.eliminardatos()
            elif op == 5:
                break
        except Exception as error:
            print(f"Error inesperado: {error}")

def main():
    while True:
        try:
            g.menu_usuarios()
            op_usu = validar_opcion("INGRESE OPCIÓN: ", 1, 3)

            if op_usu == 1:
                usuario = u.login()
                if usuario:
                    print(f"Bienvenido {usuario["username"]}")
                    menu_principal()

            elif op_usu == 2:
                u.ing_usuario()

            elif op_usu == 3:
                op_salir = input("¿DESEA SALIR [SI/NO]: ")
                if op_salir.lower() == "si":
                    break

        except Exception as error:
            print(f"Error inesperado: {error}")
if __name__ == "__main__":   
    main()