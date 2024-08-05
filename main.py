#  We will make a Rock, Paper and Sissor game
'''
First we set our identification
 Rock = R = 1
 Paper = P = 0
 Sissor = S = -1

Then we create a dictionary to store this
and also allow the computer to select random numbers         # For that go to chat GPT and search code for random number selection between 1,0 and -1
'''
import pyttsx3                                          # This import is used to give audio feed back 
engine = pyttsx3.init()


import random
comp = random.choice([-1,0,1])

gDict = {"r":1, "p":0, "s":-1}

you = input("Choose Your's: ")
U = gDict[you.lower()]

rDict = {1:"Rock", 0:"Paper", -1:"Siscors"}             # Reverse Dictionary can show us the Word/Key aginst a particular value/number. 

print(f"You Chose {rDict[U]}\nComputer Chose {rDict[comp]}")   



if (comp==U):
    print("Its a draw.")
    engine.say("Its a draw.")
    engine.runAndWait()
else:
    if (comp==0 and U==-1):
        print("Hurrah! You Win")
        engine.say("Hurrah! You Win")
        engine.runAndWait()
    elif (comp==0 and U==1):
        print("Opps! You Loss")
        engine.say("You Loss")
        engine.runAndWait()
    elif (comp==1 and U==0):
        print("Hurrah! You Win")
        engine.say("Hurrah! You Win")
        engine.runAndWait()
    elif (comp==1 and U==-1):
        print("Opps! You Loss")
        engine.say("You Loss")
        engine.runAndWait()
    elif (comp==-1 and U==0):
        print("Opps! You Loss")
        engine.say("You Loss")
        engine.runAndWait()
    elif (comp==-1 and U==1):
        print("Hurrah! You Win")
        engine.say("Hurrah! You Win")
        engine.runAndWait()
    else:
        print("Something went wrong.")
