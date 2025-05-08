"""
Angela Lisette Acosta Chaucanés
Cristian Alejandro Guarin Marin
"""

def printIntro(fileName):
    '''
    Firma:
        (string) -> ()
    
    Sinopsis:
        Función que imprime el contenido de un archivo de texto
        en la consola.
        
    Entradas y salidas:
        - filename: string que contiene el nombre del archivo a imprimir
        (preferiblemente escriba la ruta absoluta del archivo)
        - returns: None
        
    Ejemplos de uso:
        
        >>> printIntro("intro.txt")
        ___  _                             _             +---+ 
       / _ \| |                           | |            |   | 
      / /_\ \ |__   ___  _ __ ___ __ _  __| | ___        O   |    
      |  _  | '_ \ / _ \| '__/ __/ _` |/ _` |/ _ \      /|\  |    
      | | | | | | | (_) | | | (_| (_| | (_| | (_) |     / \  |
      \_| |_/_| |_|\___/|_|  \___\__,_|\__,_|\___/           |
                                                      =========
    '''

    #Cuerpo de la función
    
    #Solo se va a ejecutar en caso de que no haya errores
    try:
        
        with open(fileName, 'r', encoding="utf-8") as file:
            content = file.read()
            print(content)
    
    except FileNotFoundError:
        print(f"El archivo {fileName} no se encontró.")
    
    except Exception as e:
        print(f"Se produjo un error al leer el archivo: {e}")


def inputSecret():
    '''
    Firma:
        () -> (string)
    
    Sinopsis:
        Función que solicita al usuario la palabra secreta
        
    Entradas y salidas:
        - inputs: None
        - returns: string con la palabra secreta ingresada por el usuario
        
    Ejemplos de uso:
        
        >>> p = inputSecret()
        Ingrese la palabra o frase oculta: UdeA
        
        >>> print(p)
        UdeA 
    '''
    
    # Cuerpo de la función
    secret = input("Ingrese la palabra o frase oculta: ")
    return secret

