# Tweet-Me-A-Song
Tweet @ a Twitter bot application with a link to a YouTube or Soundcloud video/song and have the link sent to discord!

## What can it do?
This is an idea I had thought about for a while. Going to parties and places with DJs it's always an annoying process having to go up and scream your song request to them or write it down. So I made this bot in order to set up your own personal DJ bot. It does require you use MusicBot (info below) but it can manage playlists, skip songs, blacklist songs, custom playlists and the main implementation of the Tweet Me A Song bot is that it will parse a tweet sent to any twitter bot user of your liking which you must setup and send it to discord in the format of a play request sent to MusicBot. MusicBot does all the hard stuff and plays the songs as mentioned above. Look below in "Commands" for example

## Dependencies and Info

This bot is HIGHLY dependent on and runs side by side a discord Music Bot found here https://github.com/SexualRhinoceros/MusicBot in order to manage playlists as well as playing the songs through discord.

Tweepy the Twitter API library/wrapper is also required in order for this bot to work found here https://github.com/tweepy/tweepy

Tweepy can be cloned or you can use pip to install it, and MusicBot has multiple dependencies for the discord library which can beinstalled using pip.

## Getting up and running
Most information required to get this bot up and running can be found on the provided GitHub repositories posted above. Currently there is no output to console for this bot, but just open up your console and type 

`run TwitterToDiscordBot.py` 

in order to start it and it will call to the Twitter API every 60 seconds or however long you input into 

`await asyncio.sleep(60) # task runs every 60 seconds`

Once you have both the MusicBot and TwitterToDiscordBot discord applications setup, go ahead and replace the file
`permission.ini` in the MusicBot config folder with the one I provided in this repo to allow your TwitterToDiscordBot to request songs or else the !play request will be ignored by MusicBot.

## Commands
The bot is currently only configured to get the most recent tweet, but at the moment that's really all that matters unless you expect to get more than one tweet every 60 seconds. The tweet format is as follows

`@TwitterBotHandle <YouTube/SoundCloud Link>`

And that's it. The bot parses by spaces so ' ' though only the first, second and third space is parsed and then pics out the string in the middle of the first and second space. Unfortunately there is no error returned for invalid links or bad entries either in the console of the bot itself, you can manage that through Discord.

### More documentation/info to be made/added soon...
