from ast import Str


Wordlist = [None]

def Backup():
    f = open('Answers.txt', 'r')
    x = f.read()
    f.close()
    f = open('backup.txt','w')
    print('backup created')
    f.write(x)
    f.close
    global Wordlist
    Wordlist = x.split()


def lengClean():
    global Wordlist
    tem = []
    leng = input('enter length of words: ')
    for w in Wordlist:
        if str(len(w)) == leng:
            tem.append(w)
    print( str(len(Wordlist)-len(tem))+' words removed')
    Wordlist = tem

def sorting():
    global Wordlist
    Wordlist.sort()
    f = open('sorted.txt','w')
    for w in Wordlist:
        f.writelines(str(w)+'\n')
    print('sorted created')

def unique():
    global Wordlist
    f = open('unique.txt','w')
    for w in Wordlist:
        wei = 0
        for i,cha in enumerate(w):
            if cha not in w[i+1:len(w)]:
                wei+=1
        if wei == len(w):
            f.write(w+'\n')
    f.close()
    print('unique words stored')

def alphabetfreq():
    global Wordlist
    f = open('alphfreq.txt', 'w')
    for i in range(len(Wordlist[0])):
        dict = {} 
        ch = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
        for c in ch:
            dict[c] = 0
        for w in Wordlist:
            dict[w[i]] += 1
        dict1 = sorted(dict, key=dict.get,reverse=True)
        for j,r in enumerate(dict1):
            if j == len(dict1)-1 and i == len(Wordlist[0])-1:
                f.write(str(i)+','+str(26-j)+','+str(r))
            else:
                f.write(str(i)+','+str(26-j)+','+str(r)+'\n')
    f.close()

def weightage():
    f = open('unique.txt', 'r')
    x = f.read()
    f.close()
    f = open('alphfreq.txt', 'r')
    a = f.read()
    f.close()
    af = a.split('\n')
    Wordlist = x.split()

    weight = {}
    for w in Wordlist:
        weig = 0
        for i,cha in enumerate(w):
            for a in af:
                a = a.split(',')
                if str(i) == str(a[0]) :
                    # print(cha)
                    if cha == a[2]:
                        # print(str(i) +'=='+ str(a[0]) +'and'+ str(cha) +'=='+ str(a[2]))
                        weig += int(a[1])

        weight[w] = weig
    weight1 = sorted(weight, key=weight.get,reverse=True)
    f = open('uniqueWeight.txt', 'w')
    for r in weight1:
        s = str(r)+','+str(weight[r])
        f.write(s+'\n')
    f.close()
    
    
    ## find weight of each unique word based on alpha frequency and make a 
    ## weighted list file then use that to find 2nd best word
    ## then run primary auto player




Backup()
# lengClean()   check for non alpha char
sorting()
unique()
alphabetfreq()
weightage()