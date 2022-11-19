def simulation(currentJob, maxTime, avgTimeSum, avgTimeCount, globalTime): #simulates the process of one single job

    while(currentJob[2] > 0):
        if (((globalTime / 60)) % 24 == 17): #if the working time of this day is over
            globalTime += 960 #skip the night

        else:
            currentJob[2] -= 1 #working time one less
            globalTime += 1 #global time one more

    #all values get calculate
    waitingTime = globalTime - currentJob[1]
    if waitingTime > maxTime:
        maxTime = waitingTime
    avgTimeSum += waitingTime
    avgTimeCount += 1

    return maxTime, avgTimeSum, avgTimeCount, globalTime