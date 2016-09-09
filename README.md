# Tweet-Me-A-Song
Tweet @ a Twitter bot application with a link to a YouTube or Soundcloud video/song and have the link sent to discord!

## Dependencies and Info

This bot is HIGHLY dependent on and runs side by side a discord Music Bot found here https://github.com/SexualRhinoceros/MusicBot in order to manage playlists as well as playing the songs through discord.

Tweepy the Twitter API library/wrapper is also required in order for this bot to work found here https://github.com/tweepy/tweepy

Tweepy can be cloned or you can use pip to install it, and MusicBot has multiple dependencies for the discord library which can beinstalled using pip.

## Getting up and running
Most information required to get this bot up and running can be found on the provided GitHub repositories posted above. Currently there is no output to console for this bot, but just open up your console and type 

`run TwitterToDiscordBot.py` 

in order to start it and it will call to the Twitter API every 60 seconds or however long you input into 

`await asyncio.sleep(60) # task runs every 60 seconds`

### More documentation/info to be made/added soon...
