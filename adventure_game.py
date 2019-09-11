#the interface of game
import time

import random
places=["the old palace","under thr ground"]

weapons=["sword","rope","dart"]

evils=["titan","forester","monkey"]

place=random.choice(places)

weapon=random.choice(weapons)

evil=random.choice(evils)

#my game deteails
def printsos(message):
    print(message)
    time.sleep(3)

def replay():
    replay = input("Wanna play again ?\n"
                   "Please anwser with y or n.\n")
    if replay == "y":
        field()
    elif replay == "n":
        return(printsos("OK, goodbye."))
    else:
        printsos("Please anwser with y or n.")
        replay()
 
 def field():
     choice = int(input("Enter 1 to go to the palace.\n"
                       "Enter 2 to peer into the cave.\n"
                       "Please enter 1 or 2.\n"))
     if choice == 1:
        palace()
     elif choice == 2:
         cave()
     else:
         printsos("Please enter 1 or 2.\n")
         field()


def cave():
printsos(" ohh no,it is dark.\n i tell you inneed lentern !......\n what will you do now ?!   ")
printsos("you are in a game guy and you can click o on the corner of your screen do not warry...?!" )
printsos("look, it it bright . yeah now take a deep breath and movo on forward to thr X ")
printsos(" start far all things in the ground . there is a surprise here ")
printsos("now take it" + weapon)
printsos("you are ready now to the next step.do not turu out look under the X there is a tunnel ti go to in and palace.......\n go hero...")
field()
def palace():
  printsos("the on fire now,are you ready or what. all the way fired  ")
  printsos("do not escape hero i tell you bafore it is a game and joking with you(:")
  printsos(evil+ "what the hell, it is big .the war is start . let is destroy them  ")
  optios=int(input("your optios 1 or 2 have not third!\n"
                  "1.start the war\n"
                  "2.end the gamr\n"))
  if optios == 1:
     printsos("you are hero") 
     printsos("choose it now"+weapon)
  if optios ==2:
     printsos("i think it is the wrong choice")   
     turnchoice=int(input("your choice 1 to complete or 2 \n"
                         "1.yes\n"
                         "2.no\n"
    ))
     if turnchoice==1:
        palace()
     elif turnchoice==2:
          gamrover()
def gamrover()  
    printsos("thanks.for playing") 
    replay()
def start():
    printsos("your adventure start ... destroy him" + place)
    printsos("are you ready hero?! gooooo...!")
    printsos("from where you will start")
    field()

start()
         



   
