import ReadingSource
import mergeSort
import binarySearch

def Simulation(path): #simulate the better way based on the dataset by path
    globalTime = 0 #Counts each minute
    waitingTime = 0 #delay between time of incoming Job and finishing time
    maxTime = 0 #saves the max value of waitingTime
    src = [] #the whole data set as a list of lists [Jobences time, processing time]
    avgTime = 0 #Average of waitingTime
    avgTimeSum = 0 #Sum of waitingTime (for average)
    avgTimeCount = 0 #Count of finished Jobs (for average)
    possibleJobs = [] #all jobs with a lower start time than the current time

    src=ReadingSource.readingData(path)

    while(len(src) > 0): #repeat until no job is left

        possibleJobs = []
        for i in range(len(src)):
            srcVal = src[i]
            if srcVal[1] <= globalTime:
                var = src[i].copy()
                possibleJobs.append(var)
            else:
                break

        for i in possibleJobs: #makes the waiting time in relation to the start time
            i.insert(3, i[2] / i[1])



        if len(possibleJobs) != 0:
            mergeSort.mergeSort(possibleJobs, 3)
            currentJob = possibleJobs[0].copy()

        else: #skips time to the next job start time
            currentJob = src[0]
            globalTime = currentJob[1]
            while not((globalTime / 60) % 24 < 17 and (globalTime / 60) % 24 > 9): #skips time to the next morining
                globalTime += 1



        while(currentJob[2] > 0): #simulate the time of work

            if (((globalTime / 60) + 7) % 24 == 0): #if the working time per day is over




                globalTime += 960 #skip the nights

            else:
                currentJob[2] -= 1 #working time one less
                globalTime += 1 #global time one more


        src, maxTime, avgTimeSum, avgTimeCount = auswertung(src, globalTime, currentJob, maxTime, avgTimeSum, avgTimeCount)


    avgTime = avgTimeSum/avgTimeCount
    return "better", path, maxTime, avgTime

def auswertung(src, globalTime, currentJob, maxTime, avgTimeSum, avgTimeCount): #calculate all relevant values #?do it back to orgin if longer days is not implemented
    waitingTime = globalTime - currentJob[1]
    if waitingTime > maxTime:
        maxTime = waitingTime
    avgTimeSum += waitingTime
    avgTimeCount += 1
    src.pop(binarySearch.binary_search(src, 0, len(src), currentJob))
    return src, maxTime, avgTimeSum, avgTimeCount
