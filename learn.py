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
            time.sleep(.03)
        else:
            print(char, end = '', flush = True)
            time.sleep(.055)
    time.sleep(.055)

def check(response, df):
    temp = 0
    for thing in df:
        response = response.replace(" (", ", ").replace(")", "")
        responseList = response.split(", ")
        for thingy in responseList:
            if thingy.lower() == thing.lower():
                temp += 1
    if temp >= len(df):
        printy("You got the right answer!!\n")
        time.sleep(1)
    elif temp == 0:
        printy("That's not right. \nThe correct answer is...\n")
        printy(toString(df, True))
        time.sleep(1)
    else:
        printy("You got the right answer!!\nThe full answer is...\n")
        printy(toString(df, True))
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
    printy("\nChoose a set")
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


totList = []
for i in range(len(vocab)):
    totList.append(i)


printy("Choose a difficulty level (1-3)")
difficulty = input(": ")
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
    
    for e in range(1, len(vocab)+1):
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
        visited.remove(visited[num])


        printy(toString(word, False))
        
        if i == 0 & len(visited) != 1:
            time.sleep(.06)
            printy("Is it...\n")
            time.sleep(.06)
            randList = random.sample(totList, k=3)
            randList.append(randInt)
            
            randStart = random.randint(0, 3)
            for a in range(4):
                randWord = vocab[randList[(randStart+a)%4]][1]
                printy(toString(randWord, True))

        
        printy("Please input the definition")
        response = input(": ")
        
        check(response, df)

        
    printy("Do you want to continue (Y/N)")
    cont = input(": ")
    if cont.lower() == "n":
        break
    else:
        i += 1