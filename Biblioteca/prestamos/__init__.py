from .crear_prestamos import crear_prestamo
from .prestamos import listar_prestamos, buscar_prestamo_por_id
from .modificar_prestamo import actualizar_prestamo
from .baja_prestamo import bajar_prestamo

__all__ = [
    "crear_prestamo", "listar_prestamos", "buscar_prestamo_por_id",
    "actualizar_prestamo", "bajar_prestamo",
]
