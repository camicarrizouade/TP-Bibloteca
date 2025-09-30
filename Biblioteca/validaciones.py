import re

# ---- Helpers genéricos y validaciones simples para modulo de libros ----

def normalizar_texto(x):
    """Devuelve str(x).strip() o '' si es None."""
    return ("" if x is None else str(x)).strip()

def texto_no_vacio(x) -> bool:
    """True si, tras normalizar, queda algo."""
    return normalizar_texto(x) != ""

def entero_positivo(x) -> bool:
    """True si es dígito y > 0."""
    s = normalizar_texto(x)
    return s.isdigit() and int(s) > 0

def entero_no_negativo(x) -> bool:
    """True si es dígito y >= 0."""
    s = normalizar_texto(x)
    return s.isdigit() and int(s) >= 0

# Validadores “de campo” para Libros (alias semánticos)
validar_titulo   = texto_no_vacio
validar_autor    = texto_no_vacio
validar_genero   = texto_no_vacio
validar_anio     = entero_positivo
validar_totales  = entero_positivo


# --- Regex / campos compuestos ---
def validar_dni(dni) -> bool:
    """7 u 8 dígitos, sin puntos ni letras."""
    return re.fullmatch(r"\d{7,8}", normalizar_texto(dni)) is not None

def existe_valor(matriz, col_valor, valor, *, col_id=None, excluir_id=None, col_activo=None, solo_activos=True) -> bool:
    """
    True si 'valor' ya está en la columna 'col_valor'.
    - col_id/excluir_id: para ignorar una fila (cuando actualizás).
    - col_activo: si se pasa y solo_activos=True, ignora las filas inactivas.
    """
    objetivo = normalizar_texto(valor)
    for fila in matriz:
        if col_activo is not None and solo_activos and not fila[col_activo]:
            continue
        if normalizar_texto(fila[col_valor]) != objetivo:
            continue
        if col_id is not None and excluir_id is not None and fila[col_id] == excluir_id:
            continue
        return True
    return False
