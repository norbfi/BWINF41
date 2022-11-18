def simulation(arrows, jumpingWay1, jumpingWay2, attampt1, attampt2):
    while True:
        print("sim start...")
        if jumpingWay1[-1] == jumpingWay2[-1]:
            return 'solved', jumpingWay1, jumpingWay2

        elif len(jumpingWay1) >= 6:
            return 'unsolved'

        else:

            possibleWays1 = arrows[jumpingWay1[-1] -1].copy()
            possibleWays2 = arrows[jumpingWay2[-1] -1].copy()
            del possibleWays1[0]
            del possibleWays2[0]

            if attampt1 < len(possibleWays1) and attampt2 < len(possibleWays2):
                del jumpingWay1[-1]
                del jumpingWay2[-1]
                attampt2 += 1
                jumpingWay1.append(possibleWays1[attampt1])
                jumpingWay2.append(possibleWays2[attampt2])
                #simulation(arrows, jumpingWay1, jumpingWay2, attampt1, attampt2 + 1)
            elif attampt1 < len(possibleWays1) and attampt2 >= len(possibleWays2):
                print("1")
                #simulation(arrows, jumpingWay1, jumpingWay2, attampt1, attampt2 + 1)
            elif attampt1 >= len(possibleWays1) and attampt2 < len(possibleWays2):
                del jumpingWay1[-1]
                del jumpingWay2[-1]
                attampt1 += 1
                attampt2 = 0
                jumpingWay1.append(possibleWays1[attampt1])
                jumpingWay2.append(possibleWays2[attampt2])
            else:
                print("2")




    '''doesn't work
    else:
        if attampt2 >= len(arrows[jumpingWay2[-1] - 1]):
            if attampt1 >= len(arrows[jumpingWay1[-1] - 1]):
                print("dubbol if")
                del jumpingWay1[-1]
                del jumpingWay2[-1]
                return simulation(arrows, jumpingWay1, jumpingWay2, 1, )
            else:
                print (f"{jumpingWay1} {jumpingWay2}")
                return simulation(arrows, jumpingWay1, jumpingWay2, attampt1 + 1, 1)
        else:
            if attampt1 >= len(arrows[jumpingWay1[-1] - 1]):
                del jumpingWay1[-1]
                del jumpingWay2[-1]
                return simulation(arrows, jumpingWay1, jumpingWay2, len(arrows[jumpingWay1[-1] - 1]), 1)
            else:
                print (f"{jumpingWay1} {jumpingWay2}")
                nextFields = arrows[jumpingWay1[-1] - 1]
                jumpingWay1.append(nextFields[attampt1])
                nextFields = arrows[jumpingWay2[-1] - 1]
                jumpingWay2.append(nextFields[attampt2])
                return simulation(arrows, jumpingWay1, jumpingWay2, attampt1, attampt2 + 1)'''


    '''Works...
    else:
        for i in arrows[jumpingWay1[-1] - 1]:
            #print(arrows[jumpingWay1[-1] - 1])
            if i != (jumpingWay1[-1]):
                for j in arrows[jumpingWay2[-1] - 1]:
                    if j != jumpingWay2[-1]:
                        #print(arrows[jumpingWay2[-1] - 1])
                        jumpingWay1.append(i)
                        jumpingWay2.append(j)
                        print (f"{jumpingWay1} {jumpingWay2}")
                        simulation(arrows, jumpingWay1, jumpingWay2)
                        del jumpingWay1[-1]
                        del jumpingWay2[-1]'''