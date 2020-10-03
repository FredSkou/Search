import googlesearch
import Decorators.Write_Log
import Decorators.Estimate

#import google
#Google Has To Be Imported and then removed again



def searchGoogle(searchPhrase,hits,linkfile):
    # Where to save the Links.
    file_name = linkfile
    # Filter words from the Filter.txt file
    filterArray = []
    # Link List to remove Duplicates:
    linkArray = []
    # Add Terms We Dont Want From filterWords.txt
    with open("Filters/filterWords.txt", "r") as filter:
        for lines in filter.readlines():
            filterArray.append(lines.strip("\n"))
        filter.close()
    with open("Filters/brokenLinks.txt", "r") as broken:
        for lines in broken.readlines():
            filterArray.append(lines.strip("\n"))
        broken.close()
    try:
        from googlesearch import search
    except ImportError:
        print("No module named 'google' found")
    # What Phrase to Search
    query = str(searchPhrase)
    print("Starting Google Search For:",query)
    # Our Search function.
    hits = search(query, tld="dk", num=10, stop=hits, pause=2)
    # We filter the hits and only add the ones that dont include filtered words.
    hitArray = [s for s in hits if not any(xs in s for xs in filterArray)]
    if hitArray:
        for entry in (e for e in hitArray if e is not None):
            if ".com" in entry:
                entry = str(entry.split(".com")[0])
                entry_short = entry + ".com/"
                contactus = entry_short + "contactus"
                contact = entry_short + "contact"
                contact_us = entry_short + "contact-us"
                contact_Html = contactus + ".html"
                aboutus = entry_short + "/about/contactus.html"
                linkArray.append(entry_short + "\n")
                linkArray.append(contactus + "\n")
                linkArray.append(contact + "\n")
                linkArray.append(contact_us + "\n")
                linkArray.append(contact_Html + "\n")
                linkArray.append(aboutus)
            elif ".dk" in entry:
                entry = str(entry.split(".dk")[0])
                entry_short = entry + ".dk/"
                kontakt = entry_short + "kontakt"
                kontaktOs = entry_short + "kontaktos"
                linkArray.append(entry_short + "\n")
                linkArray.append(kontakt + "\n")
                linkArray.append(kontaktOs + "\n")
            else:
                linkArray.append(entry)
        with open(file_name,"w") as file:
            linkArraySorted = list(dict.fromkeys(linkArray))
            print(f"Writing to File {file_name}")
            for link in linkArraySorted:
                file.writelines(link)

    else:
        print("No Results")
    try:
        print("Search Complete! Results: ",len(linkArraySorted))
        Decorators.Write_Log.saveResults(len(linkArraySorted),"Logs/Results.txt")
        #Decorators.Estimate.estimate(len(linkArraySorted))
    except:
        pass





