import googlesearch

def searchGoogle(searchPhrase,hits):
    hitArray =[]
    file_name = "link.txt"
    try:
        from googlesearch import search
    except ImportError:
        print("No module named 'google' found")
        # What Phrase to Search
    query = str(searchPhrase)
    print("Starting Google Search For:",query)
    for hit in search(query, tld="com", num=10, stop=hits, pause=2):
        # Dont Include these Websites
        if "wikipedia" in hit:
            continue
        if "news" in hit:
            continue
        if "view" in hit:
            continue
        if "search" in hit:
            continue
        else:
            hitArray.append(hit)
    if hitArray:
        with open(file_name,"w") as file:
            print(f"Writing to File {file_name}")
            for entry in hitArray:
                entry = str(entry.split("com")[0])
                entry = entry+"com/"
                contactus = entry+"contactus"
                file.writelines(entry+"\n")
                file.writelines(contactus+"\n")
            file.close()
    else:
        print("No Results")
    print("Search Complete! Results: ",len(hitArray))

#Test It!
searchGoogle("CRM",25)
