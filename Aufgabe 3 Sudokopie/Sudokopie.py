from DataReadingSudoku import readSudoku
from DataReadingSudoku import readNumberFrequency
from DataReadingSudoku import readParallels
from DataEvaluationSudoku import isComparable


class Sudoku:

    def __init__(self, isOrginal):
        self.field = readSudoku('Aufgabe 3 Sudokopie\Beispieldaten\Sudoku0.txt', isOrginal) #[9][9] Array
        self.numberfrequency = readNumberFrequency(self.field) #1d Array
        self.parralels = readParallels(self.field) #2d Array [[R],[C]]


sudokuOriginal = Sudoku(True)
sudokuCopy = Sudoku(False)

print(sudokuOriginal.numberfrequency)


