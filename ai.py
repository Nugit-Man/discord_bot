import random

def is_in_database():
    return 0


def get_response():
    return 0

def get_channels():
    return 0

def pop_channel():
    return 0

def log_response():
    return 0

#Did not check if it was a resone make
def message(channel, message):
    #Check if the response is already in the database
    if(is_in_database(message)):
        return channel, get_response(message)
    

    #assing it to a random channel
    channels_list = get_channels()
    channels_list = pop_channel(channels_list)

    index = channels_list[random.randint(0,len(channels_list)-1)]

    log_response(index,message)
    return index,f"Please make a response to this message: {index}"