from pymongo import MongoClient


def TestearColeccion():
    try:
        client = MongoClient("mongodb://localhost:27017/")
        print("Bases de datos disponibles:", client.list_database_names())
    except Exception as e:
        print(f"Error: {e}")

def IniciarTienda(nombre):
    try:
        cliente = MongoClient("mongodb://localhost:27017/")
        db = cliente[nombre]
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
    resultado = list(tienda.find({"talles": "M"}))
    for p in resultado:
        print(f"{p['articulo']}", end=", ")
    print()
    return resultado

def PrecioPromedioPantalones(tienda):
    promedioagrupado = [
        {"$match": {"categoria": "Pantalones"}},
        {"$group": {"_id": None, "promedio": {"$avg": "$precio"}}}
    ]
    resultado = list(tienda.aggregate(promedioagrupado))
    print(f"Precio promedio en categoría pantalones: ${resultado[0]['promedio']:.2f}")

def ExisteEnNegro(tienda):
    print("Productos existentes en color negro:", end=" ")
    resultado = list(tienda.find({"colores": "Negro"}))
    for p in resultado:
        print(f"{p['articulo']}", end=", ")
    print()
    return resultado

def ConStockNoDisponible(tienda):
    print("Productos con stock que no están disponibles:", end="")
    resultado = list(tienda.find({"stock": {"$gt": 0}, "disponible": False}))
    for p in resultado:
        print(f"{p['articulo']}", end=", ")
    print()
    return resultado

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
        resultado = list(tienda.find({"stock": 0}))
        for p in resultado:
            print(f"{p['articulo']}", end=", ")
        print()
        return resultado

def EsParaRegalo(tienda):
    print("Propuestas para regalo (Precio menor a 30mil):")
    resultado = list(tienda.find({"precio": {"$lt": 30000}}))
    for p in resultado:
        print(f"{p['articulo']} — ${p['precio']}")
    return resultado

def ConsultasEspecificas(tienda):
    EsParaRegalo(tienda)
    NoHayStock(tienda)
    SiSeVendenTodosLosBuzos(tienda)
    ConStockNoDisponible(tienda)
    ExisteEnNegro(tienda)
    PrecioPromedioPantalones(tienda)
    ProductosTalleM(tienda)

#actualizaciones

def actualizarPrecios(tienda, porcentaje):
    nuevoPrecio = 1 + (porcentaje / 100)
    tienda.update_many({}, {"$mul": {"precio": nuevoPrecio}})
    print("Precios actualizados.")

def sumarStock(tienda, nombre_producto, cantidad):
    tienda.update_one({"articulo": nombre_producto}, {"$inc": {"stock": cantidad}})
    print(f"El stock de {nombre_producto} se incrementó en {cantidad} unidades.")

def iniciarBlackFriday(tienda):
    filtro = {"precio": {"$gt": 40000}}
    tienda.update_many(filtro, {"$mul": {"precio": 0.9}})
    print("Se hicieron los descuentos por Black Friday.")

def cambiarNombre(tienda, nombreViejo, nombreNuevo):
    tienda.update_one({"articulo": nombreViejo}, {"$set": {"articulo": nombreNuevo}})
    print(f"Nombre actualizado de {nombreViejo} a {nombreNuevo}.")

def renombrarCategoria(tienda, nombreViejo, nombreNuevo):
    tienda.update_many({"categoria": nombreViejo}, {"$set": {"categoria": nombreNuevo}})
    print(f"Categorías actualizada, nuevo nombre: {nombreNuevo}.")


def sobrestock(tienda):
    articuloConMasStock = tienda.find_one(sort=[("stock", -1)])

    if articuloConMasStock:
        idArticuloConMasStock = articuloConMasStock["_id"]
        nombre = articuloConMasStock["articulo"]
        tienda.update_one({"_id": idArticuloConMasStock}, {"$mul": {"precio": 0.8}})
        print(f"Por sobrestock se puso en descuento el artículo {nombre}")

def añadirColor(tienda, producto, color):
    tienda.update_one({"articulo": producto}, {"$addToSet": {"colores": color}})
    print("Color añadido a la lista.")

#main
if __name__ == "__main__":
    TestearColeccion()

    MiTienda = IniciarTienda("MiTienda")

    if MiTienda is not None:
        AgregarProductos(MiTienda)

        ConsultarProductos(MiTienda)

        ConsultasEspecificas(MiTienda)

        actualizarPrecios(MiTienda, 25)
        sumarStock(MiTienda, "Jean Clasico", 5)
        iniciarBlackFriday(MiTienda)
        cambiarNombre(MiTienda, "Remera Basica", "Remera Clásica")
        renombrarCategoria(MiTienda, "Deportivo", "Deportes")
        sobrestock(MiTienda)
        añadirColor(MiTienda, "Cardigan Tejido", "Negro")
        añadirColor(MiTienda, "Cardigan Tejido", "Beige")