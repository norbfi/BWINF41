from DataReadingSudoku import *
from DataEvaluationSudoku import *
import NumPy as np

#VarierendeVariablen
class Sudoku:

    def __init__(self, isOriginal):
        self.field = readSudoku('Aufgabe 3 Sudokopie\Beispieldaten\Sudoku0.txt', isOriginal) #[9][9] Array
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
#sudokuCopy.numberReassignment = allocateNumbers(sudokuOriginal.numberfrequency, sudokuCopy.numberfrequency)

print(sudokuOriginal.field.index(6))





def allocate():
    
    for row in range(9):
        for collumn in range(9):
            
            if sudokuOriginal.field[row][collumn] == 0:
                continue

            if sudokuCopy.numberReassignment[sudokuCopy.field[row][collumn]] != 0:
                print(x)
            #wurdeDieZahlSchonBestimmt? -> Eingrenzen
            #wurdeDieZeileSchonBestimmt? -> Eingrenzen 
            #wurdeDieSpalteSchonBestimt? -> Eingrenzen

            #WennRestDerEingrenzung = 0  -> keine Kopie
            #WennRestDerEingrenzung = 1 -> ZeileZusweisen, SpalteZuweisen, ZahlZuweisen
            #WennRestDerEingrenzung < 1 -> Dann in der Reihe alle Zahlen anschauen:
                                                                                   #bereitsZahlBestimmt?; Häufigkeit
                                                                                   #DerEinfachheit: ZeilenParallele, SpaltenParallele
                                                                                   #Fund Blockweise ()



    reassignedLines = [[False,0,0,0],[False,0,0,0],[False,0,0,0]]

#print(allocate())