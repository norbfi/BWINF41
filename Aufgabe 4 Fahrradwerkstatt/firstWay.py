import ReadingSource
import currentJobSimulation


def Simulation(path):
    globalTime = 0 #Counts each minute
    maxTime = 0 #saves the max value of waitingTime
    src = [] #the whole data set as a list of lists [Jobences time, processing time]
    avgTime = 0 #Average of waitingTime
    avgTimeSum = 0 #Sum of waitingTime (for average)
    avgTimeCount = 0 #Count of finished Jobs (for average)



    src = ReadingSource.readingData(path)

    for i in range(len(src)): #for each job in src
        currentJob = src[i]
        if(globalTime < currentJob[1]): #if there is no job available

            globalTime = currentJob[1] #skip time

            while not((globalTime / 60) % 24 < 17 and (globalTime / 60) % 24 > 9): #skips time to the next morining
                globalTime += 1


        maxTime, avgTimeSum, avgTimeCount, globalTime = currentJobSimulation.simulation(currentJob, maxTime, avgTimeSum, avgTimeCount, globalTime)


    avgTime = avgTimeSum/avgTimeCount
    return "first", path, maxTime, avgTime
