import searchGoogleScript
import findEmails

def runScrips(keyword,numberOfLinks,link_file, emailFile):
    # Start Seaching On Google
    searchGoogleScript.searchGoogle(keyword,numberOfLinks,link_file)
    # Count the Starting Amount of Emails
    # New Emails
    email_counter = 0
    try:
        with open(emailFile,"r") as emailfile:
            lines = emailfile.readlines()
            email_counter =len(lines)
            emailfile.close()
    except:
        print("Creating New File!")
    # Run findEmails per Link Found
    try:
        print("Getting Emails From Links!")
        findEmails.findEmails(emailFile,link_file)
        print("Emails Found and Saved To File:",emailFile)
        with open(emailFile,"r") as file:
            lines = file.readlines()
            print("New Emails Found:",len(lines)-email_counter)
            email_counter =len(lines)
            file.close()
        print("Total Emails:", email_counter)
    except:
        print("Cant Access File")

runScrips("CRM",100,"GoogleLinks.txt","CRM.txt")