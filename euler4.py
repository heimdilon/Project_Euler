# Created by kor_a at 07 11 2020
# Time: (23:48)

x = 1
y = 1
n = 1000
elements = []

allNumbers = []

def Ispalindromic(a):
    b = [int(d) for d in str(a)]
    Firsthalf = b[:3]
    Secondhalf = b[3:]
    if Firsthalf == Secondhalf[::-1]:
        return True
    else:
        return False

for x in range(n):
    for y in range(n):
        testValue = x*y
        if Ispalindromic(testValue) == True:
            allNumbers.append(testValue)
            elements.append(x)
            elements.append(y)

reverseNums = allNumbers[::-1]
BiggestNum = reverseNums[0]

revElements = elements[::-1]
x = revElements[1]
y = revElements[0]

print({x}, "*", {y}, "=", {BiggestNum})






