
def DataReading(source, original):
    sudoku = []
    #textdokument öffnen, auslesen
    textfile = open(source, encoding='utf-8-sig') 
    
    textfileAsList = []
    for line in textfile:
        textfileAsList.append(line)
    
    #das orignale Sodoku geht von Zeile 0 bis 8
    if original:
        i = 0
    else:
        i = 10

    for row in range(0+i,9+i):
        (c0, c1, c2, c3, c4, c5, c6, c7, c8) = textfileAsList[row].split()
        sudoku.append([c0, c1, c2, c3, c4, c5, c6, c7, c8])

    return sudoku

