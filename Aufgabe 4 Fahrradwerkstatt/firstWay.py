import ReadingSource



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

    #! Same like in First
    #? Maybe this should go in a own method
    for i in range(len(src)):
        currentJob = src[i]
        if(globalTime < currentJob[1]):
            globalTime=currentJob[1]
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
    #! Same like in Secound

    print(f"|----------|--------------------|--------------------|--------------------|\n|   path   |  Max waitingTime   |  Avg waitingTime   |        days        |\n|----------|--------------------|--------------------|--------------------|\n|{path: ^10}|{maxTime: ^20}|{avgTimeSum/avgTimeCount: ^20}|{days: ^20}|\n|----------|--------------------|--------------------|--------------------|")

"""
path = input("Which data do you want to use?: ")
Simulation(path)
"""
"""
Result:
    |----------|--------------------|--------------------|--------------------|
    |   path   |  Max waitingTime   |  Avg waitingTime   |        days        |
    |----------|--------------------|--------------------|--------------------|
    |    00    |       68771        |      32753.5       |        364         |
    |----------|--------------------|--------------------|--------------------|
    |    01    |       128321       | 63535.65274151436  |        357         |
    |----------|--------------------|--------------------|--------------------|
    |    02    |       110973       | 51194.48924731183  |        362         |
    |----------|--------------------|--------------------|--------------------|
    |    03    |       60821        | 30028.927272727273 |        363         |
    |----------|--------------------|--------------------|--------------------|
    |    04    |       167059       | 74427.52222222222  |        370         |
    |----------|--------------------|--------------------|--------------------|
"""