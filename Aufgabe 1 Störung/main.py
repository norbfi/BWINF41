results = []
s = []
index = 1
end = []


search = "Das _ mir _ _ _ vor"
#
def findword(results, search):
    index = 1

    #wörter in search
    s = search.split()

    #liste bilden
    for index in range(len(s)):
        if s[index] == results[index]:
            index += 1
        else:
            results.remove(index)

    

with open('Aufgabe 1 Störung/Alice_im_Wunderland.txt','r') as f:
    for line in f:
        f.readline()
        if " Das kommt" in line:
            results.append(line.split(" "))

    print(results)
    print(findword(results, search))