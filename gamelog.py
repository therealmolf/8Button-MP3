import random
import time


#pagpress ng game start button and typed na the input

#Varbs
testPattern = []
letterPool = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
lastClickTime = 0
flashSpeed = 0.5
flashDelay = 0.2
timeOut = 4 
levelValue = 1
scoreValue = 0
waitingForInput = False
currentStep = 0

# Sequence in 3 2 1 for loader

while True:
    clickedPad = None
    if not waitingForInput:
        #outputting letter and randomchoice
        buttonLetter = random.choice(letterPool)
        testPattern.append(buttonLetter)
        for button in testPattern:
            #change loadtext
            #flash the button on loader
            #wait
            print(button)
            time.sleep(2)
        waitingForInput = True
        

    else:
        if clickedPad and clickedPad == testPattern[currentStep]:
            #show button   
            currentStep += 1
        
            if currentStep == len(testPattern):
                scoreValue += 1
                waitingForInput = False
                currentStep = 0
                levelValue += 1
                #update level and score
        
        elif (clickedPad and clickedPad != testPattern[currentStep]):
            testPattern = []
            waitingForInput = False
            currentStep = 0
            levelValue = 1
            score = 0
            #reset variables
            #save score and name to variable
            #then txt file
            #update top 5




#time waiting
#event handling for the buttons 
#button letters


#connecting the player name, level, score and leaderboard



