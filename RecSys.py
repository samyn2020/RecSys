# m   0  1  2  3  4  5  6  7
u0 = [1, 0, 0, 0, 1, 1, 1, 0]
u1 = [0, 0, 1, 0, 0, 1, 0, 0]
u2 = [1, 1, 1, 0, 1, 0, 0, 0]
u3 = [0, 0, 0, 0, 0, 0, 0, 1]
u4 = [1, 0, 0, 1, 0, 1, 1, 1]
u5 = [1, 1, 0, 1, 1, 0, 1, 0]
u6 = [1, 0, 1, 1, 0, 0, 0, 0]
u7 = [1, 0, 1, 1, 1, 1, 0, 1]
u8 = [0, 1, 0, 0, 0, 0, 1, 1]
# u9 = [0, 0, 0, 1, 0, 0, 1, 0]
u9 = [0, 0, 0, 1, 2, 0, 1, 0]
uLists = [u0, u1, u2, u3, u4, u5, u6, u7, u8, u9]
print(uLists)
sList = []
wList = []
recList = []
listCount = 0
watchCount = 0
rec = 0
uIndex = 0
# cycle uLists (user lists) for rec (recommendation location)
# and set recList (user list with recommendation location) to aList (current list in cycle)
for aList in uLists:
    for x in aList:
        if x == 2:
            rec = aList.index(2)
            recList = aList[:]
# cycle uLists for sList (sum list of viewer lists)
for aList in uLists:
    if aList[rec] == 1:
        listCount += 1
        # set sList to aList if sList is empty
        if len(sList) == 0:
            sList = aList[:]
        # otherwise add aList to sList
        else:
            for i in range(len(aList)):
                sList[i] += aList[i]

# create wList (weight list)
for i in range(len(sList)):
    wList.append(sList[i] / listCount)

for i in range(len(wList)):
    if recList[i] == 1:
        recList[i] = wList[i]
        watchCount += 1

wSum = sum(recList) - 2
pChance = (wSum / watchCount) * 100

print("There is a " + str(pChance) + "% chance that User will watch Movie")
for aList in uLists:
    if aList[rec] == 2:
        if pChance < 50:
            print("User WILL NOT watch Movie")
            aList[rec] = 0
        else:
            print("User WILL watch Movie")
            aList[rec] = 1
print(uLists)
