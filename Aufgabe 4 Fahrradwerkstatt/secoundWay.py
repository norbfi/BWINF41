import ReadingSource
from mergeSort import mergeSort

def Simulation(path):
    globalTime = 0 #Counts each minute
    waitingTime = 0 #delay between time of incoming Job and finishing time
    maxTime = 0 #saves the max value of waitingTime
    src = [] #the whole data set as a list of lists [Jobences time, processing time]
    avgTime = 0 #Average of waitingTime
    avgTimeSum = 0 #Sum of waitingTime (for average)
    avgTimeCount = 0 #Count of finished Jobs (for average)
    days = 0 #Count of nights in the simulation

    src=ReadingSource.readingData(path)

    while(len(src) > 0):
        possibleJobs = []

        for i in range(len(src)):
            srcVal = src[i]
            if srcVal[2] <= globalTime:
                possibleJobs.append(src[i])
            else:
                break
        mergeSort(possibleJobs)
        currentJob = possibleJobs[0]

        #! Same like in First
        #? Maybe this should go in a own method
        while(currentJob[2] > 0):
            if (((globalTime / 60) + 7) % 24 == 0):


                globalTime += 960
                days += 1
            else:
                currentJob[2] -= 1
                globalTime += 1

        waitingTime = globalTime - currentJob[1]
        if waitingTime > maxTime:
            maxTime = waitingTime
        avgTimeSum += waitingTime

        avgTimeCount += 1

        #? Maybe this should go in a own method
        #! Same like in First

"""
path = input("Which data do you want to use?: ")
Simulation(path)
"""