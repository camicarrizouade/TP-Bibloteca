def linea(anchos, relleno="-", sep="+"):
    """Devuelve una línea separadora según los anchos."""
    return sep + sep.join(relleno * (w + 2) for w in anchos) + sep

def mostrar_tabla(encabezados, rows, bool_cols=None):
    """
    Imprime una tabla genérica.
    - encabezados: lista de encabezados.
    - rows: matriz (listas por fila).
    - bool_cols: set de índices a mostrar como 'Sí'/'No'.
    """
    if not rows:
        print("No hay registros.\n"); return

    bool_cols = set() if bool_cols is None else set(bool_cols)
    cols = len(encabezados)
    # normaliza filas al # de columnas
    norm = [r[:cols] + [""] * max(0, cols - len(r)) for r in rows]

    # anchos
    widths = [len(str(h)) for h in encabezados]
    for r in norm:
        for c in range(cols):
            v = r[c]
            s = "Sí" if (c in bool_cols and (v is True or v is False)) else str(v)
            widths[c] = max(widths[c], len(s))

    # encabezado
    print(linea(widths))
    print("| " + " | ".join(str(encabezados[c]).ljust(widths[c]) for c in range(cols)) + " |")
    print(linea(widths, relleno="=", sep="+"))

    # filas
    for r in norm:
        celdas = []
        for c in range(cols):
            v = r[c]
            s = "Sí" if (c in bool_cols and (v is True or v is False)) else str(v)
            celdas.append(s.rjust(widths[c]) if s.isdigit() else s.ljust(widths[c]))
        print("| " + " | ".join(celdas) + " |")

    print(linea(widths))
    print()