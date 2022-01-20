import sys
from itertools import combinations

def getinput():
    filelines = input("Enter amount of cards: ")

    listofinputs = []

    for i in range(int(filelines)):
        x = input()
        listofinputs.append(x)

    return listofinputs

def symbolchecker(symbol):
    tracker = {"$": "S","$": "s", "@":"a", "@": "A", "#":"H", "#":"h"}

    if symbol in tracker:
        symbol = tracker[symbol]
    else:
        symbol = symbol.lower()

    return symbol



def isSet(cards):
    #make list of combinations
    combos = (combinations(cards,3))
    listofcombos = [" ".join(i) for i in combos]
    #print(listofcombos)
    #print(listofcombos)

    answers = []
    #print(listofcombos)
    for i in listofcombos:
        splitted = i.split()
        
        firstcolor = splitted[0]
        firstsymbol = splitted[1][0]
        firstamount = len(splitted[1])
        firstusedsym = symbolchecker(firstsymbol)


        secondcolor = splitted[2]
        secondsymbol = splitted[3][0]
        secondamount = len(splitted[3])
        secondusedsym = symbolchecker(secondsymbol)
        
        thirdcolor = splitted[4]
        thirdsymbol = splitted[5][0]
        thirdamount = len(splitted[5])
        thirdusedsym = symbolchecker(thirdsymbol)

        #check if the case of the symbols are the same

        #print(firstcolor, secondcolor, thirdcolor)
        if (firstcolor == secondcolor == thirdcolor) or (firstcolor != secondcolor and firstcolor != thirdcolor and secondcolor != thirdcolor): 
            #print("same color")
            if (firstamount ==  secondamount == thirdamount) or (firstamount != firstamount and firstamount != thirdamount and secondamount != thirdamount):
                if (firstusedsym == secondusedsym == thirdusedsym) or (firstusedsym != secondusedsym and firstusedsym != thirdusedsym and secondusedsym != thirdusedsym):
                    if (firstsymbol == secondsymbol == thirdsymbol) or (firstsymbol != secondsymbol and firstsymbol != thirdsymbol and secondsymbol != thirdsymbol):
                        answers.append([i])


    return answers



def makecardlist(cards):
    cardslist = []
    for i in range(len(cards)):
        setcheck1 = cards[i][0].split()

        #card 1
        firstcolor = setcheck1[0]
        firstsymbol = setcheck1[1][0]
        firstamount = len(setcheck1[1])
        firstusedsym = symbolchecker(firstsymbol)
        card1 = firstcolor + " "+ firstsymbol

        #card 2
        secondcolor = setcheck1[2]
        secondsymbol = setcheck1[3][0]
        secondamount = len(setcheck1[3])
        secondusedsym = symbolchecker(secondsymbol)
        card2 = secondcolor + " " + secondsymbol

        #card3
        thirdcolor = setcheck1[4]
        thirdsymbol = setcheck1[5][0]
        thirdamount = len(setcheck1[5])
        thirdusedsym = symbolchecker(thirdsymbol)
        card3 = thirdcolor +  " " + thirdsymbol

        cardslist.append(set([card1, card2, card3]))

    return cardslist


def disjoint(listofsets):
    answers = []
    for i in range(len(listofsets)):
        check1 = listofsets[i]
        joints = []
        for j in range(i+1, len(listofsets)):
            check2 = listofsets[j]
            if check1.isdisjoint(check2):
                joints.append(check2)
                if listofsets[i] not in joints:
                    joints.append(check1)
        if joints:
            answers.append(joints)
    return answers



def getmaxDisjointset(listofdisjoint):
    listlen = [len(i) for i in listofdisjoint]
    return max(listlen)



def printdisjointset(listofdisjoint):
    listlen = {} 
    for index,value in enumerate(poop1):
        if len(value) not in listlen:
            listlen[len(value)] = [index]
        else:
            listlen[len(value)].append(index)

    maxkey = max(listlen)
    for i in listlen[maxkey]:
        for j in poop1[i]:
            print("\n")
            for elements in j:
                print(elements)

# x = ["blue #","green $","blue AA ","yellow @","blue @@@","green A", "yellow $$$", "yellow @@@", "yellow HHH", "yellow #", "yellow @@", "blue a", "blue sss", "green a", " green @"]
# test = ["blue # green $ yellow @"]
# bro = isSet(x)
# print(len(bro))
# poop = makecardlist(bro)
# poop1 = disjoint(poop)
# print(getmaxDisjointset(poop1))
# printdisjointset(poop1)

def evenSubarray(numbers, k):
    tracker = set()
    
    for i in range(len(numbers)):
        if numbers[i] % 2== 0:
            numodds = 0
        else:
            numodds = 1
            
        for j in range(i+1, len(numbers)+1):
            if tuple(numbers[i:j]) not in tracker:
                tracker.add(tuple(numbers[i:j]))
            if j< len(numbers):
                if numbers[j]%2==1:
                    numodds += 1
                    if numodds > k:
                        break
    return len(tracker)

tracker = []
numbers = [6,3,5,8]
print(numbers[2:4])
# for i in range(len(numbers)):
#     if numbers[i]%2==0:
#         numodds = 0
#     else:
#         numodds = 1
#     for j in range(i+1, len(numbers)+1):
#             numbercheck = numbers[i:j]
#             print(numbercheck)
#             if numbercheck not in tracker:
#                 tracker.append(numbercheck)
#             if j < len(numbers):
#                 if numbers[j]%2==1:
#                     numodds+=1
#                     if numodds>1:
#                         break
# print(tracker)

output = {**{}}
print(output)