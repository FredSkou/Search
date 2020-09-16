import googlesearch

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
        elif "news" in hit:
            continue
        else:
            hitArray.append(hit)
    for entry in hitArray:
        print(entry)

searchGoogle("CRM",15)