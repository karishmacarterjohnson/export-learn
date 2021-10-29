import mechanize
import http.cookiejar as cookielib
from bs4 import BeautifulSoup
import html2text

# Browser
br = mechanize.Browser()

# Cookie Jar
cj = cookielib.LWPCookieJar()
br.set_cookiejar(cj)

# Browser options
br.set_handle_equiv(True)
br.set_handle_gzip(True)
br.set_handle_redirect(True)
br.set_handle_referer(True)
br.set_handle_robots(False)
br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)

br.addheaders = [('User-agent', 'Chrome')]

# The site we will navigate into, handling it's session
print(br.open('https://auth.galvanize.com/sign_in').read())

# View available forms
for f in br.forms():
    print(f)

br.form= list(br.forms())[0] 
# Select the second (index one) form (the first form is a search query box)
#br.select_form('new_user')

# User credentials
br.form['user[email]'] = 'karishmacjohnson@gmail.com'
br.form['user[password]'] = '1080p@23.976fps'

# Login
br.submit()

print(br.open('https://learn-2.galvanize.com/cohorts/2836').read())


'''
from bs4 import BeautifulSoup
import requests

# Start the session
session = requests.Session()

# Create the payload
payload = {'user[email]':'karishmacjohnson@gmail.com', 
          'user[password]':'1080p@23.976fps'
         }
agent = {"User-Agent": 'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36'}
# Post the payload to the site to log in
s = session.post("https://auth.galvanize.com/sign_in", data=payload, headers = agent)

# Navigate to the next page and scrape the data
s = session.get('https://learn-2.galvanize.com/cohorts/2836', headers = agent)

soup = BeautifulSoup(s.content, 'html.parser')

print(soup)
'''