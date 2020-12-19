#runbotwindows.py at a considerably faster speed with randomized comments
import instabot
import time
import random
import os


def main(): #comments found on runbotwindows.py
    bot = instabot.Bot()
    bot.login()
    pauseseconds = random.randrange(1, 6) #faster range of times between posts
    os.system("copy msjww.jpg msjwwcopy.jpg")
    counter = 1;

    while(True): #comments found on runbotwindows.py
        commentversion = random.randrange(1, 5)
        if commentversion == 1:
            bot.upload_photo("msjwwcopy.jpg", caption="#msjww20")
        elif commentversion == 2:
            bot.upload_photo("msjwwcopy.jpg", caption="Let's go Warriors! #msjww20")
        elif commentversion == 3;
            bot.upload_photo("msjwwcopy.jpg", caption="Work it ayy, work it ayy, MSJ! #msjww20")
        else: #commentversion == 4
            bot.upload_photo("msjwwcopy.jpg", caption="Winter Week Chapions V2 #msjww20")
        print("Waiting: ", pauseseconds)
        print("Number of posts: ", counter)
        counter += 1
        time.sleep(pauseseconds)
        pauseseconds = random.randrange(1, 5) #faster range of times between posts
        os.system("del \\f msjwwcopy.jpg.REMOVE_ME")
        os.system("copy msjww.jpg msjwwcopy.jpg")

if __name__ == "__main__": #comments found on runbotwindows.py
	main()
