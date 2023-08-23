import os

def main():
    nombre = os.getenv("USERNAME")
    edad = os.getenv("AGE")
    localidad = os.getenv("LOCATION")
    pais = os.getenv("COUNTRY")
    informacion = os.getenv("INFORMATION")
    print(f"¡Hola, soy {nombre} y tengo {edad} años. Actualmente resido en {localidad} que se encuentra en {pais}. Gracias a seguir estudiando puedo decir que {informacion}!")

if __name__ == "__main__":
    main()