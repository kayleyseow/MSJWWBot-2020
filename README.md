# MSJWWBot 2020  
**The 2020 version of [Dylan](https://github.com/Dylan102938)'s [winter week bot from 2019](https://github.com/Dylan102938/msjwwBot).** I forked his repository and modified my automation off of his original code.  
**Shortcuts: [About](https://github.com/kayleyseow/MSJWWBot-2020#about), [Repository Navigation](https://github.com/kayleyseow/MSJWWBot-2020#repository-navigation), [Run The Automation](https://github.com/kayleyseow/MSJWWBot-2020#run-the-automation), [Demo](https://github.com/kayleyseow/MSJWWBot-2020#demo), [Further Hacking](https://github.com/kayleyseow/MSJWWBot-2020#further-hacking).**

## About
This repository contains the code for multiple automatic bots for posting the #msjww20 hashtag on Instagram.

## Repository Navigation
**Here is a quick guide to the [MSJWWBot 2020](https://github.com/kayleyseow/MSJWWBot-2020) repository. If you are looking for a specific file or want to know what each file is for, this should help you.**
- [```runbotwindows.py```](https://github.com/kayleyseow/MSJWWBot-2020/blob/master/runbotwindows.py) is the original bot from [msjwwBot](https://github.com/Dylan102938/msjwwBot), which runs on Windows OS devices. I have modified it slightly to post an up to date photo and caption. This is also the file with heavily detailed comments — chances are if there is something that is uncommented and does not make too much sense in the other files, the information you need is probably in a comment in this file.
- [```runbotmacos.py```](https://github.com/kayleyseow/MSJWWBot-2020/blob/master/runbotmacos.py) is the original bot from [msjwwBot](https://github.com/Dylan102938/msjwwBot), which runs on MacOS devices. I have modified it slightly to post an up to date photo and caption.
- [```runbotall.py```](https://github.com/kayleyseow/MSJWWBot-2020/blob/master/runbotall.py) is a modified version of [```runbotwindows.py```](https://github.com/kayleyseow/MSJWWBot-2020/blob/master/runbotwindows.py). This bot aims to spread winter week spirit by posting for other schools as well. 
- [```runbotspeed.py```](https://github.com/kayleyseow/MSJWWBot-2020/blob/master/runbotspeed.py) is a modified version of [```runbotwindows.py```](https://github.com/kayleyseow/MSJWWBot-2020/blob/master/runbotwindows.py). This bot increases the speed at which images are posted to the Instagram account — best suited for a time crunch.
- [```runbotspeedcomments.py```](https://github.com/kayleyseow/MSJWWBot-2020/blob/master/runbotspeedcomments.py) is a modified version of [```runbotspeed.py```](https://github.com/kayleyseow/MSJWWBot-2020/blob/master/runbotspeed.py). Think of this as the ultimate final form of the bot. In addition to an increased posting time, this bot also includes a variety of randomized comments.

## Run The Automation  
**The directions below are directly copied from the [msjwwBot](https://github.com/Dylan102938/msjwwBot) repository and modified to fit [MSJWWBot 2020](https://github.com/kayleyseow/MSJWWBot-2020).**  
Slight disclaimer: I use the Windows OS, but followed the MacOS instructions to run the automation because I already had Python installed.  
### How To Run On MacOS
1. Check if Python is installed on your machine. Open a terminal window and type:
      * ```python --version```
   * If you receive an error, type:
      * ```python3 --version```
   * If you receive an error for both, install python from the link below. If a python version is displayed, skip the next step.
2. Install Python at https://www.python.org/ftp/python/3.9.1/python-3.9.1-macosx10.9.pkg.  
3. Change directory to Desktop.
   ```bash 
   cd Desktop 
   ```
4. Clone this repository. If the below command does not work, you can manually download the zip file by pressing the top green "Clone or Download" button located in the top right corner of the page and move the unzipped folder to your Desktop.
   ```bash
   git clone https://github.com/kayleyseow/MSJWWBot-2020.git
   ```
5. Change directory to MSJWWBot-2020:  
   ```bash
   cd MSJWWBot-2020
   ```
6. Install the instabot library.
   ```bash
   pip install instabot
   ```
   * Alternatively, if that doesn't work, run:
      ```bash
      pip3 install instabot
      ```
7. If you used pip3, type the below command with ```python3``` as opposed to ```python```.
   ```bash
   python runbot.py
   ```
8. Follow the instructions on screen to log into an Instagram account you plan to automate.
### How To Run On Windows
1. Install Conda from the following link: https://repo.anaconda.com/miniconda/Miniconda3-latest-Windows-x86_64.exe.
2. Type Miniconda into your Windows search bar located on the bottom left corner of your screen. Press enter. You should see a black, command-prompt like display.
3. Create a conda virtual environment.
     ```bash
     conda update conda
     conda create -n MSJWWBot-2020 python=3.6 pip
     ```
4. Activate your environment.
     ```bash
     conda activate MSJWWBot-2020
     ```
5. Download this repository as a zip file. It should be located on the top right corner of the page and will show up after you click the green "Code" button.
6. Unzip the folder.
7. In your Conda terminal, change directory to the folder path. For example, if I am in C:/Users/xxx/ and my folder is located in Downloads, I would run:
     ```bash
     cd Downloads/MSJWWBot-2020
     ```
8. In your Conda terminal, install instabot.
     ```bash
     pip install instabot
     ```
9. Run the automation file and follow the instructions on screen.
     ```bash
     python runbotwindows.py
     ```
## Demo
From what I have seen, the captions for the automated posting stopped working at around 400 posts. Some examples of automated posting are [@winter_week_2020](https://www.instagram.com/winter_week_2020/) and [@winter_week_2020_2](https://www.instagram.com/winter_week_2020_2/).  
<img src="https://cloud-opyxb0uq8.vercel.app/0image.png" alt="Photo of an automated account" width=41.5%/><img src="https://cloud-opyxb0uq8.vercel.app/1image.png" alt="Photo of an automated post" width=58.5%/>
## Further Hacking
- Automation can be modified for future use. In the code, only the caption and file names need to be changed — everything else should work flawlessly
- New Features:
     - Display of the elapsed time of automation
     - Quit function to break the automation out of the loop
     - Set a number posts instead of having the automation run 
- Expanding On Current Features:
     - Addition of more comments
     - Further randomized posting times
- For this automation, Instabot was used (only the ```login()``` function). To further expand on the automation, you can look through the [Instabot docs](https://instagrambot.github.io/docs/en/) and take a look through the [Instabot instructions for use](https://instagrambot.github.io/docs/en/How_to_use.html) for the other functions and parameters in order to add functionality to the automation. 
