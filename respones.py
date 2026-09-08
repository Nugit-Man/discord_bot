from random import choice, randint
import os
import math
from objects import Person


def get_array():
    """
    gets the array and returns it
    """
    fin = open("accounts.txt","r")
    array = []

    while True:
        text = fin.readline()
        if(text == ""): break
        array.append(Person(*text))
    fin.close()
    return array

def is_registered(id):
    """
    Checks is a person is registered and returns a boolean
    """
    array = get_array()
    for i in range(len(array)):
        if (array[i].id == id):
            return True
    return False

def register(id,name):
    """
    Makes sure that the username being registered is valid before registering
    """
    for i in range(len(name)):
        if("1234567890qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM ".find(name[i]) == -1):
            return "This username is not valid, no special characters are allowed"
    fout = open("accounts.txt","w")
    fout.write(Person.blank(id,name))
    return "You have registered sucsessfully"


#Response based on message sent
def get_response(user_input: str,username, nameID, channel) -> str:
    text = ""
    return_channel = channel
    lowered: str = user_input.lower()


    #Return a random string when the criteria are met, a little trolling
    if ((lowered.find("what") != -1) & (len(lowered)>10) & (lowered.count(" ") > 4)) or(randint(1,1000) == 120):
        text = choice(["Ah shit, here we go again ...",
                      "Let's go, open up, it's time for parkour",
                      "What will the next act entail?",
                      "It's becuase this amuses me",
                      "How many times has it been now...",
                      "Now then, play it out for me",
                      "I am afraid I cannot allow you to proceed",
                      "And that's the real battle here",
                      "You shall face dispair",
                      "Let's just hear him out",
                      "You must yeild",
                      "That's what it's all about",
                      "Must this go on?",
                      "Sometimes, it is better to simply not",
                      "Once more",
                      "Keep it Comming",
                      "What statistical value does this have",
                      "Why must things have to go this way?",
                      "Wow that was really cool :thumbs_up:",
                      "I am not crazy!",
                      "I know he swapped those numbers!",
                      "And there's nothing more American than shooting a man in this Walmart of a world",
                      "Check the internet lately?",
                      "You're not cringe. You're just fucking racist",
                      "The value of a human life is negative",
                      "Your IQ is the room tempature of Alaska",
                      "I am Papa's special fucking boy!",
                      "I can see sounds",
                      "I can hear colours",
                      "I forgot how to shit",
                      "Oh Stewie, I'm so full off poo",
                      "GORP!",
                      "Fish",
                      "gay",
                      "Error 420: KYS",
                      "This is why we can't have nice things",
                      "Why must you be like this?",
                      "Why can't you just be normal?",
                      "Someone grab the popcorn",
                      "Everybody do the flop",
                      "Cookie's are pretty tasty",
                      "0.25 A presses",
                      'Well TJ """"""""""Henry"""""""""" Yoshi',
                      "You need to update your home to the death barrier",
                      "Is that a mother fucking mistake edition reference?",
                      "Is that a Jojo's refernce",
                      "Where it all began...",
                      "Let's go back to 1-1",
                      "Preheat the oven to 350",
                      "I'm hot stuff",
                      "May be slow, no need to rush you",
                      "This is the end of it all as we know it",
                      "Just Lean",
                      "How can this be?",
                      "What is truely your plan here?",
                      "I am Retep",
                      "I am evil Peter",
                      "merry christmas",
                      "||Haste||",
                      "When Village Done?",
                      "No changes were made",
                      "Everyone! Get in the car! We're leaving this town, NOW!",
                      "Hurmet!!!! Purple!!",
                      "Ah! What the?! This isn't the car!!!",
                      "Breads done",
                      "Yeah x is just a value of x"
                      ])

    #Register
    elif(lowered.startswith(",register ")):
        if(is_registered(nameID)):
            text = "You are already registered nerd"
        else:
            register(nameID, user_input.split(" ")[1])


   #Error lines if the command is invalid
    elif lowered.startswith(","):
        text = choice([
            "not valid",
            "Trolled Idiot",
            "gay",
            ":banana:"
        ])
   
    return text, return_channel