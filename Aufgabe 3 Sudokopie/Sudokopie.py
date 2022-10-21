from DataReadingSudoku import readSudoku
from DataReadingSudoku import readNumberFrequency
from DataReadingSudoku import readParallels
from DataReadingSudoku import createEmptyLineReassignment
from DataEvaluationSudoku import isComparable

#VarierendeVariablen
class Sudoku:

    def __init__(self, isOrginal):
        self.field = readSudoku('Aufgabe 3 Sudokopie\Beispieldaten\Sudoku0.txt', isOrginal) #[9][9] Array
        self.numberfrequency = readNumberFrequency(self.field) #1d Array
        self.parralels = readParallels(self.field) #2d Array [[R],[C]]

    def createReconstructionData(self):
        self.numberReassignment = [0,0,0,0,0,0,0,0,0]
        self.rowReassignment = createEmptyLineReassignment()
        self.collumnReassignemnt = createEmptyLineReassignment()
        
        isRotated = False
        

sudokuOriginal = Sudoku(True)
sudokuCopy = Sudoku(False)
sudokuCopy.createReconstructionData(sudokuCopy)



#CodiCode
isComparable(sudokuOriginal.numberfrequency, sudokuCopy.numberfrequency, sudokuOriginal.parralels, sudokuCopy.parralels)


