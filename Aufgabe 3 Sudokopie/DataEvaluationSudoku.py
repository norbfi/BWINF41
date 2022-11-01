

def isComparable(orgNF, copyNF, orgPar, copyPar):


    if orgNF.sort() != copyNF.sort():
        return "not your mom"

    orgParRow = orgPar[0][:]
    orgParCollumn = orgPar[1][:]
    copyParRow = copyPar[0][:]
    copyParCollumn = copyPar[1][:]
    
    return None #sollte am Anfang ausgeführt werden: vergleich von simplen werten



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

    

