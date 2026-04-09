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

nuevaTienda = IniciarTienda("NuevaTienda")

with open("TiendaRopa.json") as file:
    data = json.load(file)
    nuevaTienda.insert_many(data)

    print("Datos cargados correctamente.")


ProductosColorNegro = ExisteEnNegro(nuevaTienda)
DevolverComoCSV(ProductosColorNegro, "ProductosColorNegro")

ProductosTalleM = ProductosTalleM(nuevaTienda)
DevolverComoCSV(ProductosTalleM, "ProductosTalleM")

ProductosSinStock = NoHayStock(nuevaTienda)
DevolverComoCSV(ProductosSinStock, "ProductosSinStock")

ProductosParaRegalar = EsParaRegalo(nuevaTienda)
DevolverComoCSV(ProductosParaRegalar, "ProductosParaRegalar")

ProductosConStockNoDisponible = ConStockNoDisponible(nuevaTienda)
DevolverComoCSV(ProductosConStockNoDisponible, "ProductosConStockNoDisponible")