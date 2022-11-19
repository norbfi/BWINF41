from DataReadingSudoku import *
from DataEvaluationSudoku import *

#VarierendeVariablen
class Sudoku:

    def __init__(self, isOriginal, rotate):
        self.field = readSudoku('Aufgabe 3 Sudokopie\Beispieldaten\Sudoku0.txt', isOriginal, rotate) #[81] Array
        self.numberfrequency = readNumberFrequency(self.field) #1d Array, warning: number = index -1
        self.parallels = readParallels(self.field) #2d Array [[R],[C]]


    def createReconstructionData(self):
        self.numberReassignment = [0,0,0,0,0,0,0,0,0] #index + 1 = copyNumber; value = orgNumber
        self.rowReassignment = createEmptyLineReassignment()
        self.columnReassignment = createEmptyLineReassignment()
        
        self.isRotated = False

    def createSingularityGrid(self):
        self.singularityGrid = createIndividualNumber(self)
        
        self.emptySingularityGrid = []
        for i in range(81):
            self.emptySingularityGrid.append(0)
     

sudokuOriginal = Sudoku(True, False)
sudokuCopy = Sudoku(False, False)
sudokuCopy.createReconstructionData()
sudokuCopy.numberReassignment = allocateNumbers(sudokuOriginal.numberfrequency, sudokuCopy.numberfrequency)

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
    sudokuCopy.numberReassignment = allocateNumbers(sudokuOriginal.numberfrequency, sudokuCopy.numberfrequency)
    sudokuCopy.createSingularityGrid()
    sudokuCopy.isRotated == True 

    sgGridCopyCopy = sudokuCopy.singularityGrid.copy()
    sgGridCopyCopy.sort()

    if sgGridCopyOrg != sgGridCopyCopy:
        print("singularityFail")
        quit()

    print("isRotated")


while 1 == 1:
    
    for i in range(81):
        if sudokuCopy.singularityGrid[i] == 0:
            continue

        if sudokuCopy.singularityGrid.count(sudokuCopy.singularityGrid[i]) != 1:
            print("multiple")
            continue #mb notation des Index?


        #numberreassignment
        orgIndex = sudokuOriginal.singularityGrid.index(sudokuCopy.singularityGrid[i])
        if int(sudokuCopy.numberReassignment[int(sudokuCopy.field[i])-1]) != 0 and int(sudokuCopy.numberReassignment[int(sudokuCopy.field[i])-1]) != int(sudokuOriginal.field[orgIndex])-1:
            print("nbReassign problem")
            quit()

        sudokuCopy.numberReassignment[int(sudokuCopy.field[i])-1] = int(sudokuOriginal.field[orgIndex])-1
        #copyIndexNumber = OrgNumber
        
        #rowreassignment
        if sudokuCopy.rowReassignment[(i//9)//3][(i//9)%3] != 0 and sudokuCopy.rowReassignment[(i//9)//3][(i//9)%3] != orgIndex//9:
            print("rowReassign problem")
            quit()

        sudokuCopy.rowReassignment[(i//9)//3][(i//9)%3] = orgIndex//9

        #columnreassignment
        if sudokuCopy.columnReassignment[(i%9)//3][(i%9)%3] != 0 and sudokuCopy.columnReassignment[(i%9)//3][(i%9)%3] != orgIndex%9:
            print("collumnReassign problem")
            quit()
        
        sudokuCopy.columnReassignment[(i%9)//3][(i%9)%3] = orgIndex%9
    
    #try: Zahl bennenen, Row, collumn

    
    print("Ist ne Copy")
    quit()
