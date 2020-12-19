#runbotwindows.py with all schools instead of only one
import instabot
import time
import random
import os

def main():
    bot = instabot.Bot()
    bot.login()
    pauseseconds = random.randrange(40, 60, 1)
    counter = 1

    while(True):
        photoversion = random.randrange(1, 6);
        if photoversion == 1: #Irvington
            os.system("copy ihsww.jpg ihswwcopy.jpg")
            bot.upload_photo("ihswwcopy.jpg", caption="#ihsww20")
            print("Waiting: ", pauseseconds)
            print("Number of posts: ", counter)
            counter += 1
            time.sleep(pauseseconds)
            pauseseconds = random.randrange(40, 60, 1)
            os.system("del \\f ihswwcopy.jpg.REMOVE_ME")
        elif photoversion == 2: #American
            os.system("copy ahsww.jpg ahswwcopy.jpg")
            bot.upload_photo("ahswwcopy.jpg", caption="#ahstakeover2020")
            print("Waiting: ", pauseseconds)
            print("Number of posts: ", counter)
            counter += 1
            time.sleep(pauseseconds)
            pauseseconds = random.randrange(40, 60, 1)
            os.system("del \\f ahswwcopy.jpg.REMOVE_ME")
        elif photoversion == 3: #Washington
            os.system("copy whsww.jpg whswwcopy.jpg")
            bot.upload_photo("whswwcopy.jpg", caption="#whsww2020")
            print("Waiting: ", pauseseconds)
            print("Number of posts: ", counter)
            counter += 1
            time.sleep(pauseseconds)
            pauseseconds = random.randrange(40, 60, 1)
            os.system("del \\f whswwcopy.jpg.REMOVE_ME")
        elif photoversion == 4: #Kennedy
            os.system("copy jfkww.jpg jfkwwcopy.jpg")
            bot.upload_photo("jfkwwcopy.jpg", caption="#jfkww20")
            print("Waiting: ", pauseseconds)
            print("Number of posts: ", counter)
            counter += 1
            time.sleep(pauseseconds)
            pauseseconds = random.randrange(40, 60, 1)
            os.system("del \\f jfkwwcopy.jpg.REMOVE_ME")
        else: #Mission
            os.system("copy msjww.jpg msjwwcopy.jpg")
            bot.upload_photo("msjwwcopy.jpg", caption="#msjww20")
            print("Waiting: ", pauseseconds)
            print("Number of posts: ", counter)
            counter += 1
            time.sleep(pauseseconds)
            pauseseconds = random.randrange(40, 60, 1)
            os.system("del \\f msjwwcopy.jpg.REMOVE_ME")

if __name__ == "__main__":
	main()
