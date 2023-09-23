'''
install pyttsx3
pip install pyttsx3
'''
from random import randint
import pyttsx3
import csv

f = open('word.csv', newline='', encoding='utf-8')
word = list(csv.reader(f, delimiter=','))
wordlen = len(word)
f.close()

def soundword():
    global word,wordlen
    s = 0
    num = 0
    error = []
    topic = []
    engine = pyttsx3.init()
    for i in range(10):
        num = randint(s+1,wordlen-1)
        try:
            while(topic.index(num) >= 0):
                num = randint(s+1,wordlen-1)
        except:
            topic.append(num)
        print(str(i + 1) + '：' + str(word[num][1]) + '\t' + str(word[num][2]))
        engine.say(word[num][0])
        engine.runAndWait()
        ans = input('answer：')
        if(ans != word[num][0]):
            error.append(word[num])
            
    for err in error:
        print('{0:<18}{2:<8}{1:<20}'.format(err[0],err[1],err[2]))
    print('答錯' + str(len(error)) + '題')

def onlyword():
    global word,wordlen
    s = 0
    num = 0
    error = []
    topic = []
    for i in range(10):
        num = randint(s+1,wordlen-1)
        try:
            while(topic.index(num) >= 0):
                num = randint(s+1,wordlen-1)
                topic.index(num)
        except:
            topic.append(num)
        print(str(i + 1) + '：' + str(word[num][1]) + '\t' + str(word[num][2]))
        ans = input('answer：')
        if(ans != word[num][0]):
            error.append(word[num])
            
    for err in error:
        print('{0:<18}{2:<8}{1:<20}'.format(err[0],err[1],err[2]))
    print('答錯' + str(len(error)) + '題')

def chooseword():
    global word,wordlen
    s = 50
    num = 0
    cosn = 0
    ansn = 0
    error = []
    topic = []
    for i in range(10):
        Options = {'1':'','2':'','3':'','4':''}
        Dreg = [1,2,3,4]
        num = randint(s+1,wordlen-1)
        try:
            while(topic.index(num) >= 0):
                num = randint(s+1,wordlen-1)
                topic.index(num)
        except:
            topic.append(num)
        print(str(i + 1) + '：' + str(word[num][0]) + '\t' + str(word[num][2]))
        cosn = Dreg[randint(0,len(Dreg)-1)]
        ansn = cosn
        Options[str(cosn)] = word[num][1]
        Dreg.remove(cosn)
        for i in range(3):
            cosn = Dreg[randint(0,len(Dreg)-1)]
            Options[str(cosn)] = word[randint(s+1,wordlen-1)][1]
            while(1):
                if(Options[str(cosn)] == word[num][1]):
                    Options[str(cosn)] = word[randint(s+1,wordlen-1)][1]
                else:
                    Dreg.remove(cosn)
                    break
        print('1：%-18s2：%-18s3：%-18s4：%-18s' % (Options['1'],Options['2'],Options['3'],Options['4']))
        ans = input('answer：')
        if(ans != str(ansn)):
            error.append(word[num])
    for err in error:
        print('{0:<18}{2:<8}{1:<20}'.format(err[0],err[1],err[2]))
    print('答錯' + str(len(error)) + '題')
    
def test():
    while(1):
        mod = int(input('1.無聲, 2.有聲, 3.選字：'))
        if(mod == 1):
            onlyword()
        elif(mod == 2):
            soundword()
        elif(mod == 3):
            chooseword()
        else:
            break;

test()
