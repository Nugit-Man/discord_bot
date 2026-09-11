from random import choice, randint
import os
import math
from objects import Person


def get_place(array,id):
    """
    Is given an array and an ID and finds where the ID is in the array, returns a -1 if it is not found
    """
    for i in range(len(array)):
        if (array[i].id == id):
            return i
    return -1

def get_array():
    """
    gets the array and returns it
    """
    fin = open("accounts.txt","r")
    array = []

    while True:
        text = fin.readline()
        if(text == ""): break
        array.append(Person(text.split(",")))
    fin.close()
    return array

def save_array(array):
    """
    Saves the array to the file
    """
    fout = open("accounts.txt","w")
    for i in range(len(array)):
        fout.write(array[i].tostr()+"\n")

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
    fout = open("accounts.txt","a")
    fout.write(Person.blank(id,name)+"\n")
    return "You have registered sucsessfully"

def drinks(id):
    array = get_array()
    place = get_place(array,id)
    if (place == -1):
        return "You are not registered"
    array[place].beer_count += 1
    save_array(array)
    return f"You drank a beer! You have drank {array[place].beer_count} beers"

def beef_dip(message,id):
    """
    everything to do with the beef dip command
    """
    array = get_array()
    place = get_place(array,id)


    if(message == "count"):
        count = array[place].beef_dip_count
        return f"You have had {count} beef dips"
    elif(message == "rank"):
            count = array[place].beef_dip_rank
            return f"You are a rank {count} beef dipper"
    elif(message == "have"):
        if(array[place].beef_dip_rank == 5):
            array[place].beef_dip_count += 1
            save_array(array)
            return "You have beef dipped"
        else:
            return "Only a tier 5 beef dipper can do this"
    elif(message.startswith("<@")):
        if(array[place].beef_dip_rank != 5):
            return "Only a tier 5 beef dipper can do this"
        #Add a beef dip for everyone who ate a beef dip together
        unregistered = 0
        registered = 0

        for i in range(message.count("@")):
            find = int(message.split("@") [i+1].split(">")[0])
            spot = get_place(array,find)
            if(spot != -1):
                registered += 1
                array[spot].beef_dip_count += 1
            else: unregistered += 1
        save_array(array)

        if(unregistered != 0):
            return f"Added a beef dip to {registered} users. {unregistered} are not registered"
        else:
            return f"{registered} people beef dipped"
    elif(message == "help"):
        return """`count` show how many times you beef dipped
`rank` see your beef dip rank
`have` up your beef dip counter by 1
`<ping someone> <ping someone>` up those peoples beef dip counter by 1
`help` see this message"""
    else:
        return "Please use a sub-command or do `help` for a list of sub commands"

def hourly():
    """
    Pulls the current hourly value
    """
    fin = open("global.txt","r")
    text = fin.readline()
    text = text.split(":") [1]
    fin.close()
    return int(text)

def reset_hourly():
    """
    Resets the hourly value in global to 0
    """
    fin = open("global.txt","r")
    list = []

    #Read from the file
    while True:
        text = fin.readline().strip()
        if (text == ""):
            break
        list.append(text)
    fin.close()

    #Make the change
    change = list[0]
    list[0] = change [:-1] +"0"

    #Put it all back into the file
    fout = open("global.txt","w")
    for i in range(len(list)):
        fout.write(list[i]+"\n")
    fout.close()

def money(message,id):
    """
    Dealing with the money command, getting the bonus and seeing your streak
    """
    array = get_array()
    place = get_place(array,id)

    #Check if the hourly bonus is ready
    if(hourly() != 0):
        bonus = hourly() + array[place].money_streak + 2
        reset_hourly()
        array[place].money_streak += 1
        for i in range(len(array)):
            if(array[place].id != id):
                array[place].money_streak = 0

        array[place].money += bonus
        save_array(array)

        return f"You got the ${money} bonus"
    elif(message == "streak"):
        return f"You currently have a {array[place].money_streak} streak"
    elif(message == "amount"):
        return f"You have ${array[place].money}"
    elif(message == "help"):
        return """`streak` see your current money streak
`amount` view your current balence
(top of every hour) get the hourly bonus
`help` see this message"""



    return "Please add a sub command or use `help` for a list of sub commands"

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
            text = register(nameID, user_input.split(" ")[1])

    #Add a drink
    elif(lowered.startswith(",drink")):
        if(not is_registered(nameID)):
            text = "You are not registered"
        else:
            text = drinks(nameID)

    #Beef dip command
    elif(lowered.startswith(",beef dip")):
        if(not is_registered(nameID)):
                    text = "You are not registered"
        else:
            lowered = lowered [10:]
            text = beef_dip(lowered,nameID)
    elif(lowered.startswith(",beefdip")):
        if(not is_registered(nameID)):
                    text = "You are not registered"
        else:
            lowered = lowered [9:]
            text = beef_dip(lowered,nameID)

    #The money command
    elif(lowered.startswith(",money")):
        if(not is_registered(nameID)):
            text = "You are not registered"
        else:
            lowered = lowered [7:]
            text = money(nameID)

   #Error lines if the command is invalid
    elif lowered.startswith(","):
        text = choice([
            "not valid",
            "Trolled Idiot",
            "gay",
            ":banana:"
        ])
   
    return text, return_channel