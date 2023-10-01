'''
install pyttsx3
pip install pyttsx3
'''
from random import randint
import pyttsx3
import csv
import os

os.system('cls')
f = open('word.csv', newline='', encoding='utf-8')
word = list(csv.reader(f, delimiter=','))
wordlen = len(word)
f.close()

rannum = 140
testnum = 10

def settung():
    global rannum,testnum,wordlen
    print('總題數：' + str(wordlen))
    rannum = int(input('答題範圍(題號到最後一題)：'))
    testnum = int(input('作答題數：'))
    
def Pinyin(fun):
    global word,wordlen,rannum,testnum
    num = 0
    error = []
    topic = []
    yans = []
    if(fun == 1):
        engine = pyttsx3.init()
    for i in range(testnum):
        num = randint(rannum+1,wordlen-1)
        try:
            while(topic.index(num) >= 0):
                num = randint(rannum+1,wordlen-1)
        except:
            topic.append(num)
        #print('答對：{0:<10}答錯：{1:<10}'.format(testnum-len(error),len(error)))
        print(str(i + 1) + '：' + str(word[num][1]) + '\t' + str(word[num][2]))
        if(fun == 1):
            engine.say(word[num][0])
            engine.runAndWait()
        ans = input('answer：')
        if(ans != word[num][0]):
            error.append(word[num])
            yans.append(ans)
    
    os.system('cls')       
    for i in range(len(error)):
        print('{0:<18}{1:<18}{3:<12}{2:<20}'.format(yans[i],error[i][0],error[i][1],error[i][2]))
    print('答錯' + str(len(error)) + '題')

def choose(fun):
    global word,wordlen,rannum,testnum
    num = 0
    cosn = 0
    ansn = 0
    error = []
    topic = []
    if(fun == 1):
        engine = pyttsx3.init()
    for i in range(testnum):
        Options = {'1':'','2':'','3':'','4':''}
        Dreg = [1,2,3,4]
        num = randint(rannum+1,wordlen-1)
        try:
            while(topic.index(num) >= 0):
                num = randint(rannum+1,wordlen-1)
                topic.index(num)
        except:
            topic.append(num)
        print('答對：{0:<10}答錯：{1:<10}'.format(i-len(error),len(error)))
        print(str(i + 1) + '：' + str(word[num][0]) + '\t' + str(word[num][2]))
        cosn = Dreg[randint(0,len(Dreg)-1)]
        ansn = cosn
        Options[str(cosn)] = word[num][1]
        Dreg.remove(cosn)
        for n in range(3):
            cosn = Dreg[randint(0,len(Dreg)-1)]
            Options[str(cosn)] = word[randint(rannum+1,wordlen-1)][1]
            while(1):
                if(Options[str(cosn)] == word[num][1]):
                    Options[str(cosn)] = word[randint(rannum+1,wordlen-1)][1]
                else:
                    Dreg.remove(cosn)
                    break
        print('1：%-18s\n2：%-18s\n3：%-18s\n4：%-18s' % (Options['1'],Options['2'],Options['3'],Options['4']))
        if(fun == 1):
            engine.say(word[num][0])
            engine.runAndWait()
        ans = input('answer：')
        if(ans != str(ansn)):
            error.append(word[num])
        os.system('cls')
    for err in error:
        print('{0:<18}{2:<12}{1:<20}'.format(err[0],err[1],err[2]))
    print('答錯' + str(len(error)) + '題')
    
def test():
    while(1):
        mod = int(input('1.拼字無聲, 2.拼字有聲, 3.選字無聲, 4.選字有聲, 5.設定：'))
        os.system('cls')
        if(mod == 1):
            Pinyin(0)
        elif(mod == 2):
            Pinyin(1)
        elif(mod == 3):
            choose(0)
        elif(mod == 4):
            choose(1)
        elif(mod == 5):
            settung()
        else:
            break;
test()
