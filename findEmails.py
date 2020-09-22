from bs4 import BeautifulSoup
import requests
import re
import html.parser
import gc
import time
from tqdm import tqdm
def findEmails(emailfile,link_file):
    #File to save Email
    file_name = emailfile
    #Shit solution
    array = []
    # The Final Email
    realemail = []
    # Link That Dont Work:
    brokenLinks = []
    # Link Array
    linkArray = []
    # Progress Counter
    progress_counter = 0
    # Reading Links From Linkfile
    with open(link_file, "r") as file:
        for lines in file.readlines():
            linkArray.append(lines)
        file.close()
    # Call the Website
    for link in linkArray:
        try:
            response = requests.get(link)
            # Read the Html
            soup = BeautifulSoup(response.text,"html.parser")
            # Find all the links in the Html
            links = soup.find_all("a")
            # Progress Update
            percent_done = round((progress_counter / len(linkArray)) * 100)
            progress_counter += 1
            print("Links Searched:", progress_counter, "/", len(linkArray),",",percent_done,"%")
            for link in links:
                array.append(link.get("href"))
            for i in (e for e in array if e is not None):
                for char in i:
                    if char == "@":
                        realemail.append(i)
        except:
            progress_counter +=1
            print("Can't Access:", link)
            # Add to Brokenlinsk so we can add them to filter.
            brokenLinks.append(link)
    # Make sure that duplicates are removed. We make the array in to a dictionary with the entries as Keys. Keys Can't be Duplicated
    single_Emails = list(dict.fromkeys(realemail))
    with open(file_name, "a") as file:
        for mail in single_Emails:
            mail = mail[7:]
            file.writelines(mail + "\n")
        file.close()
    # Add Broken Links to Filter.
    with open("filterWords.txt","a") as file:
        for link in brokenLinks:
            link = link[12:]
            file.writelines(link)
        file.close()
    print("Broken Links Found and Added To Filter:",len(brokenLinks))
