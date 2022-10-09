from DataReadingSudoku import readSudoku
from DataReadingSudoku import readNumberFrequency
from DataReadingSudoku import readParallels


sudokuOriginal = readSudoku('Aufgabe 3 Sudokopie\Beispieldaten\Sudoku0.txt', True)
sudokuCopy = readSudoku('Sudokopie\Beispieldaten\Sudoku0.txt', False)

print(sudokuOriginal, "\n \n" , sudokuCopy)

#dataReading
sudokuOrignalNF = readNumberFrequency(sudokuOriginal) #1d Array
sudokuCopyNF = readNumberFrequency(sudokuCopy) #1d Array

sudokuOrignalPar = [readParallels(sudokuOriginal)] #2d Array [R,C]
sudokuCopyPar = [readParallels(sudokuCopy)] #2d Array [R,C]






