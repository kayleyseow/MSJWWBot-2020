# I AM SPEED
import instabot
import time
import random
import os


def main():
    bot = instabot.Bot()
    bot.login()
    pauseseconds = random.randrange(1, 5)
    os.system("copy msjww.jpg msjwwcopy.jpg")
    counter = 1;

    while(True):
        bot.upload_photo("msjwwcopy.jpg", caption="#msjww20")
        print("Waiting: ", pauseseconds)
        print("Number of posts: ", counter)
        counter += 1
        time.sleep(pauseseconds)
        pauseseconds = random.randrange(1, 5)
        os.system("del \\f msjwwcopy.jpg.REMOVE_ME")
        os.system("copy msjww.jpg msjwwcopy.jpg")

if __name__ == "__main__":
	main() #run main
