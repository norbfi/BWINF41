import ReadingSource
import mergeSort
import binarySearch
import currentJobSimulation

def Simulation(path):
    globalTime = 0 #Counts each minute
    maxTime = 0 #saves the max value of waitingTime
    src = [] #the whole data set as a list of lists [Jobences time, processing time]
    avgTime = 0 #Average of waitingTime
    avgTimeSum = 0 #Sum of waitingTime (for average)
    avgTimeCount = 0 #Count of finished Jobs (for average)
    possibleJobs = [] #all jobs available


    src=ReadingSource.readingData(path)

    while(len(src) > 0): #until not job is left
        possibleJobs = [] #resets all possible jobs

        for i in range(len(src)): #adds all possible jobs to list
            srcVal = src[i]
            if srcVal[1] <= globalTime:
                possibleJobs.append(src[i])

        if len(possibleJobs) != 0: #selects the job
            mergeSort.mergeSort(possibleJobs, 2)
            currentJob = possibleJobs[0]
        else:
            currentJob = src[0] #skip time to next possible job
            globalTime = currentJob[1]
            while not((globalTime / 60) % 24 < 17 and (globalTime / 60) % 24 > 9): #skips time to the next morining
                globalTime += 1



        maxTime, avgTimeSum, avgTimeCount, globalTime = currentJobSimulation.simulation(currentJob, maxTime, avgTimeSum, avgTimeCount, globalTime)

        src.pop(binarySearch.binary_search(src, 0, len(src), currentJob))
    avgTime = avgTimeSum/avgTimeCount
    return "secound", path, maxTime, avgTime
