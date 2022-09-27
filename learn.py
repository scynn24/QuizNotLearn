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
            time.sleep(.05)
    time.sleep(.05)

def check(response, df):
    temp = 0
    for thing in df:
        responseList = response.split(", ")
        for thingy in responseList:
            if thingy.lower() == thing.lower():
                print("You got the right answer!!\n")
                time.sleep(1)
                temp = 1
                break
        if temp == 1:
            break
    if temp == 0:
        print("That's not right. The correct answer is...\n")
        for a in range(len(df)-1):
            print(df[a] + ", ", end="")
        print(df[len(df)-1])
        time.sleep(1)




while True:
    printy("Choose a set")
    fileName = input(": ")

    try:
        with open(fileName, "r") as a_file:
            for line in a_file:
                strippedLine = line.strip()
                splitLine = re.split(", |; |\(|\)| \(", strippedLine)
                if a == 0:
                    tempWord = splitLine
                else:
                    vocab.append((tempWord, splitLine))
                a = (a+1)%2
        break
    except FileNotFoundError:
        printy("That is not a valid file\n")



print("\n\n\n\n\n\n\n\n\n\n")
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
        printer = ""
        for a in range(len(word)-1):
            printer += word[a] + ", "
        printer += word[len(word)-1] + "\n"
        printy(printer)
        
        if i == 0 & len(visited) != 1:
            time.sleep(.2)
            printy("Is it...\n")
            time.sleep(.2)
            randList[0] = randInt
            for a in range(1, 4):
                newRand = random.randint(0, len(visited)-1)
                randList[a] = visited[newRand]
            
            randStart = random.randint(0, 3)
            for a in range(4):
                printer = "    "
                randWord = vocab[randList[(randStart+a)%4]][1]
                for b in range(len(randWord)-1):
                    printer += randWord[b] + ", "
                printer += randWord[len(randWord)-1] + "\n"
                printy(printer)

        
        printy("Please input the definition")
        response = input(": ")
        
        check(response, df)

        if len(visited) == 0:
            break
        
    printy("Do you want to continue (Y/N)")
    cont = input(": ")
    if cont.lower() == "n":
        break