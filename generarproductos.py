import json
import random


def generar_dataset_json():
    articulos = ["Jean", "Remera", "Buzo", "Campera", "Short", "Vestido", "Falda", "Camisa", "Top", "Cardigan"]
    estilos = ["Clasico", "Oversize", "Slim Fit", "Vintage", "Deportivo", "Urbano"]
    colores_disponibles = ["Negro", "Blanco", "Azul", "Rojo", "Verde", "Gris", "Beige"]
    categorias = ["Pantalones", "Remeras", "Buzos", "Abrigos", "Vestidos", "Faldas", "Deportivo"]

    dataset = []

    for i in range(50):
        producto = {
            "articulo": f"{random.choice(articulos)} {random.choice(estilos)}",
            "categoria": random.choice(categorias),
            "precio": random.randint(15000, 150000),
            "stock": random.randint(0, 100),
            "talles": ["S", "M", "L", "XL"],
            "colores": random.sample(colores_disponibles, k=random.randint(1, 3)),
            "disponible": True
        }

        if producto["stock"] == 0:
            producto["disponible"] = False

        dataset.append(producto)

    with open("TiendaRopa.json", "w") as file:
        json.dump(dataset, file, indent=4)
    print("Archivo 'TiendaRopa.json' generado con éxito.")

generar_dataset_json()