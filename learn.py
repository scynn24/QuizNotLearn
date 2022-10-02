from ast import Break
import random
import time
import re
vocab = []
a = 0
tempWord = []
charList = [" (", ": ", "; ", "... "]


def printy(printer):
    for char in printer:
        if char != "\n":
            print(char, end = '', flush = True)
            time.sleep(.03)
        else:
            print(char, end = '', flush = True)
            time.sleep(.055)
    time.sleep(.055)

def check(response, df):
    temp = 0
    for thing in df:
        responseList = lineParse(response)
        for thingy in responseList:
            if thingy.lower() == thing.lower():
                temp += 1
    if temp >= len(df):
        printy("You got the right answer!!\n")
        time.sleep(1)
        return 1
    elif temp == 0:
        printy("That's not right. \nThe correct answer is...\n")
        printy(toString(df, True))
        time.sleep(1)
        return 0
    else:
        printy("You got the right answer!!\nThe full answer is...\n")
        printy(toString(df, True))
        time.sleep(1)
        return 1

def toString(word, t):
    if t:
        printer = "    "
    else:
        printer = ""
    printer += word[0]
    a = 1
    while a < len(word):
        if word[a] not in charList:
            printer += ", " + word[a]
        elif word[a] == " (":
            a += 1
            printer += " (" + word[a] + ")"
        else:
            a += 1
            printer += word[a-1] + word[a]
        a += 1

            
    printer += "\n"
    return printer


def lineParse(line):
    strippedLine = line.strip().replace(")", "")
    for thing in charList:
        strippedLine = strippedLine.replace(thing, ", "+ thing + ", ")
    return re.split(", |; ", strippedLine)


while True:
    printy("\nChoose a set")
    fileName = input(": ")


    try:
        with open(fileName, "r") as a_file:
            for line in a_file:
                splitLine = lineParse(line)
                if a == 0:
                    tempWord = splitLine
                else:
                    vocab.append((tempWord, splitLine))
                a = (a+1)%2
        break
    except FileNotFoundError:
        printy("That is not a valid file\n")


totList = []
for i in range(len(vocab)):
    totList.append(i)


printy("Choose a difficulty level (1-3)")
difficulty = input(": ")
printy("Build Repetition (Y/N)")
initRep = input(": ")
printy("\n\n\n\n\n\n\n\n\n\n")
num = 0
randInt = 0
visited = []
i = (int(difficulty)-1)%3



while i < 3:
    word = []
    df = []

    visited.clear()
    visited = totList.copy()
    score = 0

    e = 1
    while e < len(vocab) + 1:
        printer = "\n\nNo. " + str(e) + " of " + str(len(vocab)) + "\n"
        printy(printer)

        num = random.randint(0, len(visited)-1)
        randInt = visited[num]
        randList = []


        if i == 2:
            word = vocab[randInt][1]
            df = vocab[randInt][0]
        else:
            word = vocab[randInt][0]
            df = vocab[randInt][1]
        visited.remove(randInt)


        printy(toString(word, False))
        
        if i == 0:
            time.sleep(.06)
            printy("Is it...\n")
            time.sleep(.06)
            totList.remove(randInt)
            randList = random.sample(totList, k=3)
            randList.append(randInt)
            totList.append(randInt)
            
            randStart = random.randint(0, 3)
            for a in range(4):
                randWord = vocab[randList[(randStart+a)%4]][1]
                printy(toString(randWord, True))

        
        printy("Please input the definition")
        response = input(": ")
        
        tempScore = int(check(response, df))
        if (initRep.lower() != "n") & (tempScore == 0):
            visited.append(randInt)
        else:
            e += 1
        score += tempScore

    printy("\nYour final score for difficulty level " + str(i+1) + " is " + str(score) + " out of " + str(len(vocab)) + " \n")
    printy("Do you want to continue (Y/N)")
    cont = input(": ")
    if cont.lower() == "n":
        break
    else:
        i += 1