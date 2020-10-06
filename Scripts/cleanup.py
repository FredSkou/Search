

# The Absulute Path, We Can Most Likely Set this to what we need when we use it in our other projects
projectPath = "C:/Users/Bruger/Desktop/PySearch/"
timepath = projectPath+"Logs/Time.txt"
resultspath = projectPath+"Logs/Results.txt"

def cleanLogs():

    print("Cleaning...")
    with open(timepath ,"r") as file:
        try:
            lines = [int(lines) for lines in file.readlines()]
        except:
            pass
    file.close()
    with open(resultspath,"r") as file:
        try:
            resultlines = [int(lines) for lines  in file.readlines()]
        except:
            pass
    try:
        if len(lines) > 100:
            print("Time.txt is:",len(lines),"lines long. Starting Cleaning")
            average_time = round(sum(lines)/len(lines))
            average_results = round(sum(resultlines)/len(resultlines))
            rewriteTime(average_time)
            rewriteResults(average_results)
        else:
            print("No Cleaning Needed")
    except:
        print("No Files To clean")

def rewriteTime(average_time):
    with open(timepath,"w") as file:
        line = str(average_time)+"\n"
        file.write(line)
        print("Cleaning of Time.txt is Done: ",average_time,"is the Average Time.")
    file.close()

def rewriteResults(average_results):
    with open(resultspath,"w") as file:
        line = str(average_results)+"\n"
        file.write(line)
        print("Cleaning of Results.txt is Done:",average_results," is the Average Results.")
    file.close()

