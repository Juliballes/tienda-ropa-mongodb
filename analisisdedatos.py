from database import *
import json
import pandas as pd

def DevolverComoCSV(lista, nombre):
    if lista:
        df = pd.DataFrame(lista)

        df.to_csv(nombre + ".csv", index=False)

        print("Archivo generado.")

    else:
        print("La lista esta vacía.")

def RemerasDisponiblesEnTalleM(tienda):
    print("Remeras disponibles en talle M:", end=" ")

    resultado = list(tienda.find({
        "categoria": "Remeras",
        "talles": "M",
        "disponible": True
    }))

    for p in resultado:
        print(f"{p['articulo']}", end=", ")

    print()
    return resultado

def CategoriasEnNegro(tienda):
    print("Categorías con stock en color negro:", end=" ")

    resultado = list(tienda.aggregate([
        {"$match": {"colores": "Negro"}},
        {"$group": {"_id": "$categoria"}}
    ]))

    for cat in resultado:
        print(f"{cat}", end=", ")

    print()
    return resultado


def NoHayStock(tienda, prod):

    resultado = list(tienda.find({
        "articulo": {"$regex": "^" + prod},
        "stock": 0
    }))

    print(prod + " sin Stock:")
    for p in resultado:
        print(f"{p['articulo']}", end=", ")

    return resultado


def EsParaRegaloClasico(tienda):
    print("Propuestas para regalo:")

    resultado = list(tienda.find({
        "articulo": {"$regex": "Clásico$"},
        "precio": {"$lt": 30000}
    }))

    for p in resultado:
        print(f"{p['articulo']} — ${p['precio']}")

    return resultado

nuevaTienda = IniciarTienda("NuevaTienda")

with open("TiendaRopa.json") as file:
    data = json.load(file)
    nuevaTienda.insert_many(data)

    print("Datos cargados correctamente.")


CategoriasColorNegro = CategoriasEnNegro(nuevaTienda)
DevolverComoCSV(CategoriasColorNegro, "CategoriasColorNegro")

RemerasTalleM = RemerasDisponiblesEnTalleM(nuevaTienda)
DevolverComoCSV(RemerasTalleM, "RemerasTalleM")

FaldasSinStock = NoHayStock(nuevaTienda, "Falda")
DevolverComoCSV(FaldasSinStock, "FaldasSinStock")

ProductosParaRegalar = EsParaRegaloClasico(nuevaTienda)
DevolverComoCSV(ProductosParaRegalar, "ProductosParaRegalar")

ProductosConStockNoDisponible = ConStockNoDisponible(nuevaTienda)
DevolverComoCSV(ProductosConStockNoDisponible, "ProductosConStockNoDisponible")