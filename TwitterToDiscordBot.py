import discord
from discord.ext import commands
import random
import tweepy
import asyncio
from collections import deque

description = '''An example bot to showcase the discord.ext.commands extension
module.
There are a number of utility commands being showcased here.'''

bot = commands.Bot(command_prefix='?', description=description)

# You need to get all keys and secret from twitter and input them below
# the discord bot token goes all the way at the bottom

CONSUMER_KEY = ''
CONSUMER_SECRET = ''
ACCESS_KEY = ''
ACCESS_SECRET = ''

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)

api = tweepy.API(auth)

@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')

@bot.command()
async def add(left : int, right : int):
    """Adds two numbers together."""
    await bot.say(left + right)

@bot.command()
async def roll(dice : str):
    """Rolls a dice in NdN format."""
    try:
        rolls, limit = map(int, dice.split('d'))
    except Exception:
        await bot.say('Format has to be in NdN!')
        return

    result = ', '.join(str(random.randint(1, limit)) for r in range(rolls))
    await bot.say(result)

@bot.command(description='For when you wanna settle the score some other way')
async def choose(*choices : str):
    """Chooses between multiple choices."""
    await bot.say(random.choice(choices))

@bot.command()
async def repeat(times : int, content='repeating...'):
    """Repeats a message multiple times."""
    for i in range(times):
        await bot.say(content)

def requestSong(songURL):
   bot.say('!play ' + songURL)

@bot.command()
async def joined(member : discord.Member):
    """Says when a member joined."""
    await bot.say('{0.name} joined in {0.joined_at}'.format(member))

@bot.group(pass_context=True)
async def cool(ctx):
    """Says if a user is cool.
    In reality this just checks if a subcommand is being invoked.
    """
    if ctx.invoked_subcommand is None:
        await bot.say('No, {0.subcommand_passed} is not cool'.format(ctx))

@cool.command(name='bot')
async def _bot():
    """Is the bot cool?"""
    await bot.say('Yes, the bot is cool.')

def parse_string(string_to_parse):
    parsed_string = string_to_parse.split(" ", 2)
    print(parsed_string)
    print(parsed_string[1])
    return parsed_string[1]

# Calls to twitter API to get most recent mention and parses
# the tweet out and sends it over to discord
async def my_background_task():
    await bot.wait_until_ready()
    previous_songs = deque(maxlen=5)
    counter = 0
    channel = discord.Object(id='***Channel ID to be connected to***')
    previous = ''
    while not bot.is_closed:
        song_to_play = get_mention()
        counter += 1
        if same_song(song_to_play, previous) | song_already_played(previous_songs, song_to_play):
            print('This song has already been played recently.')
        else:
            await bot.send_message(channel, '!play ' + song_to_play)
            # set previous to song_to_play to check if the next song is the same
            previous = song_to_play
            if len(previous_songs) == 5:
                previous_songs.popleft()
            previous_songs.append(previous)
        await asyncio.sleep(60) # task runs every 60 seconds


# returns parsed song link
def get_mention():
    songlink = ''
    mentions = api.mentions_timeline(count=1)
    for mention in mentions:
        print(mention.text + " >>  " + mention.user.screen_name)
        songlink = parse_string(mention.text)
    return songlink


def same_song(song1, song2):
    if song1 is song2:
        return True
    else:
        return False


def song_already_played(list_of_songs, song_to_play):
    for elem in list_of_songs:
        if elem == song_to_play:
            return True
    return False

bot.loop.create_task(my_background_task())
bot.run('Discord Bot User Token')