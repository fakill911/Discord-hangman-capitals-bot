import discord
import random
import re
import asyncio
from discord.ext import commands

def split(word):
    return [char for char in word]

def list_to_word(res):
    res = ''.join(res)
    return (res)

client = commands.Bot(command_prefix='.')
client = discord.Client()

@client.event
async def on_ready():
    print("Bot starting")
    await client.change_presence(activity=discord.Game(name="Under construction"))

@client.event
async def on_message(message):
    global Hangman,unhiden,capital,tries,max_tries
    if message.content.lower() == "BOO":
        await message.channel.send("AAAaAAaaaaAAAAAaAAA")
    if message.author.bot:
        return
    if str(message.channel) != 'bots':
        return

    if message.content.lower() == ".capitals":
        max_tries = 7
        unhiden = []
        capital = []
        tries = 0
        text_file_out_R = text_file_out = []
        text_file_out_R = open("countries.txt", "r")
        text_file_out = text_file_out_R.readlines()
        capital = random.choice(text_file_out).lower()
        capital = capital.split(", ")
        letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's',
                   't', 'u', 'v', 'w', 'x', 'y', 'z']
        unhiden = split(capital[1])
        unhiden = list_to_word(unhiden)
        unhiden = unhiden.rstrip("\n")
        for x in letters:
            if x in capital[1]:
                capital[1] = capital[1].replace(x, '◯')
        capital[1] = list(split(capital[1]))
        await message.channel.send("Game of Capitals Starting.. To stop, type .halt\n\n")
        await message.channel.send("""`                                                                      
 _                                    
| |_  ____ _ _  __ _ _ __  __ _ _ _  
| - \/ -  | - \/ -  |  - \/ -  | - \ 
|_||_\__,_|_||_\__, |_|_|_\__,_|_||_|
               |___/                                                                                                                      
        `""")
        await message.channel.send("What is the capital of: ** "+capital[0].upper()+" **\n"+list_to_word(capital[1])+"\n")
        Hangman=True
    try:
        if Hangman is True:
            if message.content.lower() == unhiden:
                await message.channel.send("**"+str(message.author)+"** Wins <:happyday:423943534375338005>\nThe answer was: "+str(unhiden))
                Hangman=False
            if message.content.lower() == ".halt" or (tries == max_tries):
                Hangman = False
                await message.channel.send("Game Over!\n\n The answer was: " + list_to_word(unhiden) + "\n")
                return

            if unhiden != list_to_word(capital[1]).rstrip("\n"):
                if (str.isalpha(message.content)) and (len(message.content.lower())==1):
                    if message.content.lower() in unhiden:
                        for n, j in enumerate(unhiden):
                            if j == message.content.lower():
                                capital[1][n] = message.content.lower()
                        await message.channel.send("Goode <:nice:405424904436056075>\nWhat's the Capital of: **"+capital[0].upper()+"**\n"+list_to_word(capital[1])+"\n\n")
                    else:
                        await message.channel.send("Wronge <:angrycry:532256681300721665> you haef "+str(max_tries - tries)+" tries left\nWhat's the Capital of : **"+capital[0].upper()+"**\n"+list_to_word(capital[1])+"\n")
                        tries += 1
                else:
                    pass
            if unhiden == list_to_word(capital[1]).rstrip("\n"):
                Hangman = False
                await message.channel.send("Game Over!\n\n The answer was: **"+list_to_word(unhiden)+"**\n"+"You win **"+str(message.author)+"** I guess")
    except:
        
        
        print("wut is bool Hangman mate!")
botToken = 'Put your token here'
client.run(botToken)