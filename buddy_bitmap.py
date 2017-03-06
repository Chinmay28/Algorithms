
header = [1,2,3,4,5,6,7,8,9,10,11,12]
bitmap = [0,0,1,1,0,1,1,1,1,1,0,1]


def set_bit(offset, length):
    global bitmap

    for i in range(offset, offset+length):
        if bitmap[i] == 0:
            bitmap[i] = 1
            rearrange_map(i)
    

def clear_bit(offset, length):
    global bitmap

    for i in range(offset, offset+length):
        if bitmap[i] == 1:
            bitmap[i] = 0
            rearrange_map(i)
    

def rearrange_map(i=len(bitmap)-1):
    global bitmap
        
    child1 = i*2+1
    child2 = i*2+2
    
    if child1 < len(bitmap) and child2 < len(bitmap):
        if bitmap[child1] == 1 and bitmap[child2] == 1:
            bitmap[i] = 1
        else:
            bitmap[i] = 0
            
    elif child1 < len(bitmap):
        if bitmap[child1] == 1:
            bitmap[i] = 1
        else:
            bitmap[i] = 0
            
    elif child2 < len(bitmap):
        if bitmap[child2] == 1:
            bitmap[i] = 1
        else:
            bitmap[i] = 0            
    
    if i > 0:
        rearrange_map(int(i/2))
        

print(header)
print(bitmap)
clear_bit(7, 1)
print(bitmap)
set_bit(10, 1)
print(bitmap)
clear_bit(7, 4) 
print(bitmap)
set_bit(3, 2)
print(bitmap)   
    