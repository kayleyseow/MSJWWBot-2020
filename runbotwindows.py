#Dylan's original bot code with slight modifications
#And yes, a lot of comments for understanding
import instabot
import time
import random
import os


def main():
    bot = instabot.Bot()
    bot.login()
    pauseseconds = random.randrange(40, 60, 1) #random number between 40 and 60, step by 1
    os.system("copy msjww.jpg msjwwcopy.jpg") #copies a new file of the photo
    counter = 1 #counts number of posts posted

    while(True):
        bot.upload_photo("msjwwcopy.jpg", caption="#msjww20") #upload the photo to instagram with a caption
        print("Waiting: ", pauseseconds)  #prints out number of seconds until next photo post
        print("Number of posts: ", counter) #prints out number of posts posted by Bot
        counter += 1 #increments posted counter
        time.sleep(pauseseconds) #pause posting for random number of seconds
        pauseseconds = random.randrange(40, 60, 1) #same as above
        os.system("del \\f msjwwcopy.jpg.REMOVE_ME") #delete the copy of the photo
        os.system("copy msjww.jpg msjwwcopy.jpg") #copy the photo again for the next round

if __name__ == "__main__":
	main() #run main
