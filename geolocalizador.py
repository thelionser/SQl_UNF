#Ingreso la libreria py proj
# Importa la librería pyproj actualizada
import pyproj
import tkinter

def convertir(lat, long):
    # Define el sistema de coordenadas de entrada y salida
    wgs84 = pyproj.CRS('epsg:4326')  # Sistema de coordenadas de entrada
    utm = pyproj.CRS('EPSG:3036')  # Sistema de coordenadas de salida

    # Crea el transformador
    transformer = pyproj.Transformer.from_crs(wgs84, utm)

    # Realiza la transformación
    utm_x, utm_y = transformer.transform(lat, long)

    return utm_x, utm_y




lat = -25.95420
long = 32.55752

utm_x, utm_y = convertir(lat, long)
print(f"Coordenadas UTM X={utm_x}, Y={utm_y}")
