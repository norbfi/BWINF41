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
        for i in possibleJobs:
            i[2] = i[2] - i[1]
        if len(possibleJobs) != 0:
            mergeSort.mergeSort(possibleJobs)
            currentJob = possibleJobs[0]
        else:
            currentJob = src[0]
            delayTime = delayTime + (currentJob[1] - globalTime)
            globalTime = currentJob[1]



        while(currentJob[2] > 0):
            if (((globalTime / 60) + 7) % 24 == 0):
                
                if currentJob[2] < 60:
                    globalTime == globalTime + currentJob[2]
                    currentJob[2] = 0
                    src, maxTime, avgTimeSum, avgTimeCount = auswertung(src, globalTime, currentJob, maxTime, avgTimeSum, avgTimeCount)
                
                globalTime += 960
                days += 1
                
            else:
                currentJob[2] -= 1
                globalTime += 1

        '''waitingTime = globalTime - currentJob[1]
        if waitingTime > maxTime:
            maxTime = waitingTime
        avgTimeSum += waitingTime
        avgTimeCount += 1
        src.pop(binarySearch.binary_search(src, 0, len(src), currentJob))'''
        src, maxTime, avgTimeSum, avgTimeCount = auswertung(src, globalTime, currentJob, maxTime, avgTimeSum, avgTimeCount)


    days = days + ((delayTime  / 60) /24)
    avgTime = avgTimeSum/avgTimeCount
    return "better", path, maxTime, avgTime, days, delayTime

def auswertung(src, globalTime, currentJob, maxTime, avgTimeSum, avgTimeCount):
    waitingTime = globalTime - currentJob[1]
    if waitingTime > maxTime:
        maxTime = waitingTime
    avgTimeSum += waitingTime
    avgTimeCount += 1
    src.pop(binarySearch.binary_search(src, 0, len(src), currentJob))
    return src, maxTime, avgTimeSum, avgTimeCount
    