import betterWay
import firstWay
import secoundWay
import time

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


''' Result #1
+----------+----------+--------------------+--------------------+--------------------+
| methode  |   path   |  Max waitingTime   |  Avg waitingTime   |        days        |
+----------+----------+--------------------+--------------------+--------------------+
|  first   |    00    |       68771        |      32753.5       |       403.13       |
+----------+----------+--------------------+--------------------+--------------------+
| secound  |    00    |       188734       |      16981.28      |       403.13       |
+----------+----------+--------------------+--------------------+--------------------+
|  better  |    00    |       18874        |      4283.01       |       363.07       |
+----------+----------+--------------------+--------------------+--------------------+
|  first   |    01    |       128321       |      63535.65      |       421.53       |
+----------+----------+--------------------+--------------------+--------------------+
| secound  |    01    |       433563       |      11883.94      |       421.53       |
+----------+----------+--------------------+--------------------+--------------------+
|  better  |    01    |        5438        |       529.26       |       350.55       |
+----------+----------+--------------------+--------------------+--------------------+
|  first   |    02    |       110973       |      51194.49      |       382.35       |
+----------+----------+--------------------+--------------------+--------------------+
| secound  |    02    |       327087       |      14813.53      |       382.35       |
+----------+----------+--------------------+--------------------+--------------------+
|  better  |    02    |       18874        |      3727.57       |       358.25       |
+----------+----------+--------------------+--------------------+--------------------+
|  first   |    03    |       60821        |      30028.93      |       383.77       |
+----------+----------+--------------------+--------------------+--------------------+
| secound  |    03    |       382016       |      17242.83      |       383.77       |
+----------+----------+--------------------+--------------------+--------------------+
|  better  |    03    |        5381        |      1656.51       |       359.04       |
+----------+----------+--------------------+--------------------+--------------------+
|  first   |    04    |       167059       |      74427.52      |       407.28       |
+----------+----------+--------------------+--------------------+--------------------+
| secound  |    04    |       363155       |      42200.9       |       407.28       |
+----------+----------+--------------------+--------------------+--------------------+
|  better  |    04    |       11477        |      4779.71       |       366.08       |
+----------+----------+--------------------+--------------------+--------------------+
+ ######## + ######## + ################## + ################## + ################## +
'''
''' All Time Result
+----------+----------+--------------------+--------------------+--------------------+
| All Time |  first   |     167059.00      |      50388.02      |         --         | #- Worsed Average Time
+----------+----------+--------------------+--------------------+--------------------+
| All Time | secound  |     433563.00      |      20624.50      |         --         | #- Worsed Max Time
+----------+----------+--------------------+--------------------+--------------------+
| All Time |  better  |      18874.00      |      2995.21       |         --         | #+ Best Average Time & Best Max Time
+----------+----------+--------------------+--------------------+--------------------+
'''
'''
+----------+----------+--------------------+--------------------+
| All Time |  first   |     167060.00      |      50388.65      |
+----------+----------+--------------------+--------------------+
| All Time | secound  |     433563.00      |      20626.16      |
+----------+----------+--------------------+--------------------+
| All Time |  better  |      67430.00      |      7735.62       |
+----------+----------+--------------------+--------------------+
'''