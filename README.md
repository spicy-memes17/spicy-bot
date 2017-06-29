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
Please make sure that the directories "./descriptions" and "./images" are not empty.

Upload: **python spicybot.py  botUpload  number1  number2**  
_Number1_ describes the number of diffrent bots that will be created, _Number2_ describes the number of memes that each bot will upload.

Upvote: **python spicybot.py  botUpvote  number1  number2  number3  number4**  
_Number1_ describes the number of diffrent bots that will be created, _Number2_ describes a lower and _Number3_ a upper bound for the IDs of posts that will be handled, each bot tries to upvote _Number4_ posts between the lower and upper bound.

Downvote: **python spicybot.py  botDownvote  number1  number2  number3  number4**  
_Number1_ describes the number of diffrent bots that will be created, _Number2_ describes a lower and _Number3_ a upper bound for the IDs of posts that will be handled, each bot tries to downvote _Number4_ posts between the lower and upper bound.

Comment: **python spicybot.py  botComment  number1  number2  number3  number4**  
_Number1_ describes the number of diffrent bots that will be created, _Number2_ describes a lower and _Number3_ a upper bound for the IDs of posts that will be handled, each bot tries to comment _Number4_ posts between the lower and upper bound.
