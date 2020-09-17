import searchGoogleScript
import findEmails

def runScrips(file_name, emailFile):
    #New Emails
    email_counter = 0

    searchGoogleScript.searchGoogle("CRM",20,file_name)

    try:
        with open(emailFile,"r") as emailfile:
            lines = emailfile.readlines()
            email_counter =len(lines)
            emailfile.close()
    except:
        print("No file")


    try:
        print("Getting Emails From Links!")
        with open(file_name) as file:
            for lines in file.readlines():
                findEmails.findEmails(lines,emailFile)
            file.close()
        print("Emails Found and Saved To File: ",emailFile)
        with open(emailFile,"r") as file:
            lines = file.readlines()
            print("New Emails Found:",len(lines)-email_counter)
            email_counter =len(lines)
            file.close()
        print("Total Email:", email_counter)
    except:
        print("Cant Access File")


runScrips("GoogleLinks,txt","Email.txt")