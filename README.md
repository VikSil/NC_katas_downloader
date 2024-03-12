# NC katas downloader

This script will help you download exercises ("*katas*") from Northcoders web-development bootcamp webpage. You will need to provide credentials to access these exercises, i.e. you will need to have received authorisation by Northcoders. The script is intended for the use of former Northcoders students.

## Prerequisites

The following assumptions are made about the user of this script:

* You are running this script on a Windows machine. 
* You have Chrome web browser installed on your machine.
* You have Python, pip and git installed on your machine.
* You have ticked off at least one task in each chapter as complete (if you have not, tick off the first task before running this script).
* You have ticked off consecutive tasks (if you have ticked off more advanced tasks in a chapter before ticking off less advanced ones, tick them all off before running this script).

## Setup and installation

First things, first - git clone this repo to your machine:

    
    git clone https://github.com/VikSil/NC_katas_downloader.git
    

In order to run this script you will need to find out which version of Chrome browser do you use and get a driver for it. [Here](https://www.youtube.com/watch?v=Yh4CnDL44O8) is a video tutorial on how to get the driver (watch up to 2:00). Alternatively  you may follow these steps:

1. In your Chrome browser go to this url: `chrome://settings/help` and note down the version
1. Go to [this](https://chromedriver.chromium.org/downloads) page and find the ChromeDriver for your Chrome version. If the version is new, you may have to read the text in red at the top of the page and go to **Chrome for Testing availability dashboard** to find the appropriate driver. N.B. The dashboard is frequently unavailable, if it does not work - check back later.
1. Download the appropriate driver for your Chrome version, operating system (Windows) and processor.
1. Unzip the contents of the distributable into a `drivers` directory in the root folder of your project (where the main.py file is). There should be a `chromedriver.exe` file `drivers` directory now.

Run the following command to install dependencies (this will take several minutes to complete):

    pip install -r requirements.txt

Add into the `config.py` file:
    
* email and password that you would normally use to log into Northcoders website. If you have not been authorised by Northcoders, unfortunately, you cannot use this script (access restrictions to individual exercises may also apply).
* a list of links to the first page for every chapter that you want to download.
* root - the download directory as absolute path if you want to download the files to a specific location. By default the download directory is where the script is run from.
* timers - you may want to increase the default timer values if your internet connection is slow.

You should be ready to run the script now.

## Execution

To start the script run the following command :

    python main.py

This will cause a Chrome web browser to pop up and from there all webpages will be accessed and saved automatically.

🔴❗ DO NOT INTERACT WITH THE COMPUTER WHILE THE SCRIPT IS RUNNING❗🔴

The script is designed to always have focus on the browser window. If you click away from the browser, the script will not be able to save webpages and will exit with an error. You will be able to follow the progress by reading the messages that will be output to the console. 

# Disclaimer

This script was developed independently from Northcoders and will only work for as long as nothing is changed on the Northcoders website. Beyond this point the script will not be maintained. Obviously, it is under Northcoders sole discretion who is authorised to access their website, to what extent the access is granted, or when it may be revoked.