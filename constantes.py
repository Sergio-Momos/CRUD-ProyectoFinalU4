#Patrones de regex
PATRON_NUMEROS = r"^\d+$"
PATRON_RUN = r"^\d{7,8}[0-9kK]$"
PATRON_NOMBRE = r"^[a-zA-ZáéíóúÁÉÍÓÚÑñ\s'-]+$"
PATRON_CORREO = r"^[\w.-]+@[\w.-]+\.[a-zA-Z]{2,}$"
PATRON_TELEFONO = r"^\d{8,9}$"
PATRON_SI_NO = r"^(si|no)$"
PATRON_USER = r"^[a-zA-Z0-9_]+$"

#Mensajes de error
ERROR_NUMEROS = "Debe ser número."
ERROR_SOLO_LETRAS = "Solo letras."
ERROR_CORREO = "Correo inválido."
ERROR_TELEFONO = "Debe tener 8 o 9 números."
ERROR_SI_NO = "Responda SI o NO."
ERROR_USER = "Solo letras, números y guión bajo."
ERROR_RUN = "Formato incorrecto"

TIPOS = {
    101: "Plata",
    102: "Oro",
    103: "Platino"
}