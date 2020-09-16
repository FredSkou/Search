from bs4 import BeautifulSoup
import requests
import re
import html.parser

def findEmails(url):

    #Shit solution
    array = []
    # The Final Email
    realemail = []
    # The site we want to Scrape
    website = url
    # Call the Website
    response = requests.get(website)
    # Read the Html
    soup = BeautifulSoup(response.text,"html.parser")
    # Find all the links in the Html
    links = soup.find_all("a")
    for link in links:
        array.append(link.get("href"))
    for item in array:
        if item is None:
            array.remove(item)
    for i in array:
        for char in i:
            if char == "@":
                realemail.append(i)
    for mail in realemail:
        print(mail)


#findEmails("https://www.dr.dk/")
#findEmails("http://adcommodo.com/x/startside/")
#findEmails("https://dinero.dk/om-os/kontakt/")
findEmails("https://periskop.dk/kontakt/")
