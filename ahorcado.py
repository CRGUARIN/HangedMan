"""
Cristian Alejandro Guarin Marin
Grupo: 3
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

def loadWords(a):
    '''
    Firma:
        (string) -> (string)
        
    Sinopsis:
        Función que solicita el nombre de un archivo cualquiera y devuelve una cadena 
        de caracteres con su contenido
        
    Entradas y salidas:
        - filename: string que contiene el nombre del archivo con las palabras secretas
        - returns: string con todas las palabras secretas
        
    Ejemplos de uso:
        >>> loadWords("superHeroes.txt")
        'capitan centella, capitan planeta, batman, superman, robin, mujer maravilla, aquaman, flash,
        cyborg, capitan marciano, linterna verde,flash gordon, liga de la justicia, defensores de la 
        tierra, el fantasma, spider man, hulk, thor, iron man, los vengadores, robocop, terminator, 
        capitan america, hombre hormiga, la avispa, goku, vegeta, gohan, piccolo, trunks, spawn, 
        tintin, ghost rider, blade, tortugas ninja, soldado del invierno, el castigador, 
        el predicador, leonidas, kick ass, el comediante, el chapulin colorado, wolverine,
        flecha verde, el profesor super o, los autobots, robin hood\n'
    '''

    try: 
        text = open(f"{a}","r", encoding="utf-8")
        content = text.read()
        return content
    except FileNotFoundError:
        print("El archivo al que quiere acceder no existe o ingresó mal la ruta")

def countWords(a, b):
    '''
    Firma:
        (string,string) -> (int)
        
    Sinopsis:
        Función que cuenta la cantidad de palabras disponibles en una cadena
        
    Entradas y salidas:
        - palabras: Conjunto de palabras o frases separadas por un delimitador
        - separador: Delimitador que separa una palabra o frase de otra dentro de la cadena de entrada (palabras)
        - returns: cantidad de palabras secretas
        
    Ejemplos de uso:
        >>> materias = 'español,calculo,geometria vectorial,geometria euclidiana'
        >>> countWords(materias,',')
        4
        
        >>> countWords('gallo-gallina','-')
        2
    '''
    divided = a.split(b)
    quantity = len(divided)
    return quantity


