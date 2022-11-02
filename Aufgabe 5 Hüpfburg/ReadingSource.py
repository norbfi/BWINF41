def readingData(path): #* path: string[Path of data to read] or int[00 - 04 -> Exampltask]
    #Exampltask 0
    if(path == '00'):
        with open('Aufgabe 5 Hüpfburg\Beispielaufgaben\Beispielaufgabe_00.txt') as f:
            lines = f.read().splitlines() #reads all lines into var lines

    #Exampltask 1
    elif(path == '01'):
        with open('Aufgabe 5 Hüpfburg\Beispielaufgaben\Beispielaufgabe_01.txt') as f:
            lines = f.read().splitlines()

    #Exampltask 2
    elif(path == '02'):
        with open('Aufgabe 5 Hüpfburg\Beispielaufgaben\Beispielaufgabe_02.txt') as f:
            lines = f.read().splitlines()

    #Exampltask 3
    elif(path == '03'):
        with open('Aufgabe 5 Hüpfburg\Beispielaufgaben\Beispielaufgabe_03.txt') as f:
            lines = f.read().splitlines()

    #Exampltask 4
    elif(path == '04'):
        with open('Aufgabe 5 Hüpfburg\Beispielaufgaben\Beispielaufgabe_04.txt') as f:
            lines = f.read().splitlines()

    #Normal path
    else:
        with open(path) as f:
            lines = f.read().splitlines()

    data = []
    for i in lines: #splits values at space
        data.append(i.split())
    x = 0
    for i in data: #makes all values integers
        i[0] = int(i[0])
        i[1] = int(i[1])

    indexRow = data[0]
    arrwos = []

    for i in range(indexRow[0]):
        arrwos.append([int(i) + 1])
    del data[0]
    for i in data:

        arrwos[i[0] - 1].append(i[1])

    return arrwos
