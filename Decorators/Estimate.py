
def estimate(amount_of_tags,amount_of_hits):

    total_time = []
    total_links = []

    adjustedhits = amount_of_tags * amount_of_hits

    with open("Logs/Time.txt","r") as file:
        for line in file.readlines():
            total_time.append(float(line.strip("\n")))
    file.close()

    with open("Logs/Results.txt","r") as file:
        for line in file.readlines():
            total_links.append(int(line.strip("\n")))
    file.close()
    try:
        average_time = (sum(total_time)/len(total_time))
        average_results = (sum(total_links)/len(total_links))
        averagetimeperlink = round(average_time/average_results,1)
        estimate =  round(averagetimeperlink*adjustedhits,1)*amount_of_tags
        print("Estimated Time Per Link:", averagetimeperlink,"Total time Estimated Time:",estimate)
    except:
        print("No Estimate Available!")



