import pyglet
import glooey
import random
import threading
import time
from threading import Thread
from multiprocessing import Process

###############################################################################################################################

#SUMMARY:
#The App was made in a semi Object Oriented Fashion, Single Thread and Single Screen (Component/Widget Based Programming)
#The App was made using Pyglet, a Windowing and MultiMedia Library that uses OpenGL Context
#The App was organized and made more efficient with Glooey, a Pyglet Extension that works directly on top of Pyglet
#The App is our own version of a simple music app in a better looking interface

#CONSTRAINTS:
#1. Use Pyglet Framework (Yes - Same Library, Event Handling, Never Mentioned to Use Pyglet ONLY)
#2. Read and Write (Yes - Leaderboard with Name and Score)
#3. 2 Data Structures (Yes - Dict for LeaderBoard, List for Music and Game Logic, Event Handler Stack)
#4. GUI (Yes - Pyglet and Glooey)
#5. Interface Input (Yes - Mouse Click, Inputbox)
#6. Purpose (Yes - Visually Pleasing Game for Bored People who want to have a better Memory)
#7. Source Code in Functions (Yes - Presence of Boilerplate code but most are still in functions or classes)


#INSTRUCTIONS:


#RESOURCES:
#All Buttons and Objects were created from scratch by using Fotor, a Photo Editing/Designing Web App
#Fonts are from dafont.com {Death Star, Positive}
#Background DrumPad Picture from https://www.interstatemusic.com/21613-Roland-Octapad-SPD-30-Electronic-Drum-Pad-SPD30.aspx



###############################################################################################################################

#Create the window with pyglet, Organize with Glooey
window = pyglet.window.Window(800, 800, 'Music App')
gui = glooey.Gui(window)




#green button to show last playlist then empties current text list to run from top yay
#green button when pressed again empty text file new playlist


#Do this if unable to install fonts/fonts won't work on desired computer
#Example:
#pyglet.font.add_file('Lato-Regular.ttf')
#pyglet.font.load('Lato Regular')


#SubClasses for Customized Widgets
###################################################################
class padBackDrop(glooey.Background):
    custom_color = '#ffffff'
    custom_image = pyglet.resource.image('rsz_pad.jpg')

class padGrid(glooey.Grid):
    #custom_default_row_height = 200
    custom_bottom_padding = 200
    #custom_cell_padding = 10

class topHolder(glooey.VBox):
    custom_alignment = 'fill top'
    custom_size_hint = 200, 100

class botHolder(glooey.HBox):
    custom_alignment = 'fill bottom'
    custom_size_hint = 200, 300

class botMidLogo(glooey.VBox):
    #custom_alignment = 'bottom'
    custom_size_hint = 250, 100

class botLeaderText(glooey.VBox):
    #custom_alignment = 'bottom'
    custom_size_hint = 250, 120
    #custom_bottom_padding = 30

class botLeaderTitle(glooey.VBox):
    custom_alignment = 'center'
    custom_size_hint = 200, 60
    #custom_text = 'Top 5:'
    
class botMidLoader(glooey.VBox):
    custom_alignment = 'top'
    custom_size_hint = 250, 80

class midHolder(glooey.Placeholder):
    custom_alignment = 'center'

class topLabel(glooey.Label):
    custom_color = '#000000'
    custom_font_size = 20
    custom_bold = True
    custom_font_name = 'Death Star'

class instructLabel(glooey.Label):
    custom_color = '#000000'
    custom_font_size = 10
    custom_font_name = 'Death Star'

class textLabel(glooey.Label):
    custom_font_size = 20
    custom_bold = True
    custom_alignment = 'center'
    custom_font_name = 'Death Star'

class gameLabel(glooey.Label):
    custom_text = '8Button\n MP3'
    custom_font_size = 30
    custom_bold = True
    custom_alignment = 'top'
    custom_font_name = 'Death Star'

class loadLabel(glooey.Label):
    custom_color = '#000000'
    custom_font_size = 30
    custom_bold = True
    custom_alignment = 'center'
    custom_font_name = 'Death Star'

class leaderLabel(glooey.Label):
    custom_color = '#000000'
    custom_font_size = 20
    custom_bold = True
    custom_font_name = 'Death Star'
    custom_text = 'The Playlist'

class leaderText(glooey.Label):
    custom_bold = True
    custom_font_size = 'Arial Black'
    custom_color = '#3c5639'
    custom_font_size = 10

#Button Classes For All Separate Buttons
################################################################

class buttonA(glooey.Button):
    class Base(glooey.Image):
        custom_image = pyglet.resource.image('rsz_base.jpg')

    class Over(glooey.Image):
        custom_image = pyglet.resource.image('rsz_over.jpg')

    class Down(glooey.Image):
        custom_image = pyglet.resource.image('rsz_downA.jpg')
    
    songNum = 0

