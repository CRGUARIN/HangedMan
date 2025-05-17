"""
Cristian Alejandro Guarin Marin
Grupo: 3
"""

import ahorcado as fc

#Pruebas de la función printIntro

#fc.printIntro("/home/crguarinm/Documentos/UdeA/Informática 1/Unidad 4/HangedMan/intro.txt")

#fc.printIntro("/home/crguarinm/Documentos/UdeA/Informática 1/Unidad 4/HangedMan/main.py")

#Pruebas de la función inputSecret

#h = fc.inputSecret()
#print(h)

#l = fc.inputSecret()
#print(l)

#Pruebas de la función loadWords

#superheroes = fc.loadWords("/home/crguarinm/Documentos/UdeA/Informática 1/Unidad 4/HangedMan/superHeroes.txt")
#print(superheroes)

#generalidades = fc.loadWords("/home/crguarinm/Documentos/UdeA/Informática 1/Unidad 4/Generalidades lab 4.txt")
#print(generalidades)

#Pruebas countWords

#a = input("Ingrese una frase: ")
#b = input("Ingrese el separador entre las palabras: ") 
#c = fc.countWords(a, b)
#print(c)

#e = input("Ingrese una frase: ")
#f = input("Ingrese el separador entre las palabras: ")
#g = fc.countWords(e, f)
#print(g)

#Puebas pickWord

#a = fc.pickWord("Hola,Cómo,Estás", ",")
#print(a)

#b = fc.pickWord(superheroes, ", ")
#print(b)

#Pruebas obtainGuessedWord()

#a = fc.obtainGuessedPart("perro", "aEiousp")
#print(a)

#b = fc.obtainGuessedPart("Salvaje", "bsucbshcjs,jcblsiE")
#print(b)

#Pruebas obtainAvaliableLetters

#a = fc.obtainAvaliableLetters("Abfs")
#print(a)

#a = fc.obtainAvaliableLetters("efghijk")
#print(a)

#Pruebas verifyEnteredLetter

#attemps = "akysahbflasifbl"
#print(fc.verifyEnteredLetter("A","avksrjgbk"))

#attemps = "aeiow"
#print(fc.verifyEnteredLetter("X", "rjnlkgnklra"))

#Pruebas guessedWord

#attemps = "ljkhlafvjJKFEB"
#print(fc.guessedWord("hOla", attemps))

#attemps = "ljkhlafvjJKFEBoA"
#print(fc.guessedWord("HoLA", attemps))