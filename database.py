from pymongo import MongoClient

try:
    cliente = MongoClient("mongodb://localhost:27017/")
    db = cliente["TiendaRopaDB"]
    coleccion = db["productos"]

    productos = [
        {"articulo": "Jean Clasico", "categoria": "Pantalones", "precio": 32000, "stock": 20, "talles": [38, 40, 42, 44], "colores": ["Azul"], "disponible": True},
        {"articulo": "Remera Basica", "categoria": "Remeras", "precio": 15000, "stock": 50, "talles": ["S", "M", "L", "XL"], "colores": ["Blanco", "Negro", "Gris"], "disponible": True},
        {"articulo": "Vestido Floral", "categoria": "Vestidos", "precio": 45000, "stock": 15, "talles": ["S", "M", "L"], "colores": ["Rosa", "Celeste"], "disponible": True},
        {"articulo": "Campera de Cuero", "categoria": "Abrigos", "precio": 120000, "stock": 8, "talles": ["M", "L", "XL"], "colores": ["Negro", "Marron"], "disponible": True},
        {"articulo": "Short Jean", "categoria": "Pantalones", "precio": 28000, "stock": 30, "talles": [36, 38, 40, 42], "colores": ["Azul", "Blanco"], "disponible": True},
        {"articulo": "Buzo Hoodie", "categoria": "Buzos", "precio": 55000, "stock": 25, "talles": ["S", "M", "L", "XL", "XXL"], "colores": ["Negro", "Gris", "Verde"], "disponible": True},
        {"articulo": "Falda Plisada", "categoria": "Faldas", "precio": 32000, "stock": 0, "talles": ["S", "M"], "colores": ["Negro"], "disponible": False},
        {"articulo": "Camisa Oxford", "categoria": "Camisas", "precio": 38000, "stock": 20, "talles": ["S", "M", "L", "XL"], "colores": ["Blanco", "Celeste", "Rosa"], "disponible": True},
        {"articulo": "Pantalon de Vestir", "categoria": "Pantalones", "precio": 62000, "stock": 12, "talles": [38, 40, 42, 44, 46], "colores": ["Negro", "Gris", "Beige"], "disponible": True},
        {"articulo": "Top Deportivo", "categoria": "Deportivo", "precio": 18000, "stock": 40, "talles": ["XS", "S", "M", "L"], "colores": ["Negro", "Rosa", "Azul"], "disponible": True},
        {"articulo": "Cardigan Tejido", "categoria": "Buzos", "precio": 72000, "stock": 5, "talles": ["S", "M", "L"], "colores": ["Beige", "Blanco"], "disponible": False}
    ]

    resultado = coleccion.insert_many(productos)
    print(f"Se cargaron los productos correctamente.")
    print("Bases de datos actuales:", cliente.list_database_names())


    

except Exception as e:
    print(f"Error: {e}")