"""
Cristian Alejandro Guarin Marin
Grupo: 3
"""

import ahorcado as fc
#Hanged Man game

"""
Game instructions
"""

#Desplegando la entrada
fc.printIntro("/home/crguarinm/Documentos/UdeA/Informática 1/Unidad 4/HangedMan/intro.txt")

#Global Variables
attempedLetters = ""
attempCount = 8
again = "y"

#Enter the path of the file with the words
fileWords = fc.loadWords("/home/crguarinm/Documentos/UdeA/Informática 1/Unidad 4/HangedMan/superHeroes.txt")

while again == "y":
#Selecting gamemode
    gameMode = int(input("""
Game modes
1. Input secret word
2. Import it from a file

Selected game mode: """))
    
    if gameMode == 1:
        secret = fc.inputSecret()
    elif gameMode == 2:
        secret = fc.pickWord(fileWords, ", ")
    #Each round
    round = "y"

    while round == "y":
        
        #Showing statistics   
        print(f"""
Remaining attemps: {attempCount}
Avaliable letters: {fc.obtainAvaliableLetters(attempedLetters)}

{fc.obtainGuessedPart(secret, attempedLetters)}""")
        
        #Requesting and checking the letter
        while True:
            letter = input("Enter a letter: ")
            letter = letter.lower()
            
            #Verifying if it is a letter
            if letter.isalpha():
                
                #Verifying if it is only one
                if len(letter) == 1:
                
                    #Removing lives
                    if letter in secret:
                        pass
                    elif letter in attempedLetters:
                        print("This letter has already been selected. Try again")
                    else: 
                        attempCount = attempCount-1   
                    
                    attempedLetters = attempedLetters + letter
                    break
                
                else:
                    print("Enter only one letter")
            
            else:
                print("Enter a valid letter")
        
                     
        

        #Breaking the cycle when the user loses all the available attempts
        if attempCount == 0:
            next= ""
            next = int(input(f"""
The secret word was {secret}
Would you like to play again? (Yes = 1 ; No = 2)
"""))
            if next == 1:
                attempedLetters = ""
                attempCount = 8
                break
            elif next == 2:
                print("Thanks For playing")
                again = "N"
                round = "n"
                break
        
        
        #Breaking the cycle when the user guesses all the letters
        condition = fc.guessedWord(secret, attempedLetters)
        if condition == True: 
            next = ""
            next = int(input("""¡CONGRATULATIONS! Would you like to play again? (Yes = 1 ; No = 2)
"""))
            if next == 1:
                attempedLetters = ""
                attempCount = 8
                break
            else:
                print("Thanks For playing")
                again = "N"
                round = "n"
                break        
            #Solucionar los espacios en las palabras secretas