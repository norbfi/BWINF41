
def readSudoku(source, original):

    sudoku = []
    #textdokument öffnen, auslesen
    textfile = open(source, encoding='utf-8-sig') 
    
    textfileAsList = []
    for line in textfile:
        textfileAsList.append(line)
    
    #das orignale Sodoku geht von Zeile 0 bis 8
    if original:
        offset = 0
    else:
        offset = 10

    for row in range(0+offset,9+offset):
        (c0, c1, c2, c3, c4, c5, c6, c7, c8) = textfileAsList[row].split()
        sudoku.append([c0, c1, c2, c3, c4, c5, c6, c7, c8])
    
    return sudoku



def readNumberFrequency(sudoku):
    
    numberFrequency = [0,0,0,0,0,0,0,0,0,0,0]
    for row in range(9):
        for collumn in range(9):
            numberFrequency[int(sudoku[row][collumn])] += 1 
    numberFrequency.sort()
    return numberFrequency    


def readParallels(sudoku):
    
    parallelsRow = [0,0,0,0,0,0,0,0,0]
    for row in range(9):
        for collumn in range(9):
            if int(sudoku[row][collumn]) != 0:
                parallelsRow[row] += 1
       
    parallelsCollumn = [0,0,0,0,0,0,0,0,0]
    for collumn in range(9):
        for row in range(9):
            if int(sudoku[row][collumn]) != 0:
                parallelsCollumn[collumn] += 1
    
    return [parallelsRow,parallelsCollumn]    
