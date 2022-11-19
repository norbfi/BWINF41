 
def readSudoku(source, isOriginal, rotate):

    sudoku = []
    for i in range(81):
        sudoku.append(None)
    #textdokument �ffnen, auslesen
    textfile = open(source, encoding='utf-8-sig') 
    
    textfileAsList = []
    for line in textfile:
        textfileAsList.append(line)
    
    #das orignale Sodoku geht von Zeile 0 bis 8
    if isOriginal:
        offset = 0
    else:
        offset = 10

    if rotate == False:
        for row in range(0+offset,9+offset):
            (sudoku[(row-offset)*9+0], sudoku[(row-offset)*9+1],sudoku[(row-offset)*9+2], sudoku[(row-offset)*9+3], sudoku[(row-offset)*9+4], sudoku[(row-offset)*9+5], sudoku[(row-offset)*9+6], sudoku[(row-offset)*9+7], sudoku[(row-offset)*9+8]) = textfileAsList[row].split()

        return sudoku


    else:
        for collumn in range(0+offset,9+offset):
            (sudoku[(collumn-offset)+0], sudoku[(collumn-offset)+9], sudoku[(collumn-offset)+18], sudoku[(collumn-offset)+27], sudoku[(collumn-offset)+36], sudoku[(collumn-offset)+45], sudoku[(collumn-offset)+54], sudoku[(collumn-offset)+63], sudoku[(collumn-offset)+72]) = textfileAsList[collumn].split()
        
        return sudoku





def readNumberFrequency(sudoku):
    
    numberFrequency = [0,0,0,0,0,0,0,0,0,0]
    for i in range(81):
            numberFrequency[int(sudoku[i])] += 1 

    return numberFrequency[1:]   


def readParallels(sudoku):
    
    parallelsRow = [0,0,0,0,0,0,0,0,0]
    parallelsCollumn = [0,0,0,0,0,0,0,0,0]
    for i in range(81):    
   
        if int(sudoku[i]) != 0:
            parallelsRow[(i)//9] += 1
            parallelsCollumn[(i)%9] += 1
    
    return parallelsRow, parallelsCollumn



def createEmptyLineReassignment():
    
    return [[0,0,0],[0,0,0],[0,0,0]]