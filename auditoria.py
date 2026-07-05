import logging
import os

# El log se guarda en una carpeta 'logs' junto al resto del proyecto.
LOG_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "logs")
os.makedirs(LOG_DIR, exist_ok=True)
LOG_FILE = os.path.join(LOG_DIR, "auditoria.log")

logger = logging.getLogger("auditoria")
logger.setLevel(logging.INFO)

# Evita duplicar handlers si el módulo se importa más de una vez.
if not logger.handlers:
    formato = logging.Formatter(
        fmt="%(asctime)s | %(levelname)s | %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S"
    )
    handler = logging.FileHandler(LOG_FILE, encoding="utf-8")
    handler.setFormatter(formato)
    logger.addHandler(handler)


def registrar(usuario, accion, detalle=""):
    """
    Registra una accion exitosa en el log de auditoría.
    Ej: registrar("jperez", "CREAR_CLIENTE", "id=5, run=12345678-9")
    """
    mensaje = f"USUARIO={usuario} | ACCION={accion}"
    if detalle:
        mensaje += f" | DETALLE={detalle}"
    logger.info(mensaje)


def registrar_error(usuario, accion, error):
    """
    Registra un fallo o error ocurrido durante una acción.
    Ej: registrar_error("jperez", "ELIMINAR_CLIENTE", "id=5 no existe")
    """
    mensaje = f"USUARIO={usuario} | ACCION={accion} | ERROR={error}"
    logger.error(mensaje)