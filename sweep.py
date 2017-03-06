
# Globals
intersectingLines = {}
lineList = []
aboveMap = {}
belowMap = {}


class Line(object):
    
    def __init__(self, x1, x2, y1, y2):
        self.x1 = x1
        self.x2 = x2
        self.y1 = y1
        self.y2 = y2


class Point(object):
    
    LEFT = 0
    RIGHT = 1
    
    def __init__(self, x=0, y=0, lineIndex=0, pointType=LEFT):
        self.x = x
        self.y = y
        self.pointType = pointType
        self.lineIndex = lineIndex
        
    def isLeft(self):
        if self.pointType is self.LEFT:
            return True
        else:
            return False
    
    def isRight(self):
        return not self.isLeft()


def getPointList(lineList):
    
    pointList = []
    
    for i, line in enumerate(lineList):
        pointList.append(Point(line.x1, line.y1, i, Point.LEFT))
        pointList.append(Point(line.x2, line.y2, i, Point.RIGHT))
        
    return pointList


def getSortedPoints(pointList):
    
    """
    Sort the endpoints of the segments in S from left to right,
    breaking ties by putting left endpoints before right endpoints
    and breaking further ties by putting points with lower
    y-coordinates first
    """
    pointList.sort(key = lambda p:(p.x, p.pointType, p.y))
    print(pointList)
    
    return pointList


def isLinePairAdded(line1, line2):
    if (line1 in intersectingLines.keys() and intersectingLines[line1] == line2)\
    or (line2 in intersectingLines.keys() and intersectingLines[line2] == line1):
        return True
    else:
        return False


def updateIntersectingLines(currentLineList):
    
    if len(currentLineList) > 1:
        for index in range(len(currentLineList) - 1):
            line1 = currentLineList[index]
            line2 = currentLineList[index+1]
            if not isLinePairAdded(line1, line2):
                intersectingLines[line1] = line2
    else:
        pass


def populateLineOrientation(pointList):
    
    for point in pointList:
        aboveMap[point] = []
        belowMap[point] = []
        for line in lineList:
            if point.lineIndex == line:
                continue
            else:
                v1 = Point(point.x-line.x1, point.y-line.y1)
                v2 = Point(point.x-line.x2, point.y-line.y2)
                crossProduct = v1.x*v2.y - v1.y*v2.x
                if crossProduct > 0:
                    aboveMap[point].append(line)
                elif crossProduct < 0:
                    belowMap[point].append(line)
    
    aboveMap.sort(key = lambda l:l.y)
    print(aboveMap, belowMap)            


def getLineAbove(current, yCoordinate):
    
    for line in lineList:
        if line == current:
            continue
        else:
            if line.x2 > current.x1 and line.x1 >
            (line.)

def getLineBelow(line, yCoordinate):
    pass

    
def lineSweep(pointList):
    
    currentLines = []
    
    for point in pointList:
        updateIntersectingLines(currentLines)
        
        if point.isLeft():
            currentLines.append(point.lineIndex)
        else:
            currentLines.remove(point.lineIndex)

