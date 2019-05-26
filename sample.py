#while game is still playing it shud keep looping to input the new song
y = str(input("Enter Song Here: "))

def inputsong(y):
    file_stream = open("text.txt", "a")
    file_stream.write(y)
	
    file_stream = open("text.txt", "r")

    i = 0

    songnum = []
    for line in file_stream:
        songnum = line.split(" ")

    print(songnum)

    numbers = ['1.', '2.', '3.', '4.', '5.', '6.', '7.', '8.']
    song = []
    while i < len(songnum):
        song.append(songnum[i])

        i = i+1

    file_stream = open("text.txt", "a")
    file_stream.write(" ")
	
    file_stream.close()

    dictionary = dict(zip(numbers, song))
    print(dictionary)

    result = sorted(dictionary.items(), key=lambda t:[1])
    resultText = ""
    for k, v in result:
            resultText += "{} {}\n".format(k,v)

		
    print(resultText)

inputsong(y)






























"""

#Top 5 Leaderboard Function for Start Screen
def leaderboard():

    file_stream = open("text.txt", "a")
    file_stream.write(nameValue)
    file_stream.write(" ")

	file_stream.write(songsPlayed)
	file_stream.close()


	
    file_stream = open("text.txt", "r")

    i = 0
	
    scorename = []
    for line in file_stream:
	    scorename = line.split(" ")

    name = []
    score = []
    while i < len(scorename):
        if i%2 == 0: #even : keys/Name
            name.append(scorename[i])
        else: #odd : values/Score
            score.append(scorename[i])

        i = i+1

    file_stream = open("text.txt", "a")
    file_stream.write("") #I THINK THIS IS FOR WHENEVR YOU ADD MORE PEOPLE TO THE LIST

    file_stream.close()

    i = 0
    masterlist = []

    while i < len(name):
        namedictionary = {
			"Name": name[i]
		}
        scoredictionary = {
			"Score": score[i]
		}
		

        leaddictionary = [(namedictionary["Name"], scoredictionary["Score"])]
        for entry in leaddictionary:
            masterlist.append(entry)

        i = i+1

    def getKey(item):
        return int(item[1])

    #list of tuples
    result = sorted(masterlist, key=getKey, reverse=True)
    file_stream.close()
    return result

	
topfivelist = leaderboard()


    #Supposed Sequence Start
    load_update('SEQ')
    load_update('IN')
    load_update('3')
    load_update('2')
    load_update('1')

    #Non Constant Variables that need to be refreshed per game
    testPattern = []
    lastClickTime = 0
    songsPlayed = 0
    waitingForInput = False
    currentStep = 0
    gameLoopStart = True
    gameProc.start()


#THis is where all the magic begins
def gameFunc():
    global gameLoopStart
    while gameLoopStart is True:
        clicked = None
        if not waitingForInput:
            #outputting letter and randomchoice
            buttonLetter = random.choice(letterPool)
            testPattern.append(buttonLetter)
            for button in testPattern:
                #change loadtext
                #flash the button on loader
                #wait
                time.sleep(2)
                print(button)
                for i in range(4):
                    print('*')
                    
            waitingForInput = True

        else:
            global ownPattern
            if clicked is True and ownPattern[0] == testPattern[currentStep]:
                #show button   
                currentStep += 1
            
                if currentStep == len(testPattern):
                    songsPlayed += 1
                    waitingForInput = False
                    currentStep = 0
                    topTextValue += 1
                    #update topText and score
            
            elif (clicked is False and ownPattern[0] != testPattern[currentStep]):
                testPattern = []
                waitingForInput = False
                currentStep = 0
                topTextValue = 1
                score = 0
                gameLoopStart = False
                print('YOU JUST LOST TRASH MONSTER')
                #reset variables
                #save score and name to variable
                #then txt file
                #update top 5

#gameThread = Thread(target=gameFunc)
gameProc = Process(target=gameFunc)

#while not gameProc.ready():
"""
