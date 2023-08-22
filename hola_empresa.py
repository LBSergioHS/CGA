import os


def main():
    nombre = os.getenv("USERNAME")
    print(f"Mi empresa se llama {nombre} y esto es un curso que me ha proporcionado.")


if __name__ == "__main__":
    main()