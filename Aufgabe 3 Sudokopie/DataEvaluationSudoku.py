from os import system

def isNotACopy(error):

    print(f'\nThe sudoku is not a copy [{error}]')
    input()
    quit()

def isACopy(sudoku):
    print("\nThe sudoku is a copy from the original\n")
    
    if sudoku.isRotated == True:
        print("--The sudoku has been rotated--")

    outputStringNB = "Numberreassignment [copy -> original number]: "
    i = 0
    for number in sudoku.numberReassignment:
        if number != None:
            outputStringNB += f'[{i+1} -> {number+1}], '
        i+=1
    print(outputStringNB)

    outputStringRow = "Rowreassignment [copy -> original row]: "
    outputStringCol = "Columnreassignment [copy -> original column]: "
    for x in range(3):
        for y in range(3):
            if sudoku.rowReassignment[x][y] != None:
                outputStringRow += f'[{(x*3)+y+1} -> {sudoku.rowReassignment[x][y]+1}], '
            
            if sudoku.columnReassignment[x][y] != None:
                outputStringCol += f'[{(x*3)+y+1} -> {sudoku.columnReassignment[x][y]+1}], '

    print(outputStringRow)
    print(outputStringCol)
    print("\n-----------------------------------------------------------")
    input("Press enter to exit")
    quit()


def createIndividualNumbers(sudoku):
    
    singularityGrid = []

    for i in range(81):
        if int(sudoku.field[i]) == 0:
            singularityGrid.append(0)
            continue
        
        #Häufigkeit der Zahl * 1000
        frequencyValue = sudoku.numberfrequency[int(sudoku.field[i])-1] * 1000 
        
        #NumbersInBlock * 100 * (Sum of: numberFrequency of NumbersInBlock)
        count = 0
        sumOfNf = 0
        position = 0
        blockBeginn = (i//27)*27 + ((i%9)//3)*3 

        for row in range(3):
            for column in range(3):
                
                position = blockBeginn + column + row*9
                if int(sudoku.field[position]) == 0:
                    continue

                count += 1
                sumOfNf += sudoku.numberfrequency[int(sudoku.field[position])-1]

        blockValue = count * sumOfNf * 100

        #parallelsRow * 10 * (Sum of: numberFrequency(row))
        sumOfNf = 0
        row = (i//9)*9

        for column in range(9): 

            if int(sudoku.field[row+column]) == 0:
                    continue
            sumOfNf += sudoku.numberfrequency[int(sudoku.field[row+column])-1]

        parallelsRowValue = sudoku.parallels[0][i//9] * sumOfNf * 10

        #parallelsColumn * 1 * (Sum of: numberFrequency(col.))
        sumOfNf = 0
        column = (i%9)

        for row in range(9): 
            
            if int(sudoku.field[column + row*9]) == 0:
                continue
            sumOfNf += sudoku.numberfrequency[int(sudoku.field[column + row*9])-1]

        parallelsColumnValue = sudoku.parallels[1][i%9] * sumOfNf * 1
          
        value = frequencyValue + blockValue + parallelsRowValue + parallelsColumnValue
        singularityGrid.append(value)
    
    return singularityGrid