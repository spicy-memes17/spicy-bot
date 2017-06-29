import sys, requests, os, random, threading, shutil
from train import trainImages, trainDescriptions

#a bot that simulates a user
class botThread (threading.Thread):
    def __init__(self, threadID, username, password, botFunction):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.username = username
        self.password = password
        self.botFunction = botFunction

    #runs the given botfunction
    def run(self):
        print("Starting thread " + self.name)
        self.botFunction(self.username, self.password)
        print("Exiting thread " + self.name)

# important urls
SIGNUP = "http://localhost:8000/spicy_memes/signUp/"
LOGIN = "http://localhost:8000/spicy_memes/loginPage/"
UPLOAD = "http://localhost:8000/spicy_memes/uploadFile"
VOTE = "http://localhost:8000/spicy_memes/post/"
POST = "http://localhost:8000/spicy_memes/post/"

#important files/directories
IMAGES = "./images"
DESCRIPTIONS = "./descriptions"

#loads random image from ./images
def loadRandomImage():
    img = open(IMAGES + "/" + random.choice(os.listdir(IMAGES)), "rb")
    return img

#uses loadRandomDescription for the moment
def loadRandomTitle():
    return loadRandomDescription()

#returns a random line from a random text-file in ./descriptions
def loadRandomDescription():
    f = open(DESCRIPTIONS + "/" + random.choice(os.listdir(DESCRIPTIONS)),"r")
    l = [line for line in f]
    return random.choice(l)[:-1]

#arguments: input data for a new user, returns a session for the created user
def signup(username, email, password):

    client = requests.session() #create a new session
    client.get(SIGNUP)
    csrftoken = client.cookies['csrftoken']
    signupdata = {'csrfmiddlewaretoken' : csrftoken, 'username' : username, 'email' : email, 'password' : password, 'passwordConfirm' : password}
    r = client.post(SIGNUP, data = signupdata)
    return client

#uploads a meme with the following parameters via the account associated with the client-session
def upload(title, description, file, client):
    
    client.get(UPLOAD)
    csrftoken = client.cookies['csrftoken']
    uploaddata = {'csrfmiddlewaretoken' : csrftoken, 'title' : title, 'description' : description}
    r = client.post(UPLOAD, data = uploaddata,  files = {'image_field' : file})

#a function that tries to upvote the post with the specific id 
def upvote(client, id):
    csrftoken = client.cookies['csrftoken']
    uploaddata = {'csrfmiddlewaretoken' : csrftoken}
    r = client.post(VOTE+str(id)+"/1/likePost/", data = uploaddata)

#a function that tries to downvote the post with the specific id 
def downvote(client, id):
    csrftoken = client.cookies['csrftoken']
    uploaddata = {'csrfmiddlewaretoken' : csrftoken}
    r = client.post(VOTE+str(id)+"/0/likePost/", data = uploaddata)

def comment(client, id):
    csrftoken = client.cookies['csrftoken']
    comment = loadRandomDescription()
    uploaddata = {'csrfmiddlewaretoken' : csrftoken, 'content' : comment}
    r = client.post(POST+str(id)+"/comment/", data=uploaddata)


#login for a existing user, returns a new session for this user
def login(username, password):
    client = requests.session() #create a new session
    client.get(LOGIN)
    csrftoken = client.cookies['csrftoken']
    logindata = {'csrfmiddlewaretoken' : csrftoken, 'username' : username, 'password' : password}
    r = client.post(LOGIN, data = logindata)
    return client

#creates and runs number many bots
def run(name, number, botFunction):
    for i in range(number):
        signup(name+str(i), "bot@spicy-memes.de", name+str(i))
        thread = botThread(i, name+str(i), name+str(i), botFunction)
        thread.start()


# a bot function to upload a specific number of posts
def uploadBot(username, password, posts):
    client = login(username, password)
    for i in range(posts):
        upload (loadRandomTitle(), loadRandomDescription(), loadRandomImage(), client)

#a bot that tries to upvote a specific number of posts between lowerID and upperID
def upvoteBot(username, password, lowerID, upperID, number):
    client = login(username, password)
    for i in range(number):
        id = random.choice(range(lowerID, upperID+1))
        upvote(client, id)


#a bot that tries to downvote a specific number of posts between lowerID and upperID
def downvoteBot(username, password, lowerID, upperID, number):
    client = login(username, password)
    for i in range(number):
        id = random.choice(range(lowerID, upperID+1))
        downvote(client, id)

#a bot that tries to comment a specific number of posts between lowerId and upperID
def commentBot(username, password, lowerID, upperID, number):
    client = login(username, password)
    for i in range(number):
        id = random.choice(range(lowerID, upperID+1))
        comment(client, id)



if sys.argv[1] is None:
    print("Usage:")
else:

    if sys.argv[1] == 'trainDescriptions':
        print("Downloading new Titles...")
        trainDescriptions(int(sys.argv[2]))

    elif sys.argv[1] == 'trainImages':
        print("Downloading new Images...")
        trainImages(int(sys.argv[2]))

    elif sys.argv[1] == 'botUpload':
        print("Starting " + str(sys.argv[2]) +  " bots to upload " + str(sys.argv[3]) + " posts each.")
        run("uploadBot", int(sys.argv[2]), lambda username, password: uploadBot(username, password, int(sys.argv[3])))

    elif sys.argv[1] == 'botUpvote':
        print("Starting" + str(sys.argv[2]) + " bots to upvote " + str(sys.argv[5]) + " posts between the IDs " + str(sys.argv[3]) + " and " + str(sys.argv[4]))
        run("upvoteBot", int(sys.argv[2]), lambda username, password: upvoteBot(username, password, int(sys.argv[3]), int(sys.argv[4]), int(sys.argv[5])))

    elif sys.argv[1] == 'botDownvote':
        print("Starting" + str(sys.argv[2]) + " bots to downvote " + str(sys.argv[5]) + " posts between the IDs " + str(sys.argv[3]) + " and " + str(sys.argv[4]))
        run("downvoteBot", int(sys.argv[2]), lambda username, password: downvoteBot(username, password, int(sys.argv[3]), int(sys.argv[4]), int(sys.argv[5])))

    elif sys.argv[1] == 'botComment':
        print("Starting" + str(sys.argv[2]) + " bots to comment " + str(sys.argv[5]) + " posts between the IDs " + str(sys.argv[3]) + " and " + str(sys.argv[4]))
        run("commentBot", int(sys.argv[2]), lambda username, password: commentBot(username, password, int(sys.argv[3]), int(sys.argv[4]), int(sys.argv[5])))
