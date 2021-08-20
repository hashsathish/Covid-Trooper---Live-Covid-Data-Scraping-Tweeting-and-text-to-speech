# IMPORT 
import csv
import requests
from bs4 import BeautifulSoup
import time
import threading
import math
import tweepy
from tkinter import *
import pyttsx3

# TWITTER CONSUMER AND ACCESS KEY
consumer_key = 'zDWPLuFK9IoGhs5lrXpKqCNBp'
consumer_secret = '2MV94YDcCwtXE54FhYYzk1mngQroA7rWNqajbkipGRcSwAWTQ2'
access_token = '918093653477691394-8VeDioyWHToZJ1P8gJLX0IhgqLMuVhW'
access_token_secret = 'Px6cp5R9iK3c9JzKYeGUROsnxN8b0KZdABNuXLvHDUqeY'

#AUTHENTICATING THE USER VIA THE DEFINED KEY VALUES
auth = tweepy.OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_token,access_token_secret)
api = tweepy.API(auth,wait_on_rate_limit = True)

# LIST OF COUNTRIES
country_list = [   "us",
        "india",
        "russia",
        "uk",
        "france",
        "italy",
        "spain",
        "turkey",
        "germany",
        "colombia",
        "argentina",
        "mexico",
        "poland",
        "iran",
        "south-africa",
        "ukraine",
        "indonesia",
        "peru",
        "netherlands",
        "canada",
        "chile",
        "romania",
        "israel",
        "belgium",
        "portugal",
        "iraq",
        "sweden",
        "philippines",
        "pakistan",
        "switzerland",
        "bangladesh",
        "hungary",
        "serbia",
        "austria",
        "morocco",
        "japan",
        "united-arab-emirates",
        "lebanon",
        "saudi-arabia",
        "panama",
        "malaysia",
        "ecuador",
        "belarus",
        "bulgaria",
        "georgia",
        "nepal",
        "bolivia",
        "azerbaijan",
        "greece",
        "ireland",
        "denmark",
        "kuwait",
        "costa-rica",
        "egypt",
        "qatar",
        "nigeria",
        "libya",
        "oman",
        "myanmar",
        "kenya",
        "algeria",
        "china",
        "sri-lanka",
        "norway",
        "brazil",
        "finland",
        "cuba",
        "singapore",
        "jamaica",
        "thailand",
        "maldives",
        "madagascar",
        "syria",
        "china-hong-kong-sar",
        "somalia",
        "mongolia",
        "viet-nam",
        "guinea",
        "congo",
        "bahamas",
        "benin",
        "iceland",
        "liberia",
        "cambodia",
        "taiwan",
        "bhutan",
        "fiji",
        "new-zealand",
        "australia",
    ]

country = 'NONE'
# SCRAPING SELECTED COVID DATA AND STORING IT IN FILENAME.TXT
def getCases(start, end, c):
    
    # OPEN THE FILE
    f = open('filename.txt','w')
    
    # WEBSITE URL
    url = "https://www.worldometers.info/coronavirus/#countries"
    
    # SCRAPING DATA
    f.write("NUMBER OF SELECTED COUNTRIES: " + str(len(c)) + "\n\n")
    for i in c:
        url = "https://www.worldometers.info/coronavirus/country/" + i + "/"
        response = requests.get(url)
        html = response.text
        bs_html = BeautifulSoup(html,"html.parser")
        f.write(bs_html.title.text + "\n")
    
    #CLOSING THE FILE
    f.close()

# SCRAPING COVID DATA AND STORING IT IN FILENAME.TXT
def getAllCases(start, end):
    
    # OPEN THE FILE
    f = open('filename.txt','w')
    
    # WEBSITE URL
    url = "https://www.worldometers.info/coronavirus/#countries"
    
    # SCRAPING DATA
    response = requests.get(url)
    html = response.text
    bs_html = BeautifulSoup(html,"html.parser")
    f.write("OVERAL CASES: \n" + bs_html.title.text + "\n\n")
    f.write("NUMBER OF COUNTRIES: " + str(len(country_list)) + "\n\n")
    for i in country_list:
        url = "https://www.worldometers.info/coronavirus/country/" + i + "/"
        response = requests.get(url)
        html = response.text
        bs_html = BeautifulSoup(html,"html.parser")
        f.write(bs_html.title.text + "\n")
    
    #CLOSING THE FILE
    f.close()



