from DataReadingSudoku import *
from DataEvaluationSudoku import *

#VarierendeVariablen
class Sudoku:

    def __init__(self, isOriginal):
        self.field = readSudoku('Beispieldaten\Sudoku0.txt', isOriginal) #[9][9] Array
        self.numberfrequency = readNumberFrequency(self.field) #1d Array
        self.parallels = readParallels(self.field) #2d Array [[R],[C]]

    def createReconstructionData(self):
        self.numberReassignment = [0,0,0,0,0,0,0,0,0]
        self.rowReassignment = createEmptyLineReassignment()
        self.columnReassignment = createEmptyLineReassignment()
        
        isRotated = False
        

sudokuOriginal = Sudoku(True)
sudokuCopy = Sudoku(False)
sudokuCopy.createReconstructionData()


#CodiCode
#print(isComparable(sudokuOriginal.numberfrequency, sudokuCopy.numberfrequency, sudokuOriginal.parallels, sudokuCopy.parallels))
getAllocatedData(sudokuCopy.numberReassignment, sudokuCopy.rowReassignment, sudokuCopy.columnReassignment)

