# spicy-bot
a content generator for the spicy-memes page

## How does it work?
In order to upload memes the bot looks for images in "./images" and .txt files in "./descriptions". It selects a random image from the "./images" directory to upload. The title and description of a meme are both a random line from a random .txt file in "./descriptions".
You can use your own image and .txt files or use the _train-system_

## Train-System
The train-system can download images for you into "./images" and random texts into "./descriptions". Images are downloaded by default from "https://www.reddit.com/r/images/new/". The created .txt file in "descriptions" contains the titles of posts in "https://www.reddit.com/r/funny/new/" line by line.
To download images type: **python spicybot.py trainImages number**
To download texts type: **python spicybot.py trainDescriptions number**
_Number_ describes the number of pages of a subreddit that are downloaded (usually 25 items per page)

## Bot usage
The tool will support diffrent kinds of bots in the future. For now there is only a bot which can upload memes. To do so make sure that the directories "./descriptions" and "./images" are not empty and type: **python spicybot.py botUpload number1 number2**
_Number1_ describes the number of diffrent bots that will be created, _Number2_ describes the number of memes that each bot will upload.