# DEFINING VARIABLES AND ARRAYS
flag = 0
thread_count = 16
country_count = len(country_list)
thread_list = []

# WELCOME TO COVID TROOPER
print("----------------------------------")
print("WELCOME TO COVID TROOPER TWEET BOT")
print("----------------------------------")

# PRESS 'YES' TO CONTINUE
startExe = input("PRESS 'Y' TO CONTINUE (y/Y): ")
if startExe == 'y' or startExe == 'Y':

    # OPTION FOR SCRAPING
    print("----------------------------------")
    print("THESE ARE THE AVAILABLE OPTIONS:")
    print(" 1 - SCRAPE PREFERRED COUNTRIES COVID DATA")
    print(" 2 - SCRAPE ALL COUNTRIES COVID DATA ")
    option = int(input("ENTER YOUR OPTION (1/2) : "))

    # SCRAPE SELECTED COUNTRIES COVID DATA
    if(option == 1):
        flag = 1
        
        # GET INPUT OF COUNTRIES DATA REQUIRED
        c = []

        # ENTER THE COUNTRY NAME AND ENTER 'FINISH' TO SCRAPE THE COURIES DATA
        print("-------------------------------------------------------")
        print("ENTER THE COUNTRIES NAME ONE BY ONE IN SMALL CASES")
        print("FINALLY AFTER ENTERING COUNTRIES NAME, ENTER 'FINISH' TO SCRAPE DATA")
        while country != 'FINSIH':
            country = input()
            if country in country_list:
                c.append(country)
            elif country == 'FINISH':
                break
            else:
                print("PLEASE CHECK WHETHER THE SPECIFIED COUNTRY'S NAME IS CORRECT")
        
        print("-------------------------------")
        print("PROCESSING YOUR REQUEST")
        print("SCRAPING COVID DATA %.%.%.%\n")

        # STARTING TIME CALCULATION
        start_time = time.time()
        for i in range(thread_count):
            start = math.floor(i * country_count/thread_count)
            end = math.floor((i+1) * country_count/thread_count)
            thread_list.append(threading.Thread(target=getCases, args=(start, end,c)))
    
    # SCRAPE ALL COUNTRIES COVID DATA
    elif(option == 2):
        print("-------------------------------")
        print("PROCESSING YOUR REQUEST")
        print("SCRAPING COVID DATA %.%.%.%\n")
        flag = 1
        # STARTING TIME CALCULATION
        start_time = time.time()
        for i in range(thread_count):
            start = math.floor(i * country_count/thread_count)
            end = math.floor((i+1) * country_count/thread_count)
            thread_list.append(threading.Thread(target=getAllCases, args=(start, end)))

# STARTING THE THREAD AND ENDING THE THREAD
for thread in thread_list:  
    thread.start()

for thread in thread_list:
    thread.join()

# END TIME CALCULATION
end_time = time.time()

# SCRAPE SUCCESS RATE AND TIME TAKEN TO SCRAPE DATA
if flag == 1:
    print("--------------------------------------------")
    print("YOUR DATA HAS BEEN SCRAPED SUCCESSFULLY")
    print('TIME TAKEN TO SCRAPE DATA : '+ str(end_time - start_time) + 'SEC')
    print("--------------------------------------------")
else:
    print("--------------------------------------------")
    print("YOUR DATA HAS NOT BEEN SCRAPED SUCCESSFULLY")
    print('TIME TAKEN TO SCRAPE DATA : '+ str(end_time - start_time) + 'SEC')
    print("--------------------------------------------")
    exit(0)

# PYTTSX3 - TEXT TO SPEECH CONVERSION LIBRARY
def talk():
    f = open('filename.txt','r')
    s = f.read()
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice',voices[1].id)
    engine.say(s)
    engine.runAndWait()
    
# AUDIO
a_input = input("Do you want to hear the audio? press(y/n): ")
if(a_input == 'y'):
    talk()


# TWITTER
t_input = input("Do you want to tweet about it? press(y/n): ")

# FUNCTION TO UPLOAD THE TEXT AND IMAGE FILE
def upload_media(text, filename):
        media = api.media_upload(filename)
        api.update_status(text, media_ids = [media.media_id_string])

if(t_input == 'y'):
    f = open('filename.txt','r')
    s = f.read()
    upload_media(s,'cc.jpg')

elif(t_input == 'n'):
    print('END OF APPLICATION')

else:
    print('WRONG INPUT')
    print('END OF APPLICATION')