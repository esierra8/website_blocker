#This is a website blocker, what it does is it goes to your conf files in your system
#   in this case in windows. You will have to schedule a task in the background that
#   will check the time and depending on the time (working hours) it will edit the file
#   and will add the specify websites in the list of links to the block websites. And
#   thanks to that you won't be able to access the website.

#Esteban Sierra
#07/12/17
#


import time
from datetime import datetime as dt

#Declaring global variables

#temp_path is used as a temporary path to test the file change
temp_path = 'hosts'
#real path for the file
host_path = r'C:\Windows\System32\drivers\etc\hosts'
redirect = '127.0.0.1'
#The list if links to block
website_links = ['www.facebook.com', 'www.tumblr.com', 'facebook.com', 'tumblr.com']

#Infinite loop
while True:
    #Checking for the date and time to see if I want to block the websites

    #If(RIGHT NOW (dt.now()) is between 8 am and 4 pm) Change the file
    if dt(dt.now.year, dt.now().month, dt.now().day, 8) < dt.now() < dt.now(dt.now().year, dt.now().month, dt.now().day, 16):
        print('Working hours...')
        with open(temp_path, 'r+') as file:
            content = file.read()
            for website in website_links:
                if website in content:
                    pass
                else:
                    file.write(redirect + ' ' + website + '\n')
    #Else rewrite every line of the document that does not contain the links.
    #In other words, rewrite without links to block.
    else:
        with open(temp_path, 'r+') as file:
            content = file.readline()
            file.seek(0)
            for line in content:
                #If there is no website link from the list of website links
                #in this line of document. Rewrite it, else don't.
                if not any(website in line for website in website_links):
                    file.write(line)
            file.truncate()
        print('Fun hours...')
    time.sleep(5)