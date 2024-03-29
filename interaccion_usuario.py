#encoding: latin1

def ingresar_numero(numero_minimo, numero_maximo):
    ''' Muestra un cursor de ingreso al usuario para que ingrese un numero
    tal que numero_minimo <= ingreso <= numero_maximo. Ante un ingreso
    invalido muestra un mensaje descriptivo de error y repregunta.
    Devuelve el numero ingresado en formato entero.
    '''
    while True:
        ingreso = input()
        if not ingreso.isdigit():
            print ("El ingreso debe ser numerico.")
        elif not numero_minimo <= int(ingreso) <= numero_maximo:
            print ("El ingreso debe estar entre {} y {}".format(numero_minimo, numero_maximo))
        else:
            return int(ingreso)


def ingresar_cadena_no_vacia():
    ''' Muestra un cursor de ingreso al usuario para que ingrese una cadena
    no vacia. Ante un ingreso invalido muestra un mensaje descriptivo de
    error y repregunta.
    Devuelve la cadena ingresada, en mayusculas.
    '''
    while True:
        ingreso = input()
        if len(ingreso) == 0:
            print ("El ingreso no debe ser vacio.")
        else:
            return ingreso.upper()


def mostrar_menu_generico(opciones, opcion_por_defecto):
    ''' Muestra una pantalla de selección dada una lista de opciones y una
    opción por defecto. El usuario tendrá la opción de elegir una opción de
    acuerdo a la numeración mostrada, generada por la función. Se valida el
    ingreso repreguntando tantas veces como sea necesario.
        opciones es una lista de cadena con las opciones a mostrar.
    opcion_por_defecto es una opción adicional, obligatoria, no incluida en
    la lista de opciones. Se mostrará última y su uso se orienta a una
    opción de tipo "cancelar".
        Se devuelve un número entero según la elección del usuario. Si
    selecciona un elemento de la lista de opciones, devuelve su índice. Si
    selecciona la opción por defecto, devuelve -1.
    '''
    print ("Seleccione una opción:")
    for numero_opcion in range(len(opciones)):
        print ("{}, {}".format(numero_opcion + 1, opciones[numero_opcion]))
    print ("{}, {}.".format(len(opciones) + 1, opcion_por_defecto))
    print

    seleccion = ingresar_numero(1, len(opciones) + 1)

    # Caso en el que elija la opcion por defecto.
    if seleccion == len(opciones) + 1:
        return -1

    # Caso en el que elija una opcion dentro de la lista.
    return seleccion - 1
