from typing import Final
import os
from dotenv import load_dotenv
from discord import Intents, Client, Message
from respones import get_response
from respones import add_hourly
import time
import asyncio

# STEP 0: LOAD OUR TOKEN FROM SOMEWHERE SAFE
load_dotenv()
TOKEN: Final[str] = os.getenv('DISCORD_TOKEN')

# STEP 1: BOT SETUP
intents: Intents = Intents.default()
intents.message_content = True  # NOQA
intents.members = True  # REQUIRED to access all members
client: Client = Client(intents=intents)
intents.voice_states = True  # 🔥 REQUIRED for voice tracking


# STEP 2: MESSAGE FUNCTIONALITY
async def send_message(message: Message, user_message: str) -> None:
    if not user_message:
        print('(Message was empty because intents were not enabled probably)')
        return

    if is_private := user_message[0] == '?':
        user_message = user_message[1:]

    try:
        response, channel_id = get_response(user_message,str(message.author),message.author.id,message.channel.id)
        if response != "":
            if is_private:
                await message.author.send(response)
            else:
                channel = client.get_channel(channel_id)
                if channel is not None:
                    await channel.send(response)
                else:
                    print(f'Could not find channel with ID: {channel_id}')

    except Exception as e:
        print(e)



# NEW: BACKGROUND TASK
async def update_vc_file():
    while True:
        await asyncio.sleep(0.9)
        if time.asctime().split(" ")[-2].split(":")[1] == "00" and time.asctime().split(" ")[-2].split(":")[2] == "00":
            add_hourly()
            await asyncio.sleep(1)



# STEP 3: HANDLING THE STARTUP FOR OUR BOT
@client.event
async def on_ready() -> None:
    print(f'{client.user} is now running!')
    client.loop.create_task(update_vc_file())  # start background task


# STEP 4: HANDLING INCOMING MESSAGES
@client.event
async def on_message(message: Message) -> None:
    if message.author == client.user:
        return

    username: str = str(message.author)
    user_message: str = message.content
    channel: str = str(message.channel)

    print(f'[{channel}] {username}: "{user_message}"')

    await send_message(message, user_message)


# STEP 5: MAIN ENTRY POINT
def main() -> None:
    client.run(token=TOKEN)


if __name__ == '__main__':
    main()