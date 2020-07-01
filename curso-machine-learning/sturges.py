""""Esta funcion calcula el numero de bins a partir de la regla de Sturges"""
def bins(tamanio):
    import numpy as np
    c = 1 + np.log2(tamanio)
    part_entera = c//1
    if part_entera%2 == 0:
        c = np.ceil(c)
    else:
        c = np.floor(c)
    return int(c)