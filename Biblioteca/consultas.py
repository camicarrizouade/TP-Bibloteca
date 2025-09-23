def _linea(anchos, relleno="-", sep="+"):
    return sep + sep.join(relleno * (w + 2) for w in anchos) + sep

def mostrar_tabla(encabezados, rows, bool_cols=None, num_cols=None):
    """
    Imprime tabla genérica sin sorpresas.
      - encabezados: lista de strings
      - rows: matriz (listas/tuplas por fila)
      - bool_cols: set de índices a mostrar como 'Sí'/'No'
      - num_cols : índices a alinear a la derecha
    """
    if not rows:
        print("No hay registros.\n"); return

    bool_cols = set() if bool_cols is None else set(bool_cols)
    num_cols  = set() if num_cols  is None else set(num_cols)

    cols = len(encabezados)

    # normaliza filas al nº de columnas (asumimos rows = listas de listas)
    norm = [r[:cols] + [""] * max(0, cols - len(r)) for r in rows]

    def _formato(v, c): 
        #formatos en lineas indicadas
        if c in bool_cols and (v is True or v is False):
            return "Sí" if v else "No"
        return str(v)

    # anchos
    widths = [len(str(h)) for h in encabezados]
    for r in norm:
        for c in range(cols):
            s = _formato(r[c], c)
            if len(s) > widths[c]:
                widths[c] = len(s)

    # encabezado
    print(_linea(widths))
    print("| " + " | ".join(str(encabezados[c]).ljust(widths[c]) for c in range(cols)) + " |")
    print(_linea(widths, relleno="=", sep="+"))

    # filas (num_cols a derecha; resto a izquierda)
    for r in norm:
        celdas = []
        for c in range(cols):
            s = _formato(r[c], c)
            celdas.append(s.rjust(widths[c]) if c in num_cols else s.ljust(widths[c]))
        print("| " + " | ".join(celdas) + " |")

    print(_linea(widths)); 
print()