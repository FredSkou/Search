from datetime import *

def writeLog(data,logfile):
    dateString = str(datetime.now().replace(second=0, microsecond=0))

    with open(logfile, "a") as file:
        line = dateString,": ",str(data),"\n"
        file.writelines(line)
    file.close()


def saveResults(data, logfile):

    with open(logfile, "a") as file:
        line = str(round(data)), "\n"
        file.writelines(line)
    file.close()

def writeSearchLoPart1(data,logfile):
    dateString = str(datetime.now().replace(second=0, microsecond=0))

    with open(logfile, "a") as file:
        line =dateString," - Search For Tags:",str(data),"\n"
        file.writelines(line)
    file.close()

def writeSearchLogPart2(data,logfile):
    dateString = str(datetime.now().replace(second=0, microsecond=0))
    with open(logfile, "a") as file:
        line = dateString," - ",str(data)," Results Where Found For Search On Tag(s): "
        file.writelines(line)
    file.close()