import time
#the interface og  thre game
print("your adventure game start...destroy them")
time.sleep(3)
print("are you ready hero ?!...gooo")
time.sleep(3)

import random

places=["old palace","under the ground"]

evils=["monker","titan","forester"]

weapons=["dart","rope","sword"]

place = random.choice(places)

evil= random.choice(evils)

weapon= random.choice(weapons)
#my game details
def printsos(sos):
    print(sos)  
    time.sleep(2)

def cave():
    printsos("oh no it is dark here .what will you do ")
    printsos("you are in a game gyu and you can click on the conor of screen..do not worry!")
    printsos("it is bright now .so take a deep breath and and move on forward to the X")
    printsos("please,far all these things and take it"+weapon)
    printsos("you are ready now to the next step .do not turn out .look under the X there is a tunnel ,go and star\n go hero go ")
    tunnel()
def field():
    printsos("there are  strane plants hete , why it look like that")
    printsos("look there is a path and you should go right")
    printsos("look there is a black tree; behind it there is X and box t,take it " +weapon ) 
    printsos("you are warrior now, go not left there are a wooden door it is lead you to tunnel go..")
    tunnel()
def start():
    start=int(input("your time to win come.first step ,,choose the place click 1 to inter to faild ,2 to inter to the cave"))
    if start == 1:
       field()
    elif start== 2:
         cave()
    else:
        printsos("please choose 1 or 2 only")
def tunnel():
    printsos("it is on fire now, are you ready or what.all the way fired")
    printsos("do not escape baby it it a game i tell you before . i am joking with you !(:")
    printsos(evil+"what the hell .it is big .the war is star lets destroy them")
    options=int(input("your option 1 or 2 have not third!\n"
    "1.star the war\n"
    "2.end the game\n"))
    if options ==1: 
       printsos("you are a hero go")
       start()  
    if options== 2:
       printsos("i think it is the wrong choice")
       turnchoice()   
def turnchoice():
    turnchoice=int(input("chose 1 to complete\n 
    2 to end the game\n"))
    if turnchoice == 1:
       start()
    if turnchoice == 2:
       gameover() 
def gameover():
    printsos("thanks for paying")                       
def play():
    printsos("you are in the gammmme"+place)
    start()

play()



   
