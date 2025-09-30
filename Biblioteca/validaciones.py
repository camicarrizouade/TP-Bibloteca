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
    return re.match(r"\d{7,8}", normalizar_texto(dni)) is not None

def validar_fecha_ymd(fecha) -> bool:
    """AAAA-MM-DD (solo formato)."""
    s = normalizar_texto(fecha)
    return re.match(r"\d{4}-\d{2}-\d{2}", s) is not None


