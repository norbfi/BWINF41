import betterWay
import firstWay
import secoundWay

paths = [] #path of dataset

firstAllTimeMax = 0 #var to save the max time of each way
secoundAllTimeMax = 0
betterAllTimeMax = 0

firstAllTimeAvgSum = 0 #Sum of all waiting times to get the average time
secoundAllTimeAvgSum = 0
betterAllTimeAvgCount = 0

firstAllTimeAvgCount = 0 #Count of all waiting times to get the average time
secoundAllTimeAvgCount = 0
betterAllTimeAvgSum = 0

allTimeStats = [] #two dimensional list of time statistics for each way


#User input
pathInput = input(" Which data do you want to use?\n(empty Input -> all five examples; give path or number of example task [00 to 05])\n ")

paths.append(pathInput)

#if empty input: run each example task
if paths == [""]:
    paths = ["00", "01", "02", "03", "04"]

#set up table header
print(f"+----------+----------+--------------------+--------------------+")
print(f"| methode  |   path   |  Max waitingTime   |  Avg waitingTime   |")

#Simulation of each data set on all three ways
for i in range(len(paths)):

    #Sim first Way
    methode, path, maxTime, avgTime, = firstWay.Simulation(paths[i])
    print(f"+----------+----------+--------------------+--------------------+")
    print(f"|{methode: ^10}|{path: ^10}|{maxTime: ^20}|{round(avgTime, 2): ^20}|")

    firstAllTimeAvgSum += avgTime
    firstAllTimeAvgCount += 1
    if firstAllTimeMax < maxTime:
        firstAllTimeMax = maxTime


    #sim secound Way
    methode, path, maxTime, avgTime, = secoundWay.Simulation(paths[i])
    print(f"+----------+----------+--------------------+--------------------+")
    print(f"|{methode: ^10}|{path: ^10}|{maxTime: ^20}|{round(avgTime, 2): ^20}|")

    secoundAllTimeAvgSum += avgTime
    secoundAllTimeAvgCount += 1
    if secoundAllTimeMax < maxTime:
        secoundAllTimeMax = maxTime


    #sim better Way
    methode, path, maxTime, avgTime, = betterWay.Simulation(paths[i])
    print(f"+----------+----------+--------------------+--------------------+")
    print(f"|{methode: ^10}|{path: ^10}|{maxTime: ^20}|{round(avgTime, 2): ^20}|")

    betterAllTimeAvgSum += avgTime
    betterAllTimeAvgCount += 1
    if betterAllTimeMax < maxTime:
        betterAllTimeMax = maxTime



if len(paths) > 1: #show average if there are multiple datasets
    firstAllTimeAvg = firstAllTimeAvgSum / firstAllTimeAvgCount
    secoundAllTimeAvg = secoundAllTimeAvgSum / secoundAllTimeAvgCount
    betterAllTimeAvg = betterAllTimeAvgSum / betterAllTimeAvgCount


    allTimeStats = [["first", '{0:.2f}'.format(firstAllTimeMax), '{0:.2f}'.format(firstAllTimeAvg)], ["secound", '{0:.2f}'.format(secoundAllTimeMax), '{0:.2f}'.format(secoundAllTimeAvg)], ["better", '{0:.2f}'.format(betterAllTimeMax), '{0:.2f}'.format(betterAllTimeAvg)]]

    print(f"+----------+----------+--------------------+--------------------+")
    print(f"+ ######## + ######## + ################## + ################## +")

    for i in allTimeStats: #for each way one revision

        print(f"+----------+----------+--------------------+--------------------+")
        print(f"| All Time |{i[0]: ^10}|{i[1]: ^20}|{i[2]: ^20}|")

print(f"+----------+----------+--------------------+--------------------+")

end=input("press any key to close...")

