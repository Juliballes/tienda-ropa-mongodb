from database import *
import json

nuevaTienda = IniciarTienda("NuevaTienda")

with open("TiendaRopa.json") as file:
    data = json.load(file)
    nuevaTienda.insert_many(data)

    print("Datos cargados correctamente.")

ConsultasEspecificas(nuevaTienda)