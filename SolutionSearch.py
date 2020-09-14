import urllib.request

import requests
import googlesearch
import urllib3
import urllib
import re
import soupsieve
from bs4 import BeautifulSoup
import re
import requests
from urllib.parse import urlsplit
from collections import deque
from bs4 import BeautifulSoup
import pandas as pd


def searchGoogle(searchPhrase,hits):
    hitArray =[]
    try:
        from googlesearch import search
    except ImportError:
        print("No module named 'google' found")

        # What Phrase to Search
    query = str(searchPhrase)
    for hit in search(query, tld="com", num=10, stop=hits, pause=2):
        # Dont Include these Websites
        if "wikipedia" in hit:
            continue
        elif "businessnews" in hit:
            continue
        else:
            hitArray.append(hit)
    for entry in hitArray:
        print(entry)





#searchGoogle("CRM",15)

