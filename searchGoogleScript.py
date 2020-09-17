import googlesearch

def searchGoogle(searchPhrase,hits,file):
    hitArray =[]
    file_name = file
    try:
        from googlesearch import search
    except ImportError:
        print("No module named 'google' found")
        # What Phrase to Search
    query = str(searchPhrase)
    print("Starting Google Search For:",query)
    for hit in search(query, tld="dk", num=10, stop=hits, pause=2):
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

                if ".com" in entry:
                    entry = str(entry.split(".com")[0])
                    entry = entry+".com/"
                    contactus = entry+"contactus"
                    file.writelines(entry+"\n")
                    file.writelines(contactus+"\n")
                elif ".dk" in entry:
                    entry = str(entry.split(".dk")[0])
                    entry = entry + ".dk/"
                    contactus = entry + "kontakt"
                    file.writelines(entry + "\n")
                    file.writelines(contactus + "\n")

            file.close()
    else:
        print("No Results")
    print("Search Complete! Results: ",len(hitArray))

#Test It!
#searchGoogle("CRM",25,"links.txt")
