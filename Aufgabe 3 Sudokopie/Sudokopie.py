from DataReadingSudoku import *
from DataEvaluationSudoku import *

#VarierendeVariablen
class Sudoku:

    def __init__(self, isOriginal, rotate):
        self.field = readSudoku('Aufgabe 3 Sudokopie\Beispieldaten\Sudoku0.txt', isOriginal, rotate) #[81] Array
        self.numberfrequency = readNumberFrequency(self.field) #1d Array, warning: number = index -1
        self.parallels = readParallels(self.field) #2d Array [[R],[C]]


    def createReconstructionData(self):
        self.numberReassignment = [None,None,None,None,None,None,None,None,None] #index + 1 = copyNumber; value = orgNumber
        self.rowReassignment = createEmptyLineReassignment()
        self.columnReassignment = createEmptyLineReassignment()
        
        self.isRotated = False

    def createSingularityGrid(self):
        self.singularityGrid = createIndividualNumbers(self)
     

sudokuOriginal = Sudoku(True, False)
sudokuCopy = Sudoku(False, False)
sudokuCopy.createReconstructionData()

sudokuOriginal.createSingularityGrid()
sudokuCopy.createSingularityGrid()

sgGridCopyOrg = sudokuOriginal.singularityGrid.copy()
sgGridCopyCopy = sudokuCopy.singularityGrid.copy()
sgGridCopyOrg.sort()
sgGridCopyCopy.sort()


if sgGridCopyOrg == sgGridCopyCopy:
    print("singularityPass")

#else rotate
else:
    sudokuCopy = Sudoku(False, True)
    sudokuCopy.createReconstructionData()
    sudokuCopy.createSingularityGrid()
    sudokuCopy.isRotated = True 

    sgGridCopyCopy = sudokuCopy.singularityGrid.copy()
    sgGridCopyCopy.sort()

    if sgGridCopyOrg != sgGridCopyCopy:
        isNotACopy("mismatching singularities")

while 1 == 1:
    
    for i in range(81):
        if sudokuCopy.singularityGrid[i] == 0:
            continue

        if sudokuCopy.singularityGrid.count(sudokuCopy.singularityGrid[i]) != 1:
            #print("multiple")
            continue #hier ist es moeglich weitere Daten zu verwerten


        #numberreassignment
        orgIndex = sudokuOriginal.singularityGrid.index(sudokuCopy.singularityGrid[i])
        if sudokuCopy.numberReassignment[int(sudokuCopy.field[i])-1] != None and int(sudokuCopy.numberReassignment[int(sudokuCopy.field[i])-1]) != int(sudokuOriginal.field[orgIndex])-1:
            isNotACopy("mismatching numberreassignment")

        sudokuCopy.numberReassignment[int(sudokuCopy.field[i])-1] = int(sudokuOriginal.field[orgIndex])-1
        #copyIndexNumber = OrgNumber
        
        #rowreassignment
        if sudokuCopy.rowReassignment[(i//9)//3][(i//9)%3] != None and sudokuCopy.rowReassignment[(i//9)//3][(i//9)%3] != orgIndex//9:
            isNotACopy("missmatching rowreassignment")

        sudokuCopy.rowReassignment[(i//9)//3][(i//9)%3] = orgIndex//9

        #columnreassignment
        if sudokuCopy.columnReassignment[(i%9)//3][(i%9)%3] != None and sudokuCopy.columnReassignment[(i%9)//3][(i%9)%3] != orgIndex%9:
            isNotACopy("missmatching columnreassginment")
        
        sudokuCopy.columnReassignment[(i%9)//3][(i%9)%3] = orgIndex%9
    
    #Lines auﬂerhalb des Trios
    for x in range(3):
        avgRow = None
        avgColumn = None
        for y in range(3):
            #row
            if sudokuCopy.rowReassignment[x][y] == None and int(sudokuCopy.rowReassignment[x][:].count(None)) == 1:
                
                blockCopy = sudokuCopy.rowReassignment[x][:].copy()
                blockCopy.remove(None)
                blockCopy.sort()
                if blockCopy[0]%3 == 0 and blockCopy[1]%3 == 1:
                    sudokuCopy.rowReassignment[x][y] = (blockCopy[0]//3)*3+2
                if blockCopy[0]%3 == 1 and blockCopy[1]%3 == 2:
                    sudokuCopy.rowReassignment[x][y] == (blockCopy[0]//3)*3+0
                if blockCopy[0]%3 == 0 and blockCopy[1]%3 == 2:
                    sudokuCopy.rowReassignment[x][y] == (blockCopy[0]//3)*3+1
                continue

            if avgRow == None:
                avgRow = int(sudokuCopy.rowReassignment[x][y])//3
                continue
            if avgRow != int(sudokuCopy.rowReassignment[x][y])//3:
                isNotACopy("missmatching rows in Blocks")

            #column
            if sudokuCopy.columnReassignment[x][y] == None and int(sudokuCopy.columnReassignment[x][:].count(None)) == 1:
                
                blockCopy = sudokuCopy.columnReassignment[x][:].copy()
                blockCopy.remove(None)
                blockCopy.sort()
                if blockCopy[0]%3 == 0 and blockCopy[1]%3 == 1:
                    sudokuCopy.columnReassignment[x][y] = (blockCopy[0]//3)*3+2
                if blockCopy[0]%3 == 1 and blockCopy[1]%3 == 2:
                    sudokuCopy.columnReassignment[x][y] == (blockCopy[0]//3)*3+0
                if blockCopy[0]%3 == 0 and blockCopy[1]%3 == 2:
                    sudokuCopy.columnReassignment[x][y] == (blockCopy[0]//3)*3+1
                continue

            if avgColumn == None:
                avgColumn = int(sudokuCopy.columnReassignment[x][y])//3
                continue
            if avgColumn != int(sudokuCopy.columnReassignment[x][y])//3:
                isNotACopy("missmatching columns in Blocks")

    #letzte Werte fuellen
    if sudokuCopy.numberReassignment.count(None) == 1:
        indexEmpty = sudokuCopy.numberReassignment.inex(None)
        sum = 0
        for number in sudokuCopy.numberREassignment(9):
            if number != None:
                sum += number
        sudokuCopy.numberReassignment[indexEmpty] = 36 - sum 

    break

isACopy(sudokuCopy)