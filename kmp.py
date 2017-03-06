import time

piArray = []


def getMilliseconds():
    return int( round( time.time() * 1000 ))


def computePrefixFunction(baseString):
    
    global piArray
    piArray = [0 for i in range(len(baseString))]
    
    length = 0 # length of the previous longest prefix suffix

    i = 1
 
    # the loop calculates lps[i] for i = 1 to M-1
    while i < len(baseString):
        if baseString[i]==baseString[length]:
            length += 1
            piArray[i] = length
            i += 1
        else:
            # This is tricky. Consider the example.
            # AAACAAAA and i = 7. The idea is similar 
            # to search step.
            if length != 0:
                length = piArray[length-1]
 
            # Also, note that we do not increment i here
            else:
                piArray[i] = 0
                i += 1   
    
    print(piArray)
          

def kmpMatcher(string1, string2):
    
    n = len(string1)
    m = len(string2)

    # create lps[] that will hold the longest prefix suffix 
    # values for pattern
    j = 0 # index for pat[]
 
    # Preprocess the pattern (calculate lps[] array)
    computePrefixFunction(string2)
 
    i = 0 # index for txt[]
    while i < n:
        if string2[j] == string1[i]:
            i += 1
            j += 1
 
        if j == m:
            return i-j
            j = piArray[j-1]
 
        # mismatch after j matches
        elif i < n and string2[j] != string1[i]:
            # Do not match lps[0..lps[j-1]] characters,
            # they will match anyway
            if j != 0:
                j = piArray[j-1]
            else:
                i += 1
    
    return -1


def naiveMatcher(string1, string2):
    return string1.find(string2)
            

s1 = "yaafqaafkdhaafqaaraafquqaafqaagaafsajaafqaaflazaafqakaafqaafaafqaafkaafqaayaazaaftaafqaafkaafqaaybaaf"
s2 = "aafqaafkaafqaayaazaaf"
time1 = getMilliseconds()
print(kmpMatcher(s1, s2))
time2 = getMilliseconds()
print(naiveMatcher(s1, s2))
time3 = getMilliseconds()

print("Time1: " + str(time2-time1) + " Time2: " + str(time3-time2))