class buttonB(glooey.Button):
    class Base(glooey.Image):
        custom_image = pyglet.resource.image('rsz_base.jpg')

    class Over(glooey.Image):
        custom_image = pyglet.resource.image('rsz_over.jpg')

    class Down(glooey.Image):
        custom_image = pyglet.resource.image('rsz_downB.jpg')

    songNum = 1

class buttonC(glooey.Button):
    class Base(glooey.Image):
        custom_image = pyglet.resource.image('rsz_base.jpg')

    class Over(glooey.Image):
        custom_image = pyglet.resource.image('rsz_over.jpg')

    class Down(glooey.Image):
        custom_image = pyglet.resource.image('rsz_downC.jpg')
    
    songNum = 2


class buttonD(glooey.Button):
    class Base(glooey.Image):
        custom_image = pyglet.resource.image('rsz_base.jpg')

    class Over(glooey.Image):
        custom_image = pyglet.resource.image('rsz_over.jpg')

    class Down(glooey.Image):
        custom_image = pyglet.resource.image('rsz_downD.jpg')

    songNum = 3

class buttonE(glooey.Button):
    class Base(glooey.Image):
        custom_image = pyglet.resource.image('rsz_base.jpg')

    class Over(glooey.Image):
        custom_image = pyglet.resource.image('rsz_over.jpg')

    class Down(glooey.Image):
        custom_image = pyglet.resource.image('rsz_downE.jpg')
    
    songNum = 4

class buttonF(glooey.Button):
    class Base(glooey.Image):
        custom_image = pyglet.resource.image('rsz_base.jpg')

    class Over(glooey.Image):
        custom_image = pyglet.resource.image('rsz_over.jpg')

    class Down(glooey.Image):
        custom_image = pyglet.resource.image('rsz_downF.jpg')

    songNum = 5

class buttonG(glooey.Button):
    class Base(glooey.Image):
        custom_image = pyglet.resource.image('rsz_base.jpg')

    class Over(glooey.Image):
        custom_image = pyglet.resource.image('rsz_over.jpg')

    class Down(glooey.Image):
        custom_image = pyglet.resource.image('rsz_downG.jpg')

    songNum = 6

class buttonH(glooey.Button):
    class Base(glooey.Image):
        custom_image = pyglet.resource.image('rsz_base.jpg')

    class Over(glooey.Image):
        custom_image = pyglet.resource.image('rsz_over.jpg')

    class Down(glooey.Image):
        custom_image = pyglet.resource.image('rsz_downH.jpg')

    songNum = 7

class nameForm(glooey.Form):
    custom_alignment = 'center'

    class Label(glooey.EditableLabel):
        custom_font_name = 'Arial Black'
        custom_font_size = 10
        custom_color = '#b9ad86'
        custom_alignment = 'fill'
        custom_horz_padding = 5
        custom_top_padding = 5
        custom_width_hint = 250


    class Base(glooey.Background):
        custom_center = pyglet.resource.texture('form_center.png')
        custom_left = pyglet.resource.image('form_left.png')
        custom_right = pyglet.resource.image('form_right.png')

class playlistButton(glooey.Button):
    class Base(glooey.Image):
        custom_image = pyglet.resource.image('gamebase.jpg')

    class Over(glooey.Image):
        custom_image = pyglet.resource.image('gameover.jpg')

    class Down(glooey.Image):
        custom_image = pyglet.resource.image('gamedown.jpg')

###################################################################



#INSTANCES


#Variables
songsPlayed = 0
nameValue = 'Person'
songtext = 'Songs Played :   ' + str(songsPlayed)
nametext = 'Playlist ni :   ' + nameValue
loadtext = '. . . . .'


#topholder widget instances
topText = textLabel('Music')
score = topLabel(songtext)
name = topLabel(nametext)


#topholder instance and widget addition
topholder = topHolder()
topholder.add(topText)
topholder.add(name)
topholder.add(score)

#botmidlogo instance and logoname widget
botmidlogo = botMidLogo()
gamelabel = gameLabel()
botmidlogo.add(gamelabel)

#botmidLoader instance
loader = loadLabel(loadtext)
botmidloader = botMidLoader()
botmidloader.add(loader)


#botmid instance
botmid = glooey.VBox()
botmid.add(botmidloader)
botmid.add(botmidlogo)

#leaderboard widget instances and loading leaderboard

botleadertext = botLeaderText()

#botleadertext.add(leaderText(resulted))

botleadertitle = botLeaderTitle()
botleadertitle.add(leaderLabel())


#leaderboard vbox instance
leaderboard = glooey.VBox()
leaderboard.add(botleadertitle)
leaderboard.add(botleadertext)


#nameForm instance
nameform = nameForm('Type Your Name Here')

#bottopleft vbox instance
instruct = instructLabel('How to Use:\n Type Your Name\n Then Press the Green Button\nAfter That Just Press the Pads!\n Enjoy your music! :P')
bottopleft = glooey.VBox()
bottopleft.add(instruct)
bottopleft.add(nameform)


