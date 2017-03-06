DEBUG = True

def index(i, j):
    return "i"+str(i)+"j"+str(j)


def isFitting(list1, list2):
    
    if DEBUG:
        print(len(list1), len(list2), len(set(list1 + list2)), len(set(list1 + list2)) == len(list1 + list2))
    if len(set(list1 + list2)) != len(list1 + list2):
        return False
    else:
        return True
    
    

n, m = [int(x) for x in input('').strip().split()]

plus1 = 0
plus2 = 0
gFlag1 = False
gFlag2 = False
plusMap = {}


for i in range(n):
    line = input('').strip()
    matrix.append(line)
    # check if there is a 'G' at all!
    found = line.find('G')
    
    if found != -1:
        if not gFlag1:      
            gFlag1 = True
            plus1 = 1
            plusMap[index(i, found)] = 1
        elif not gFlag2:
            gFlag2 = True
            plus2 = 1
            plusMap[index(i, found)] = 1

if not gFlag1:
    print(0)
elif gFlag1 and not gFlag2:
    print(0)
else:            
    # Core logic
    for i in range(1, n-1):
        for j in range(1, m-1):
            if DEBUG:
                if i == 2 and j == 4:
                    print()
                if i == 6 and j == 3:
                    print()
            if matrix[i][j] == 'G':
                # examine top
                tCount = 0
                ti = i - 1
                while ti >= 0:
                    if matrix[ti][j] == 'G':
                        tCount += 1
                        ti -= 1
                    else: break
                
                # examine bottom
                bCount = 0
                bi = i + 1
                while bi < n:
                    if matrix[bi][j] == 'G':
                        bCount += 1
                        bi += 1
                    else: break                
                        
                # examine left
                lCount = 0
                lj = j - 1
                while lj >= 0:
                    if matrix[i][lj] == 'G': 
                        lCount += 1
                        lj -= 1
                    else: break
                
                # examine right
                rCount = 0
                rj = j + 1
                while rj < m:
                    if matrix[i][rj] == 'G': 
                        rCount += 1
                        rj += 1
                    else: break
                
                newPlus = min(tCount, bCount, lCount, rCount)
                
                while newPlus > 0: # consider inner pluses as well!
                    tempList = []
                    tempList.append(index(i, j))
                    for k in range(1, newPlus+1):
                        tempList.append(index(i-k, j))
                        tempList.append(index(i+k, j))
                        tempList.append(index(i, j-k))
                        tempList.append(index(i, j+k))
                            
                    total = newPlus*4 + 1 # tblr + middle
                    
                    #if DEBUG:
                    #    print(tempList)
                    plusMap[",".join(tempList)] = total
                    newPlus -= 1

                                           
    keyList = list(plusMap.keys())
    for i in range(0, len(keyList)-1):
        tempList1 = keyList[i].split(",")
        for j in range(i+1, len(keyList)):
            tempList2 = keyList[j].split(",")
            
            if (len(tempList1)*len(tempList2)) > (plus1*plus2) and isFitting(tempList1, tempList2):
                plus1 = len(tempList1)
                plus2 = len(tempList2)
                
    if DEBUG:
        print(plus1, plus2)
    print(plus1 * plus2)
         
            
            