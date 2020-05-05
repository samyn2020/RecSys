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
recList = []
listRec = []
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

for i in range(len(recList)):
    sList[i] -= recList[i]

while sum(sList) != len(sList) * -1:
    for x in sList:
        if x == max(sList):
            listRec.append( sList.index( max( sList ) ) )
            sList[sList.index(x)] = -1
listRec.remove(rec)

for aList in uLists:
    if aList[rec] == 2:
        print("It is highly recommended that User watch Movies " +str(listRec))