#botleft instance
playlistButton = playlistButton()
botleft = glooey.VBox()
botleft.add(bottopleft)
botleft.add(playlistButton)


#botholder instance
botholder = botHolder()
botholder.add(botleft)
botholder.add(botmid)
botholder.add(leaderboard)

midholder = midHolder(200, 400)




#Grid Instance and Pad Widget Addition

A = buttonA()
B = buttonB()
C = buttonC()
D = buttonD()
E = buttonE()
F = buttonF()
G = buttonG()
H = buttonH()
grid = padGrid(4,5)
grid.add(1, 0, A)
grid.add(1, 1, B)
grid.add(1, 2, C)
grid.add(1, 3, D)
grid.add(2, 0, E)
grid.add(2, 1, F)
grid.add(2, 2, G)
grid.add(2, 3, H)



#Main Widgets addition to Gui instance
padbackdrop = padBackDrop()
gui.add(padbackdrop)
gui.add(grid)
gui.add(botholder)
gui.add(topholder)



#Event Handling and Functions
###########################################


#Music Functions and Variables
musiclist = ['roar.mp3', 'jealous.mp3', 'fancy.mp3','baby.mp3','beer.mp3','paparazzi.mp3', 'clarity.mp3', 'gravity.mp3']

#Function that Input and Output the played song to a Txt File 
def inputsong(y):
    file_stream = open("text.txt", "a")

    file_stream.write(y)
	
    file_stream = open("text.txt", "r")

    i = 0

    songnum = []
    for line in file_stream:
        songnum = line.split(" ")
    if len(songnum) > 8:
        first = songnum[8]
        songnum = [first] 
        file_stream = open('text.txt', 'w')
    else:
        file_stream = open("text.txt", "a")

        

    print(songnum)

    numbers = ['1.', '2.', '3.', '4.', '5.', '6.', '7.', '8.']
    song = []
    while i < len(songnum):
        song.append(songnum[i])

        i = i+1

    
    file_stream.write(" ")
	
    file_stream.close()

    dictionary = dict(zip(numbers, song))
    print(dictionary)

    result = sorted(dictionary.items(), key=lambda t:[1])

    resultText = ""
    for k, v in result:
            resultText += "{} {:*^30}\n".format(k,v)

		
    return resultText


player = pyglet.media.Player()
plays = 0

#Plays the song on button pad press
def songer(button):
    global plays
    global music
    
    song = button.songNum
    music = pyglet.resource.media(musiclist[song])
    if plays > 0:
        player.pause()
        player.queue(music)
        player.next_source()
    else:
        player.queue(music)
        plays += 1
    player.play()


#Updates the text on the loader screen
def load_update(text):
    global loadtext
    global loader
    botmidloader.remove(loader)
    loadtext = text
    loader = loadLabel(loadtext)
    botmidloader.add(loader)
    print('The Song ' + text + ' is playing')


#The inner function used for InputBox Handler
def name_form_inner(typedtext):
    #Get the value from the name form
    global nametext
    global name
    global nameValue
    nameValue = typedtext
    print("The name '{}' has been inputted".format(nameValue))

    #Change the name label on top
    topholder.remove(name)
    nametext = 'Name :   ' + nameValue
    name = topLabel(nametext)
    topholder.add(name)

def song_num_changer():
    global songsPlayed
    global songtext
    global score
    topholder.remove(score)
    songsPlayed += 1
    songtext = 'Songs Played :   ' + str(songsPlayed)
    score = topLabel(songtext)
    topholder.add(score)

#Push name form handler off the stack once unfocused from Input Box
nameform.push_handlers(on_unfocus=lambda w: name_form_inner(w.text))


#get from the txt file
resulted = ""

#General Pad Button Function
def buttonFunc(button, song):
    global resulted
    songer(button)
    song_num_changer()
    songbert = song
    resulted = inputsong(songbert)


#Button Pad Events to Play Music and Change Some Values

@A.event
def on_click(A):
    global resulted
    buttonFunc(A, "Roar")
    load_update('Roar')

@B.event
def on_click(B):
    global resulted
    buttonFunc(B, "Jealous")
    load_update('Jealous')

@C.event
def on_click(C):
    global resulted
    buttonFunc(C, "Fancy")
    load_update('Fancy')

@D.event
def on_click(D):
    global resulted
    buttonFunc(D, "Baby")
    load_update('Baby')

@E.event
def on_click(E):
    global resulted
    buttonFunc(E, "Beer")
    load_update('Beer')

@F.event
def on_click(F):
    global resulted
    buttonFunc(F, "Paparazzi")
    load_update('Paparazzi')

@G.event
def on_click(G):
    global resulted
    buttonFunc(G, "Clarity")
    load_update('Clarity')

@H.event
def on_click(H):
    global resulted
    buttonFunc(H, "Gravity")
    load_update('Gravity')


@playlistButton.event
def on_click(playlistButton):
    global resulted
    leadertext = leaderText(resulted)
    botleadertext.add(leadertext)
    




pyglet.app.run()