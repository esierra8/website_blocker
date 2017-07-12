import time
from datetime import datetime as dt

temp_path = 'hosts'
host_path = r'C:\Windows\System32\drivers\etc\hosts'
redirect = '127.0.0.1'
website_links = ['www.facebook.com', 'www.tumblr.com', 'facebook.com', 'tumblr.com']

while True:
    if dt(dt.now.year, dt.now().month, dt.now().day, 8) < dt.now() < dt.now(dt.now().year, dt.now().month, dt.now().day, 16):
        print('Working hours...')
        with open(temp_path, 'r+') as file:
            content = file.read()
            for website in website_links:
                if website in content:
                    pass
                else:
                    file.write(redirect + ' ' + website + '\n')
    else:
        with open(temp_path, 'r+') as file:
            content = file.readline()
            file.seek(0)
            for line in content:
                if not any(website in line for website in website_links):
                    file.write(line)
            file.truncate()
        print('Fun hours...')
    time.sleep(5)