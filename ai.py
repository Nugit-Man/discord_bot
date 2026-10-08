from random import randint

def is_ai(dud):
    register = get_array("ai/channels.txt")
    for i in range(len(register)):
        if(int(register[i]) == dud):
            return True
    return False

def count_lines(file):
    """Counts the lines in a given file and returns how many lines there are"""

    count = 0
    fin = open(file,"r")
    while True:
        text = fin.readline()
        if(text == ""):
            fin.close()
            return count
        count += 1



def get_message(q):
    """Is given a question and returns a boolean if it has an answer and a string containing the answer"""
    fin = open("ai/brain.txt","r")
    while True:
        text = fin.readline()
        if (text == ""):
            fin.close()
            return False,""
        elif(text.split("\t") [0] == q):
            return True, text.split("\t") [1]
        
def get_array(file):
    """
    gets the array and returns it
    """
    fin = open(file,"r")
    array = []

    while True:
        text = fin.readline()
        if(text == ""): break
        array.append(text.strip())
    fin.close()
    return array

def save(array,file):
    """takes an array and save it to the file"""
    fout = open(file, "w")
    for i in range(len(array)):
        fout.write(array[i]+"\n")
    fout.close()

def main(message,channel):
    """The main ai function, returns message and channel to send"""
    outgoing = get_array("ai/asking.txt")
    brain = get_array("ai/brain.txt")
    register = get_array("ai/channels.txt")

    #Step 1, check if the user is filling out a request
    for i in range(len(outgoing)):
        if(int(outgoing[i].split("\t")[1]) == channel):

            #If found, add it to brain
            brain.append(outgoing[i].split("\t")[2]+"\t"+message)
            
            #prepare returns
            return_channel = int(outgoing[i].split("\t")[0])
            return_text = message

            #remove from requests and save
            outgoing.pop(i)
            save(outgoing,"ai/asking.txt")
            save(brain,"ai/brain.txt")
            return return_text, return_channel

    #Step 2, Now that we know they are not furfilling a message, it means they must be making one
    #Lets see if the message they want is in the brain first
    for i in range(len(brain)):
        if(brain[i].split("\t") [0] == message.strip()):
            return brain[i].split("\t")[1], channel

    #Step 3, since it is not in the brain, we will have to ask someone to furfill that request
    #There are a few steps that need to be made before we can send it off to someone
    #First, we need to make sure that there is some avilible space to put it
    #If outgoing +1 = register then there is no room
    #The +1 is because we have to offset the fact that we know the current user is not furfilling a request as they would be in step 1
    #And we do not want them sending the message to theirselves
    if(len(outgoing) +1 == len(register)):
        return "Sorry, ai is overloaded currently, please try again later", channel
    
    #Second, we need to make sure that the user doesn't already have a request already waiting a response
    #Probably should have done this step one, but it should still work in this order
    for i in range(len(outgoing)):
        print(i)
        print(outgoing[i])
        if (int(outgoing[i].split("\t") [0]) == channel):
            return "Please wait for your first request to finish", channel

    print("I should not have removed all of this crap")
    #Step 4, time to send out the message to a random person that is not the person sending the message

    #Part 1: Pull all possible channels
    for i in range(len(outgoing)):
        for j in range(len(register)):
            if (outgoing[i].split("\t")[1] == register [j]):
                register.pop(j)

    #Part 1.5: make sure it does not go to the same person
    for i in range(len(register)):
        if (channel == int(register[i])):
            register.pop(i)
            break

    #Part 2: select one at random
    num = randint(1,len(register))

    #Part 3: add it to outgoing
    outgoing.append(str(channel)+"\t"+register[num-1]+"\t"+message)

    #Part 4: Save outgoing
    save(outgoing,"ai/asking.txt")

    #Part 5: Return Everything
    return "Make a response for the following: "+message, int(register[num-1])

    #Part 6: Profit