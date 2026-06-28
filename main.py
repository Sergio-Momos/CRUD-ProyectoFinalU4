import grupoFunciones as g
import clientes as c
import usuarios as u

"""La función ingresoUusarios, cumple con todo lo que debiese tener
una buena función, merezco el cielo"""


def menu_principal():
    while True:
        g.menuprincipal()
        op = int(input("INGRESE OPCIÓN: "))

        if op == 1:
            c.ing_cliente()
        elif op == 2:
            c.mostrar()
        elif op == 3:
            c.modificardatos()
        elif op == 4:
            c.eliminardatos()
        elif op == 5:
            if input("¿Salir? ").lower() == "si":
                break
        else:
            print("Opción fuera de rango")

def main():
    while True:
        g.menu_usuarios()
        op_usu = int(input("INGRESE OPCIÓN: "))
        if op_usu == 1:
            usuario = u.login()
            if usuario:
                print(f"Bienvenido {usuario[3]}")
                menu_principal()
        elif op_usu == 2:
            u.ing_usuario()
        elif op_usu == 3:
            op_salir = input("¿DESEA SALIR [SI/NO]: ")
            if op_salir.lower() == "si":
                break
        else:
            print("Opción Fuera de Rango")
if __name__ == "__main__":   
    main()