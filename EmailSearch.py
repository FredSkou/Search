import re
import requests
from urllib.parse import urlsplit
from collections import deque
from bs4 import BeautifulSoup
import pandas as pd

def getEmail(url):
    # What Website to search
    original_url = url
    # Unsraped urls
    unscraped = deque([original_url])
    # After we scrape them
    scraped = set()
    # The emails we find
    emails = set()

    while len(unscraped):
        # We move the URL from Unscraped to Scraped after we scrape it.
        url = unscraped.popleft()
        scraped.add(url)
        # We split the URL
        parts = urlsplit(url)
        # We find out what is the main URL and what are "/" parts.
        base_url = "{0.scheme}://{0.netloc}".format(parts)
        if '/' in parts.path:
            path = url[:url.rfind('/') + 1]
        else:
            path = url
        # We send a Get Request to the URL
        print("Crawling URL %s" % url)
        try:
            response = requests.get(url)
        except (requests.exceptions.MissingSchema, requests.exceptions.ConnectionError):
            # Skips a website with and Error
            continue
        # We find the Email we need using what ever parameters we choose
        new_emails = set(re.findall(r"[a-z0-9\.\-+_]+@[a-z0-9\.\-+_]+\.com", response.text, re.I))
        # We then add them to the email List
        emails.update(new_emails)
        # We use BeautifulSoup to make the HTML readable.
        soup = BeautifulSoup(response.text, 'lxml')
        # We search for all links in the HTML.
        for anchor in soup.find_all("a"):
            if "href" in anchor.attrs:
                link = anchor.attrs["href"]
            else:
                link = ''

                if link.startswith('/'):
                    link = base_url + link

                elif not link.startswith('http'):
                    link = path + link
                # Things we know arent Emiils
                if not link.endswith(".gz"):
                    if not link in unscraped and not link in scraped:
                        unscraped.append(link)

    #df = pd.DataFrame(emails, columns=["Email"])
    #df.to_csv('email.csv', index=False)

    print(emails)


getEmail("https://tpfrb.dk/")