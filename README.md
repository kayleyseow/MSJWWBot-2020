# MSJWWBot 2020  
**The 2020 version of [Dylan](https://github.com/Dylan102938)'s [winter week bot from 2019](https://github.com/Dylan102938/msjwwBot).** I forked his repository and modified my bots off of his original code.  

## About
This repository contains the code for multiple automatic bots for posting the #msjww20 hashtag on Instagram.

## Repository Navigation
**Here is a quick guide to the [MSJWWBot 2020](https://github.com/kayleyseow/MSJWWBot-2020) repository. If you are looking for a specific file or want to know what each file is for, this should help you.**
- [```runbotwindows.py```](https://github.com/kayleyseow/MSJWWBot-2020/blob/master/runbotwindows.py) is the original bot from [msjwwBot](https://github.com/Dylan102938/msjwwBot), which runs on Windows OS devices. I have modified it slightly to post an up to date photo and caption. This is also the file with heavily detailed comments — chances are if there is something that is uncommented and does not make too much sense in the other files, the information you need is probably in a comment in this file.
- [```runbotmacos.py```](https://github.com/kayleyseow/MSJWWBot-2020/blob/master/runbotmacos.py) is the original bot from [msjwwBot](https://github.com/Dylan102938/msjwwBot), which runs on MacOS devices. I have modified it slightly to post an up to date photo and caption.
- [```runbotall.py```](https://github.com/kayleyseow/MSJWWBot-2020/blob/master/runbotall.py) is a modified version of [```runbotwindows.py```](https://github.com/kayleyseow/MSJWWBot-2020/blob/master/runbotwindows.py). This bot aims to aims to spread winter week spirit by posting for other schools as well. 
- [```runbotspeed.py```](https://github.com/kayleyseow/MSJWWBot-2020/blob/master/runbotspeed.py) is a modified version of [```runbotwindows.py```](https://github.com/kayleyseow/MSJWWBot-2020/blob/master/runbotwindows.py). This bot increases the speed at which images are posted to the Instagram account — best suited for a time crunch.
- [```runbotspeedcomments.py```](https://github.com/kayleyseow/MSJWWBot-2020/blob/master/runbotspeedcomments.py) is a modified version of [```runbotspeed.py```](https://github.com/kayleyseow/MSJWWBot-2020/blob/master/runbotspeed.py). Think of this as the ultimate final form of the bot. In addition to an increased posting time, this bot also includes a variety of randomized comments.

## Run The Bot  
**The directions below are directly copied from the [msjwwBot](https://github.com/Dylan102938/msjwwBot) repository and modified to fit [MSJWWBot 2020](https://github.com/kayleyseow/MSJWWBot-2020).**
### How To Run On MacOS
1. Check if Python is installed on your machine. Open a terminal window and type
    * ```bash python --version```
If you receive an error, type
```bash
python3 --version
```
If you receive an error for both, install python from the link below. If a python version is displayed, skip the next step.

2. Install Python
https://www.python.org/ftp/python/3.7.6/python-3.7.6-macosx10.9.pkg

3. Change directory to Desktop.
```bash
cd Desktop
```

4. Clone this repository. If the below command does not work, you can manually download the zip file by pressing the top green "Clone or Download" button located in the top right corner of the page and move the unzipped folder to your Desktop.
```bash
git clone https://github.com/Dylan102938/msjwwBot.git
```

5. Change directory to msjwwBot
```bash
cd msjwwBot
```

6. Install the instabot library.
```bash
pip install instabot
```
Alternatively, if that doesn't work, run
```bash
pip3 install instabot
```

7. If you used pip3, type the below command with python3 as opposed to python.
```bash
python runbot.py
```

8. Follow the instructions on screen to log into a bot Instagram account.
### How To Run On Windows
## Demo
## Further Hacking
