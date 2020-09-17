from bs4 import BeautifulSoup
import requests
import re
import html.parser

def findEmails(url):
    #File to save Email
    file_name = "email_list.txt"
    #Shit solution
    array = []
    # The Final Email
    realemail = []
    # The site we want to Scrape
    website = url
    # Call the Website
    try:
        response = requests.get(website)
        # Read the Html
        soup = BeautifulSoup(response.text,"html.parser")
        # Find all the links in the Html
        links = soup.find_all("a")

        for link in links:
            array.append(link.get("href"))
        for i in (e for e in array if e is not None):
            for char in i:
                if char == "@":
                    realemail.append(i)
        with open(file_name,"a") as file:
            for mail in realemail:
                mail = mail[7:]
                file.writelines(mail+"\n")
            file.close()
    except:
        print("Cant Acess:", website)

def read():
    filename = "link.txt"
    with open(filename,"r") as file:
        print(f"Starting Email Search in {filename}!")
        lines = file.readlines()
        for line in lines:
            findEmails(line)
    print("Email Search Complete!")

read()
