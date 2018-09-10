# Author: Roxanne Lai 9/10/18
# Class: CMPT 120L 113
# Program Name: Text-Adventure: Delight and Discrimination (A play on Pride and Prejeduce)

# Global imports
import random

# functions

def cls():
    print("\n" *100)

def start_room():
    cls()
    start_room_options = ["1","2","3"]
    user_choice =""
    while user_choice not in start_room_options: 
        print(''' For as long as you can remember you have held a strong disdain for nobles,
noblemen especially, as they have a conceited air about them -
one that seens to belittle your intellect in the most infuriating manner.
One would think that in the early 19th century men would have the common sense
not to gawk so openely at a woman's superior wisdom - but that is of no consequence
to you at the current moment: all that matters now is calming your poor mother down.
She has gone into a terible fit after learning that a rich nobleman, Mr. Bradley Kensignton,
is returning to his manner house in a weeks time. She flits about you and your sisters,
fussing with your hair and grumbling about the state of the house.
With five younger sisters, and one older, she plans to show you off to potential suitors
at the upcoming ball - ultimately hoping to wed one of you to the painfully rich Mr. Bradley.
You sigh heavily at the thought of going to the ball, and sigh even more heavily
at the thought of potential suitors - no matter how many times you insult them,
men fail to understand your lack of interest in them! You find the whole idea of marriage ridiculous,
but your mother will never stop pestering you until you finally settle down.
At last, after many sleepless nights dreading the upcoming ball,
you decide that if you MUST marry it will either be for money, or for love -
but the choice will be up to you, not your mother!

Later: It is the night of the ball, and your elder sister, Louisa,
is dancing with Mr. Bradley, the young nobleman who just returned.
Looking around the room absentmindedly, you notice a sullen man
standing awkwardly by the far wall of the ballroom.
You note his confusingly contradictory appearence: while  his hair is
haphazardly brushed back from his face, his clothes look rich and finely tailored.
While you are puzzingling over the true nature of the stranger,
your mother follows the direction of your stare and comments:
"That is the infamously gloomy friend of Mr. Bradley, Lord Vincent Darlington.
According to my friend Merrywheather, he is the filthy rich son of the late Darlingtons.
As he was their only child he inhereted everything after their death,
even the estate across the moor!".
You don't find Lord Darlington particularly handsome,
but there is an intellegent and slightly curious look in his eyes.
Your mother tells you to introduce yourself to him: you choose to___

  1) Cross the room to introduce yourself as you mother suggested.
  2) Scoff at your mother's suggestion, and occupy yourself yet again with people-watching.
  3) Turn to the nearest stranger and ask them to dance(in an attempt to rid yourself of your mother's presence). ''')

        user_choice = str(input("Enter option number: "))
    #print("You have selected " + user_choice)\
    if user_choice == start_room_options[0]:
        room01()
    elif user_choice == start_room_options[1]:
        room02()
    elif user_choice == start_room_options[2]:
        room03()
def room01():
    cls()
    print("\n \n --> you are in room 01 now")

def room02():
    cls()
    print("\n \n --> you are in room 02 now")

def room03():
    cls()
    print("\n \n --> you are in room 03 now")
        
# Main Program
start_room() 
