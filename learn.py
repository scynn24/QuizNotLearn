from ast import Break
import random
import time
import re
vocab = []
a = 0
tempWord = []


def printy(printer):
    for char in printer:
        if char != "\n":
            print(char, end = '', flush = True)
            time.sleep(.04)
        else:
            print(char, end = '', flush = True)
            time.sleep(.06)
    time.sleep(.06)

def check(response, df):
    temp = 0
    for thing in df:
        response = response.replace(" (", ", ").replace(")", "")
        responseList = response.split(", ")
        for thingy in responseList:
            if thingy.lower() == thing.lower():
                printy("You got the right answer!!\n")
                time.sleep(1)
                temp = 1
                break
        if temp == 1:
            break
    if temp == 0:
        printy("That's not right. The correct answer is...\n")
        printy(toString(df, False))
        time.sleep(1)

def toString(word, t):
    if t:
        printer = "    "
    else:
        printer = ""
    printer += word[0]
    a = 1
    while a < len(word):
        if word[a] != "(":
            printer += ", " + word[a]
        else:
            a += 1
            printer += " (" + word[a] + ")"
        a += 1

            
    printer += "\n"
    return printer




while True:
    printy("Choose a set")
    fileName = input(": ")

    try:
        with open(fileName, "r") as a_file:
            for line in a_file:
                strippedLine = line.strip().replace(" (", ", (, ").replace(")", "")
                splitLine = re.split(", |; ", strippedLine)
                if a == 0:
                    tempWord = splitLine
                else:
                    vocab.append((tempWord, splitLine))
                a = (a+1)%2
        break
    except FileNotFoundError:
        printy("That is not a valid file\n")



printy("\n\n\n\n\n\n\n\n\n\n")
visited = []
num = 0
randInt = 0
randList = [0, 0, 0, 0]
for i in range(3):
    
    word = []
    df = []
    for e in range(len(vocab)):
        visited.append(e)
    
    while True:
        num = random.randint(0, len(visited)-1)
        randInt = visited[num]
        if i == 2:
            word = vocab[randInt][1]
            df = vocab[randInt][0]
        else:
            word = vocab[randInt][0]
            df = vocab[randInt][1]
        visited.remove(visited[num])

        print("\n")
        printy(toString(word, False))
        
        if i == 0 & len(visited) != 1:
            time.sleep(.06)
            printy("Is it...\n")
            time.sleep(.06)
            randList[0] = randInt
            for a in range(1, 4):
                newRand = random.randint(0, len(visited)-1)
                randList[a] = visited[newRand]
            
            randStart = random.randint(0, 3)
            for a in range(4):
                randWord = vocab[randList[(randStart+a)%4]][1]
                printy(toString(randWord, True))

        
        printy("Please input the definition")
        response = input(": ")
        
        check(response, df)

        if len(visited) == 0:
            break
        
    printy("Do you want to continue (Y/N)")
    cont = input(": ")
    if cont.lower() == "n":
        break