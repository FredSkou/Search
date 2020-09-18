import searchGoogleScript
import findEmails

def runScrips(keyword,numberOfLinks,file_name, emailFile):
    # Start Seaching On Google
    searchGoogleScript.searchGoogle(keyword,numberOfLinks,file_name)
    # Count the Starting Amount of Emails
    # New Emails
    email_counter = 0
    try:
        with open(emailFile,"r") as emailfile:
            lines = emailfile.readlines()
            email_counter =len(lines)
            emailfile.close()
    except:
        print("No file")
    # Run findEmails per Link Found
    try:
        print("Getting Emails From Links!")
        with open(file_name) as file:
            for lines in file.readlines():
                findEmails.findEmails(lines,emailFile)
            file.close()
        print("Emails Found and Saved To File:",emailFile)
        with open(emailFile,"r") as file:
            lines = file.readlines()
            print("New Emails Found:",len(lines)-email_counter)
            email_counter =len(lines)
            file.close()
        print("Total Emails:", email_counter)
    except:
        print("Cant Access File")


runScrips("Immanuel Storm Lokzinsky",15,"GoogleLinks,txt","Emails.txt")