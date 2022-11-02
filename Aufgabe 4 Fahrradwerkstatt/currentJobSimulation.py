def simulation(currentJob, maxTime, avgTimeSum, avgTimeCount, days, globalTime):

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

    return maxTime, avgTimeSum, avgTimeCount, days, globalTime