
def DataReading(source):
    d=[]
    with open(source) as f:
        for line in f:
            (entrance, duration) = line.split()
            d.append([entrance, duration])
    return d