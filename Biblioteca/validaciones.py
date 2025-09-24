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
