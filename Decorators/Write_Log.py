from datetime import *



def writeLog(tags, results, time):
    dateString = str(datetime.today())
    try:
        with open("Logs/Log.txt","a") as file:
            file.writelines(f"{dateString} - A Search was Made For: {tags}. Total Result: {results}. Time Elapsed: {time}"+"\n")
    except:
        print("Cant Access Log File!")