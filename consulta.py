import sys
import pandas as pd

def manejar_registro(accion, nombre, edad):
    # Ruta del archivo Excel
    archivo_excel = r'C:\xampp\htdocs\PHP_PYTHON_CHATGPT\pruebas\rellenar excel python panda\registros.xlsx'
    
    # Cargar el archivo Excel
    df = pd.read_excel(archivo_excel)
    # usamos las cabezeras Nombre, Edad
    match accion:
        case "buscar":
            resultado = df[df['Nombre'] == nombre]
            if not resultado.empty:
                print(resultado)
            else:
                print(f"No se encontró el registro con nombre: {nombre}")
        
        case "añadir":
            # Añadir un nuevo registro
            nuevo_registro = pd.DataFrame({'Nombre': [nombre], 'Edad': [edad]})
            df = pd.concat([df, nuevo_registro], ignore_index=True)
            df.to_excel(archivo_excel, index=False)
            print(f"Se añadió el registro: {nombre}, {edad}")
        
        case "modificar":
            # Modificar la edad de un registro existente
            if nombre in df['Nombre'].values:
                df.loc[df['Nombre'] == nombre, 'Edad'] = edad
                df.to_excel(archivo_excel, index=False)
                print(f"Se modificó el registro de {nombre} con nueva edad: {edad}")
            else:
                print(f"No se encontró el registro con nombre: {nombre}")
        
        case "eliminar":
            # Eliminar un registro por nombre
            if nombre in df['Nombre'].values:
                df = df[df['Nombre'] != nombre]
                df.to_excel(archivo_excel, index=False)
                print(f"Se eliminó el registro de {nombre}")
            else:
                print(f"No se encontró el registro con nombre: {nombre}")
        
        case _:
            print("Acción no válida.")
def mostrar_excel(archivo_excel):
    # Leer el archivo Excel
    df = pd.read_excel(archivo_excel)

    # Configurar Pandas para mostrar todas las filas y columnas
    pd.set_option('display.max_rows', None)  # Mostrar todas las filas
    pd.set_option('display.max_columns', None)  # Mostrar todas las columnas

    # Mostrar el DataFrame completo
    print(df)

    # Restablecer la configuración a valores por defecto (opcional)
    pd.reset_option('display.max_rows')
    pd.reset_option('display.max_columns')


# archivo_excel = r'C:\xampp\htdocs\PHP_PYTHON_CHATGPT\pruebas\rellenar excel python panda\registros.xlsx'

# Recibir argumentos desde PHP
nombre = sys.argv[1]
edad = sys.argv[2]
accion = sys.argv[3]
# nombre = "mario"
# edad = 24
# accion = "añadir"

manejar_registro(accion, nombre, edad)
print()
# Ejemplo de uso de la función
# manejar_registro("añadir", "Juan", edad=30)
# mostrar_excel(archivo_excel)
# manejar_registro("buscar", "Juan")
# manejar_registro("añadir", "Maria", edad=30)
# mostrar_excel(archivo_excel)   
# manejar_registro("modificar", "Juan", edad=25)
# manejar_registro("eliminar", "Maria")
