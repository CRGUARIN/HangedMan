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
    abc = "abcdefghijklmnopqrstuvwxyz"
    
    while True:
        secret = input("Ingrese la palabra o frase oculta: ").lower()
        if all(letra in abc for letra in secret) and secret != "":
            return secret
        else:
            print("Entrada inválida. Intente de nuevo.")

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
    if b != ",":
        c = b.replace(b, ",")    
        a = a.replace(b, c) + c
    else:
        c = b
        a = a + c
    l = len(a)
    i = 0
    count = 0
    while i < l:
        temp = a[i]
        if temp == c:
            count = count + 1
        i = i + 1
    return count

def pickWord(a, b):

    '''
    Firma:
        (string,string) -> (string)
        
    Sinopsis:
        Función que permite seleccionar una palabra o frase secreta correspondiente a una posicion 
        dada de un conjunto de palabras separadas por un delimitador.  
    
    Entradas y salidas:
        - palabras: Conjunto de palabras o frases secretas separadas por un delimitador
        - separador: Delimitador que separa una palabra o frase secreta de otra
    
    Salidas
        - returns: Palabra o frase de la posiciónon elegida
        
    Ejemplos de uso:
        >>> x = 'homero_marge_bart_lisa_maggie' 
        >>> pickWord(x,'_')
        'homero'
        
        >>> palabra = pickWord('marcos, lucas, mateo, juan',',')
        >>> print(palabra)
        'mateo'
        
    '''
    import random as rd
    
    c = ""
    if b != ",":
        c = b.replace(b, ",")
        a = a.replace(b, c)
        a = a + c
    else:
        a = a + c
        c = b
    
    option = rd.randint(0, countWords(a,c))
    l = len(a)
    i = 0
    temp = ""
    count = 0
    word = ""
    
    while i < l:
        temp = a[i]
        if temp != c:
            word = word + temp
        elif temp == c:
            count = count + 1
            if count - 1 == option:                    
                break
            else:
                word = ""
        i = i + 1
    return word

def obtainGuessedPart(word,attemps):
    '''
    Firma:
        (string,string) -> (string)
        
    Sinopsis:
        Imprime la parte de la cadena que ha sido adivinada.  
        
    Entradas y salidas:
        - palabraSecreta: string, palabra que el usuario esta adivinando
        - letrasIntentadas: string, letras intentadas por el usuario para adivinar la palabra
        - returns: string, compuesto de letras y caracteres raya bajo que representan las letras aun no adivinadas
        
    Ejemplos de uso:
        >>> palabraSecreta = 'perro'
        >>> letrasIntentadas = 'aeiousp'
        >>> print obtenerParteAdivinada(palabraSecreta, letrasIntentadas)
        'p e _ _ o'
        
        >>> obtenerParteAdivinada('frodo', '')
        '_ _ _ _ _'  
    '''
    l = len(word)
    word = word.lower()
    attemps = attemps.lower()
    i = 0
    temp = ""
    result = ""
    first = True
    while i < l:
        temp = word[i]
        if temp in attemps:
            result = result + temp + " "
            if first and i == 0:
                result = result.upper()
        else:
            result = result + "_" + " "
        i = i+1
    return result


