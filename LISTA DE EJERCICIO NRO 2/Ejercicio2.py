Biblioteca={"categorias":{
            "Cientificos":{"titulo":"Somos nuestro cerebro",
                              "autor":"Dick Swaab",
                              "estado":"disponible"},
            "Romance":    {"titulo":"Romeo y Julieta",
                              "autor":"William Shakespeare",
                              "estado":"disponible"},
            "Comic":     {"titulo":"Spiderman",
                              "autor":"Stan lee",
                              "estado":"disponible"},
            "Biograficos": {"titulo":"Vida Interna",
                                "autor":"Dora Mayor",
                                "estado": "disponible"} ,
            "Usuarios":     ["Alum001", "Alum002", "Alum003", "Alum004"]
}  
}                    

opcion=0
while opcion != 5:
    print("Menú de la biblioteca:")
    print("1. Consultar Cartegorias de libros")
    print("2. Nombres de los libros y autores")
    print("3. Prestarse un libro")
    print("4. Usuarios")
    print("5. Salir")
    opcion = int(input("Selecciona una de las opciones dadas: "))
    
    if opcion == 1:
        categorias=list(Biblioteca["categorias"].keys())
        print("Las Categorias de libros son:")
        for A in categorias:
            print("-",A)

    elif opcion == 2:
        for B in categorias:
            print(B)
        categoria=input("Ingrese categoria a consultar: ")
        for a,b in Biblioteca["categorias"][categoria].items():
            print(a,":", b)

    elif opcion == 3:
        for C in categorias:
            print(C)
        categoria=input("Ingrese el libro a prestarse: ")
        for a,b in Biblioteca["categorias"][categoria].items():
            print(a,":", b)
        Respuesta=["si"]
        Prestado=input("Se prestara el libro? (si/no): ")
        if Prestado in Respuesta:
            UsuarioPrestado=input("ingrese el usuario: ")
        Biblioteca["categorias"][categoria]["estado"]="prestado"+"-"+UsuarioPrestado
        print("Se actualizo estado del libro")
        for k,v in Biblioteca["categorias"][categoria].items():
            print(k,":", v)
        else:
            print("fin de la consulta")

    elif opcion == 4:
        print("Lista de Usuarios actuales:")
        print(Biblioteca["categorias"]["Usuarios"])

    elif opcion == 5:
        print("Programa terminado \n Gracias")

    else:
        print("ERROR \n Vuelva a digitar una opcion")
