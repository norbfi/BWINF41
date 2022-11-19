def allocateNumbers(orgNF, copyNF):

    reassignedNumbers=[0,0,0,0,0,0,0,0,0]

    for number in range (0,max(orgNF)):
        if orgNF.count(number) != 1:
            continue
        if copyNF.count(number) != 1:
            continue

        orgIndex = orgNF.index(number)
        copyIndex = copyNF.index(number)
        reassignedNumbers[orgIndex] = copyIndex

    return reassignedNumbers

   

def createIndividualNumber(sudoku):
    
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
            for collumn in range(3):
                
                position = blockBeginn + collumn + row*9
                if int(sudoku.field[position]) == 0:
                    continue

                count += 1
                sumOfNf += sudoku.numberfrequency[int(sudoku.field[position])-1]

        blockValue = count * sumOfNf * 100

        #parallelsRow * 10 * (Sum of: numberFrequency(row))
        sumOfNf = 0
        row = (i//9)*9

        for collumn in range(9): 

            if int(sudoku.field[row+collumn]) == 0:
                    continue
            sumOfNf += sudoku.numberfrequency[int(sudoku.field[row+collumn])-1]

        parallelsRowValue = sudoku.parallels[0][i//9] * sumOfNf * 10

        #parallelsCollumn * 1 * (Sum of: numberFrequency(col.))
        sumOfNf = 0
        collumn = (i%9)

        for row in range(9): 
            
            if int(sudoku.field[collumn + row*9]) == 0:
                continue
            sumOfNf += sudoku.numberfrequency[int(sudoku.field[collumn + row*9])-1]

        parallelsCollumnValue = sudoku.parallels[1][i%9] * sumOfNf * 1
        
        value = frequencyValue + blockValue + parallelsRowValue + parallelsCollumnValue
        singularityGrid.append(value)

    return singularityGrid