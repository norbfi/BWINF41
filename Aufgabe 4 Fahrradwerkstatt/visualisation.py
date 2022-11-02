import betterWay
import firstWay
import secoundWay


def visualisation(paths=[]):
    firstAllTime = []
    firstAllTimeMax = 0
    firstAllTimeAvgSum = 0
    firstAllTimeAvgCount = 0
    secoundAllTimeMax = 0
    secoundAllTimeAvgSum = 0
    secoundAllTimeAvgCount = 0
    firstAllTime = []
    betterAllTimeMax = 0
    betterAllTimeAvgSum = 0
    betterAllTimeAvgCount = 0
    print(f"+----------+----------+--------------------+--------------------+--------------------+")
    print(f"| methode  |   path   |  Max waitingTime   |  Avg waitingTime   |        days        |")
    for i in range(len(paths)):
        methode, path, maxTime, avgTime, days, delayTime = firstWay.Simulation(paths[i])
        print(f"+----------+----------+--------------------+--------------------+--------------------+")
        print(f"|{methode: ^10}|{path: ^10}|{maxTime: ^20}|{round(avgTime, 2): ^20}|{round(days, 2): ^20}|")

        firstAllTime = []
        firstAllTimeAvgSum += avgTime
        firstAllTimeAvgCount += 1
        if firstAllTimeMax < maxTime:
            firstAllTimeMax = maxTime


        methode, path, maxTime, avgTime, days, delayTime = secoundWay.Simulation(paths[i])
        print(f"+----------+----------+--------------------+--------------------+--------------------+")
        print(f"|{methode: ^10}|{path: ^10}|{maxTime: ^20}|{round(avgTime, 2): ^20}|{round(days, 2): ^20}|")

        secoundAllTimeAvgSum += avgTime
        secoundAllTimeAvgCount += 1
        if secoundAllTimeMax < maxTime:
            secoundAllTimeMax = maxTime


        methode, path, maxTime, avgTime, days, delayTime = betterWay.Simulation(paths[i])
        print(f"+----------+----------+--------------------+--------------------+--------------------+")
        print(f"|{methode: ^10}|{path: ^10}|{maxTime: ^20}|{round(avgTime, 2): ^20}|{round(days, 2): ^20}|")

        betterAllTimeAvgSum += avgTime
        betterAllTimeAvgCount += 1
        if betterAllTimeMax < maxTime:
            betterAllTimeMax = maxTime

    firstAllTimeAvg = firstAllTimeAvgSum / firstAllTimeAvgCount
    secoundAllTimeAvg = secoundAllTimeAvgSum / secoundAllTimeAvgCount
    betterAllTimeAvg = betterAllTimeAvgSum / betterAllTimeAvgCount

    return [["first", '{0:.2f}'.format(firstAllTimeMax), '{0:.2f}'.format(firstAllTimeAvg)], ["secound", '{0:.2f}'.format(secoundAllTimeMax), '{0:.2f}'.format(secoundAllTimeAvg)], ["better", '{0:.2f}'.format(betterAllTimeMax), '{0:.2f}'.format(betterAllTimeAvg)]]

