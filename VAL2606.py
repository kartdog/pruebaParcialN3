# funciones de ejercicio.
# grabar, buscar, retirarse.

num_id = 1
acum_id = 0

lista_habitacion = [[1,2,3,4,5],[6,7,8,9,10]]
lista_numHab = []
lista_rut = []
lista_id = []
lista_cantidad = []

def fun_habit():
    cont = 0
    num = 1
    acum = 0
    print("FILA")
    print("|")
    print("V")
    for x in range(2):
        acum += num
        print(acum, "" ,end = "")
        for y in range(5):
            print(lista_habitacion[x][y], end = "")
        print()
    print("  12345", " <- COLUMNA")
    print("")

    for x in range(2):
        for y in range(5):
            if lista_habitacion[x][y] == 'X':
                cont += 1
    
    while True:
        if cont == 10:
            print("Todas las habitaciones estan ocupadas.")
        else:
            while True:
                try:
                    opcion_fila = int(input("Elija fila: "))
                    if opcion_fila in (1,2):
                        break
                    else:
                        print("ERROR! elija una opción válida.")
                except:
                    print("ERROR! ingrese un número entero.")

            while True:
                try:
                    opcion_columna = int(input("Elija columna: "))
                    if opcion_columna in (1,2,3,4,5):
                        break
                    else:
                        print("ERROR! elija una opción válida.")
                except:
                    print("ERROR! debe ingresar un número entero.")

            if lista_habitacion[opcion_fila-1][opcion_columna-1] == 'X':
                print("ERROR! la habitación esta ocupada.")
            else:
                val_original = lista_habitacion[opcion_fila-1][opcion_columna-1]
                lista_numHab.append(val_original)
                lista_habitacion[opcion_fila-1][opcion_columna-1] = 'X'
                break

def fun_id():
    acum = 0 
    num = 1
    acum += num
    lista_id.append(acum)

def fun_grabar():
    rut = val_rut()
    lista_rut.append(rut)

    nombre_dueno = val_nombre()
    id_unico = fun_id()
    nombre_mascot = val_nombre_mascot()

    cantidad_dias = val_cantidad(1,366)
    lista_cantidad.append(cantidad_dias)

    habitaciones = fun_habit()
    print(">> Registrado exitosamente.")

def fun_buscar():
    rut = val_rut()
    if rut in lista_rut:
        index_rut = lista_rut.index(rut)
        index_hab = lista_numHab[index_rut]
        print(">> Su mascota se hospeda en la habitación #", index_hab)

def fun_retirarse():
    rut = val_rut()
    if rut in lista_rut:
        index_rut = lista_rut.index(rut)
        total_dias = (lista_cantidad[index_rut])
        print(">> Su total a pagar es:", total_dias * 15000)
        lista_rut.pop(index_rut)
        lista_cantidad.pop(index_rut)
        lista_id.pop(index_rut)
        lista_numHab.pop(index_rut)
        print(">> Retirado exitosamente.")

# validaciones.
# rut, nombre, correo, opciones, cantidad, telefono...

def val_rut():
    while True:
        try:
            rut = int(input("Ingrese rut: "))
            if rut >= 1000000 and rut <= 99999999:
                return rut
            else:
                print("ERROR! ingrese un rut válido.")
        except:
            print("ERROR! ingrese un número entero.")

def val_nombre():
    while True:
        nombre = input("Ingrese nombre: ")
        if nombre.isalpha and len(nombre.strip()) >= 3:
            return nombre
        else:
            print("ERROR! ingrese un nombre válido.")

def val_nombre_mascot():
    while True:
        nombre = input("Ingrese nombre de mascota: ")
        if nombre.isalpha and len(nombre.strip()) >= 3:
            return nombre
        else:
            print("ERROR! ingrese un nombre válido.")

def val_correo():
    while True:
        correo = input("Ingrese correo: ")
        if '@' in correo:
            return correo
        else:
            print("ERROR! ingrese un correo válido.")

def val_opcion():
    while True:
        try:
            opcion = int(input("Ingrese opción: "))
            if opcion in (1,2,3,4):
                return opcion
            else:
                print("ERROR! ingrese opción válida.")
        except:
            print("ERROR! ingrese un número entero.")

def val_cantidad(a,b):
    while True:
        try:
            cantidad = int(input("Ingrese cantidad: "))
            if cantidad >= a and cantidad <= b:
                return cantidad
            else:
                print("ERROR! ingrese una cantidad válida.")
        except:
            print("ERROR! ingrese un número entero.")

def val_telefono():
    while True:
        try:
            telefono = input("Ingrese número telefonico: ")
            if telefono.isnumeric() and len(telefono) == 9:
                return telefono
            else:
                print("ERROR! ingrese número válido.")
        except:
            print("ERROR! ingrese número entero.")

def val_fila():
    while True:
        try:
            opcion_fila = int(input("Elija fila: "))
            if opcion_fila in (1,2):
                return opcion_fila
            else:
                print("ERROR! elija una opción válida.")
        except:
            print("ERROR! ingrese un número entero.")

def val_columna():
    while True:
        try:
            opcion_columna = int(input("Elija columna: "))
            if opcion_columna in (1,2,3,4,5):
                return opcion_columna
            else:
                print("ERROR! elija una opción válida.")
        except:
            print("ERROR! debe ingresar un número entero.")