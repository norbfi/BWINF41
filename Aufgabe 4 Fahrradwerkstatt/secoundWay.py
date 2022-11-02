import ReadingSource
import mergeSort
import binarySearch
import currentJobSimulation

def Simulation(path):
    globalTime = 0 #Counts each minute
    waitingTime = 0 #delay between time of incoming Job and finishing time
    maxTime = 0 #saves the max value of waitingTime
    src = [] #the whole data set as a list of lists [Jobences time, processing time]
    avgTime = 0 #Average of waitingTime
    avgTimeSum = 0 #Sum of waitingTime (for average)
    avgTimeCount = 0 #Count of finished Jobs (for average)
    days = 0 #Count of nights in the simulation

    delayTime = 0 #

    src=ReadingSource.readingData(path)

    while(len(src) > 0):
        possibleJobs = []

        for i in range(len(src)):
            srcVal = src[i]
            if srcVal[1] <= globalTime:
                possibleJobs.append(src[i])
            else:
                break
        if len(possibleJobs) != 0:
            mergeSort.mergeSort(possibleJobs)
            currentJob = possibleJobs[0]
        else:
            currentJob = src[0]
            delayTime = delayTime + (currentJob[1] - globalTime)
            globalTime = currentJob[1]



        maxTime, avgTimeSum, avgTimeCount, days, globalTime = currentJobSimulation.simulation(currentJob, maxTime, avgTimeSum, avgTimeCount, days, globalTime)

        src.pop(binarySearch.binary_search(src, 0, len(src), currentJob))
    days = days + ((delayTime  / 60) /24)
    avgTime = avgTimeSum/avgTimeCount
    return "secound", path, maxTime, avgTime, days, delayTime





    print(f"|----------|--------------------|--------------------|--------------------|\n|   path   |  Max waitingTime   |  Avg waitingTime   |        days        |\n|----------|--------------------|--------------------|--------------------|\n|{path: ^10}|{maxTime: ^20}|{avgTimeSum/avgTimeCount: ^20}|{days: ^20}|\n|----------|--------------------|--------------------|--------------------|")

"""
path = input("Which data do you want to use?: ")
Simulation(path)
"""