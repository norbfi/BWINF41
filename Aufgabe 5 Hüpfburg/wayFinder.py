def simulation(arrows, jumpingWay1, jumpingWay2):
    print('sim starting...')
    if jumpingWay1[-1] == jumpingWay2[-1]:
        return 'solved', jumpingWay1, jumpingWay2

    elif len(jumpingWay1) >= 4:
        return 'unsolved'

    else:
        for i in arrows[jumpingWay1[-1] - 1]:
            #print(arrows[jumpingWay1[-1] - 1])
            if i != (jumpingWay1[-1]):
                for j in arrows[jumpingWay2[-1] - 1]:
                    if j != jumpingWay2[-1]:
                        #print(arrows[jumpingWay2[-1] - 1])
                        jumpingWay1.append(i)
                        jumpingWay2.append(j)
                        print (jumpingWay1)
                        print (jumpingWay2)
                        return simulation(arrows, jumpingWay1, jumpingWay2)
                        #del jumpingWay1[-1]
                        #del jumpingWay2[-1]