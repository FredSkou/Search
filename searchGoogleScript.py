import googlesearch
# import google - Has To Be Imported and then removed again
def searchGoogle(searchPhrase,hits,file):
    hitArray =[]
    file_name = file
    filterArray = []
    # Add Terms We Dont Want From filterWords.txt
    with open("filterWords.txt","r") as filter:
        for lines in filter.readlines():
            filterArray.append(lines.strip("\n"))
        filter.close()
    try:
        from googlesearch import search
    except ImportError:
        print("No module named 'google' found")
        # What Phrase to Search
    query = str(searchPhrase)
    print("Starting Google Search For:",query)
    for hit in search(query, tld="dk", num=10, stop=hits, pause=2):
        # Dont Include these Websites
        for word in filterArray:
            if word in hit:
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
