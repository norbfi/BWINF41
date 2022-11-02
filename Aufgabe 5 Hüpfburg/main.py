import wayFinder
import ReadingSource
path = ["00", "01", "02", "03", "04"]

arrows = ReadingSource.readingData(path[0])

jumpingWay1 = [1]
jumpingWay2 = [2]
print(arrows)
print(wayFinder.simulation(arrows, jumpingWay1, jumpingWay2))
