import random
from time import sleep
import pyautogui

LinePos = 0
notList = []
green = []
guesses = []
cWords = []
yellows = []
x = [570,630,690,750,810]
y = [215,260,320,380,440,500]
line = ''
def emoji(c):
    global line
    if c == (87, 172, 87) or c == (106, 170, 100) or c == (83, 141, 78):
        line += "g"
    elif c == (233, 198, 1) or c == (233, 190, 1) or c == (181, 159, 59):
        line += "y"
    elif c == (142, 142, 142) or c == (216, 216, 216) or c == (134, 136, 138) or c == (134, 136, 138) or c == (58, 58, 60):
        line += "b"
    else:
        line += "w"

def WinCheck():
    sleep(1)
    global line
    if line == 'ggggg':
        print('win')
        sleep(2)
        pyautogui.click(580,560)
        sleep(3)
        start()

def firstChoice():
    f = open('uniqueWeight.txt', 'r')
    x = f.read()
    f.close()
    lines = x.split('\n')
    words = lines[0]
    word = words.split(',')
    word[0]
    Keyboard(word[0])
    guesses.append(word[0])
    check()
def addtoNotList(c):
    global notList
    if c not in notList:
        notList.append(c)
def Keyboard(text):
    sleep(2)
    pyautogui.click(560,200)
    pyautogui.write(text+'\n') 

def charAtPos(c,pos):
    # print('removing all words with '+ c + ' not at '+str(pos))
    m = 100
    while m > 0:
        for i in cWords:
            if c != i[pos]:
                cWords.remove(i)
        m -= 1
    # print(str(len(cWords))+' words remain')

def haveACharNotHere(c,pos):
    yellows.append(c)
    # print('removing all words with '+ c + ' at '+str(pos))
    m = 100
    while m > 0:
        for i in cWords:
            if c == i[pos]:
                cWords.remove(i)
            if c not in i:
                cWords.remove(i) 
        m -= 1
    # print(str(len(cWords))+' words remain')

def whitechar(c):
    # print('removing all words with '+ c)
    m = 100
    while m > 0:
        for i in cWords:
            if c in i:
                if c in yellows:
                    continue
                if green[i.index(c)] == '':
                    cWords.remove(i)  
        m -= 1
    # print(str(len(cWords))+' words remain')

def check():
    global LinePos
    global x
    global line
    global green
    global guesses
    global yellows
    line = ''
    word = guesses[LinePos]
    # print(word)
    sleep(3)
    col()
    # print(line)
    for i,val in enumerate(line):
        if val == 'g':
            green[i] = word[i]
            charAtPos(word[i],i)
            addtoNotList(word[i])
        else:
            green[i]=''
        if val == 'y':
            haveACharNotHere(word[i],i)
    for i,val in enumerate(line):        
        if val == 'b':
            whitechar(word[i])
            addtoNotList(word[i])
    # if 'g' in line:
        # print(green)
    # print('words left: '+str(len(cWords)))
    # print(notList)
    printText()
    WinCheck()

def printText():
    global LinePos
    global guesses
    global line
    s = ''
    ce = '\33[0m'
    cy = '\33[93m'
    cg = '\33[92m'
    cw = '\33[90m'
    w = guesses[LinePos]
    for i,j in enumerate(line):
        if j == 'g':
            s += cg + w[i] + ce
        if j == 'y':
            s += cy + w[i] + ce
        if j == 'b':
            s += cw + w[i] + ce
    s += '\twords left: '+str(len(cWords))
    print(s)
        


def col():
    for i in x:
        c = pyautogui.pixel(i,int(y[LinePos]))
        emoji(c)
    # print(line)
def setgreen():
    global green
    for i in cWords[0]:
        green.append('')
def guess():
    ch = ''
    global LinePos
    LinePos += 1
    if green[4] == 'g' and green[3] == 'g':
        ch = erFix()
    else:
        ch = random.choice(cWords)
    Keyboard(ch)
    guesses.append(ch)
    check()
    

def erFix():
    global notList
    words = []
    f = open('uniqueWeight.txt', 'r')
    x = f.read()
    f.close()
    lines = x.split('\n')
    for l in lines:
        val = l.split(',')
        for i in notList:
            if i not in val[0]:
                words.append(val[0])
    a = random.choice(words)
    return a
        


def start():
    global cWords
    global LinePos
    global green
    global guesses 
    global yellows 
    global notList
    notList = []
    green = []
    guesses = []
    yellows = []
    f = open('Answers.txt', 'r')
    a = f.read()
    f.close()
    cWords = a.split()
    setgreen()
    
    LinePos = 0
    firstChoice()
    sleep(1)
    loop()

def loop():
    guess()
    guess()
    guess()
    guess()
    guess()

sleep(3)
start()