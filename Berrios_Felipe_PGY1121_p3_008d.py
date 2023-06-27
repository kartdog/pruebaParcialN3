import VAL2606 as fn

while True:
    print("Mascota Segura")
    print("1. GRABAR")
    print("2. BUSCAR")
    print("3. RETIRARSE")
    print("4. SALIR")

    opcion = fn.val_opcion()

    if opcion == 1:
        fn.fun_grabar()
    elif opcion == 2:
        fn.fun_buscar()
    elif opcion == 3:
        fn.fun_retirarse()
    else:
        break