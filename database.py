from pymongo import MongoClient


def TestearColeccion():
    try:
        client = MongoClient("mongodb://localhost:27017/")
        print("Bases de datos disponibles:", client.list_database_names())
    except Exception as e:
        print(f"Error: {e}")

def IniciarTienda():
    try:
        cliente = MongoClient("mongodb://localhost:27017/")
        db = cliente["TiendaRopaDB"]
        coleccion = db["productos"]

        print("Se creó la base de datos TiendaRopaDB con su colección productos.")
        return coleccion

    except Exception as e:
        print(f"Error: {e}")


def AgregarProductos(coleccion):
    try:
        # Punto 3: Insertar documentos manualmente
        productos = [
            {"articulo": "Jean Clasico", "categoria": "Pantalones", "precio": 32000, "stock": 20,
             "talles": [38, 40, 42, 44], "colores": ["Azul"], "disponible": True},
            {"articulo": "Remera Basica", "categoria": "Remeras", "precio": 15000, "stock": 50,
             "talles": ["S", "M", "L", "XL"], "colores": ["Blanco", "Negro", "Gris"], "disponible": True},
            {"articulo": "Vestido Floral", "categoria": "Vestidos", "precio": 45000, "stock": 15,
             "talles": ["S", "M", "L"], "colores": ["Rosa", "Celeste"], "disponible": True},
            {"articulo": "Campera de Cuero", "categoria": "Abrigos", "precio": 120000, "stock": 8,
             "talles": ["M", "L", "XL"], "colores": ["Negro", "Marron"], "disponible": True},
            {"articulo": "Short Jean", "categoria": "Pantalones", "precio": 28000, "stock": 30,
             "talles": [36, 38, 40, 42], "colores": ["Azul", "Blanco"], "disponible": True},
            {"articulo": "Buzo Hoodie", "categoria": "Buzos", "precio": 55000, "stock": 25,
             "talles": ["S", "M", "L", "XL", "XXL"], "colores": ["Negro", "Gris", "Verde"], "disponible": True},
            {"articulo": "Falda Plisada", "categoria": "Faldas", "precio": 32000, "stock": 0, "talles": ["S", "M"],
             "colores": ["Negro"], "disponible": False},
            {"articulo": "Camisa Oxford", "categoria": "Camisas", "precio": 38000, "stock": 20,
             "talles": ["S", "M", "L", "XL"], "colores": ["Blanco", "Celeste", "Rosa"], "disponible": True},
            {"articulo": "Pantalon de Vestir", "categoria": "Pantalones", "precio": 62000, "stock": 12,
             "talles": [38, 40, 42, 44, 46], "colores": ["Negro", "Gris", "Beige"], "disponible": True},
            {"articulo": "Top Deportivo", "categoria": "Deportivo", "precio": 18000, "stock": 40,
             "talles": ["XS", "S", "M", "L"], "colores": ["Negro", "Rosa", "Azul"], "disponible": True},
            {"articulo": "Cardigan Tejido", "categoria": "Buzos", "precio": 72000, "stock": 5,
             "talles": ["S", "M", "L"], "colores": ["Beige", "Blanco"], "disponible": False}
        ]

        coleccion.insert_many(productos)
        print(f"Se cargaron los productos correctamente.")

        cliente_actual = coleccion.database.client
        print("Bases de datos actuales:", cliente_actual.list_database_names())

    except Exception as e:
        print(f"Error: {e}")


def ConsultarProductos(coleccion):
    try:
        print("Lista de productos:")
        resultados = coleccion.find()

        for producto in resultados:
            print(producto)

    except Exception as e:
        print(f"Error al consultar: {e}")

def ProductosTalleM(tienda):
    print("Productos disponibles en talle M:", end=" ")
    for p in tienda.find({"talles": "M"}):
        print(f"{p['articulo']}", end=", ")
    print()

def PrecioPromedioPantalones(tienda):
    promedioagrupado = [
        {"$match": {"categoria": "Pantalones"}},
        {"$group": {"_id": None, "promedio": {"$avg": "$precio"}}}
    ]
    resultado = list(tienda.aggregate(promedioagrupado))
    print(f"Precio promedio en categoría pantalones: ${resultado[0]['promedio']:.2f}")

def ExisteEnNegro(tienda):
    print("Productos existentes en color negro:", end=" ")
    for p in tienda.find({"colores": "Negro"}):
        print(f"{p['articulo']}", end=", ")
    print()

def ConStockNoDisponible(tienda):
    print("Productos con stock que no están disponibles:", end="")
    for p in tienda.find({"stock": {"$gt": 0}, "disponible": False}):
        print(f"{p['articulo']}", end=", ")
    print()

def SiSeVendenTodosLosBuzos(tienda):
    sumaagregada = [
        {"$match": {"categoria": "Buzos"}},
        {"$project": {"total_producto": {"$multiply": ["$precio", "$stock"]}}},
        {"$group": {"_id": None, "total_general": {"$sum": "$total_producto"}}}
    ]
    resultado = list(tienda.aggregate(sumaagregada))
    print(f"Ganancia total si se vende el stock completo de buzos: ${resultado[0]['total_general']}")

def NoHayStock(tienda):
        print("\nProductos sin stock:", end=" ")
        for p in tienda.find({"stock": 0}):
            print(f"{p['articulo']}", end=", ")
        print()

def EsParaRegalo(tienda):
    print("Propuestas para regalo (Precio menor a 30mil):")
    for p in tienda.find({"precio": {"$lt": 30000}}):
        print(f"{p['articulo']} — ${p['precio']}")

#main
if __name__ == "__main__":
    TestearColeccion()

    MiTienda = IniciarTienda()

    if MiTienda is not None:
        AgregarProductos(MiTienda)
        ConsultarProductos(MiTienda)

        EsParaRegalo(MiTienda)
        NoHayStock(MiTienda)
        SiSeVendenTodosLosBuzos(MiTienda)
        ConStockNoDisponible(MiTienda)
        ExisteEnNegro(MiTienda)
        PrecioPromedioPantalones(MiTienda)
        ProductosTalleM(MiTienda)

