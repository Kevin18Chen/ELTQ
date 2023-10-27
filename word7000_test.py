'''
windows
pip install pyttsx3
linux
pip install pyttsx3
maybe
sudo apt install espeak
sudo apt-get install alsa-utils
'''
from random import randint
import pyttsx3
import csv
import platform
import os

def clear_screen(os_name):
    if(os_name == 'Windows'):
        os.system('cls')
    elif(os_name == 'Linux'):
        os.system('clear')
        
os_name = platform.system()
f = open('word.csv', newline='', encoding='utf-8')
word = list(csv.reader(f, delimiter=','))
wordlen = len(word)
f.close()

clear_screen(os_name)

rannums = 1
rannuml = wordlen - 1
testnum = 10

def settung():
    global testnum,rannums,rannuml,wordlen
    clear_screen(os_name)
    print('總題數：' + str(wordlen - 1) + '\tOS：' + str(os_name))
    print('答題範圍 ' + str(rannums) + '~' + str(rannuml) + '\t作答題數 ' + str(testnum),end ='\n\n')
    rannums = int(input('答題範圍(開始)：'))
    rannuml = int(input('答題範圍(結束)：'))
    testnum = int(input('作答題數：'))

def typewd(fun):
    global word,wordlen,rannums,rannuml,testnum
    num = 0
    ans = ''
    topic = []
    if(fun == 1):
        engine = pyttsx3.init()
    for i in range(testnum):
        num = randint(rannums,rannuml)
        try:
            while(topic.index(num) >= 0):
                num = randint(rannums,rannuml)
        except:
            topic.append(num)
        print(str(i + 1) + '：' + str(word[num][0]) + '\t' + str(word[num][1]) + '\t' + str(word[num][2]))
        if(fun == 1):
            engine.say(word[num][0])
            engine.runAndWait()
        while(ans != word[num][0]):
            try:
                ans = input('answer：')
            except KeyboardInterrupt:
                break
        clear_screen(os_name) 
    
def Pinyin(fun):
    global word,wordlen,rannums,rannuml,testnum
    num = 0
    error = []
    topic = []
    yans = []
    if(fun == 1):
        engine = pyttsx3.init()
    for i in range(testnum):
        num = randint(rannums,rannuml)
        try:
            while(topic.index(num) >= 0):
                num = randint(rannums,rannuml)
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
    
    clear_screen(os_name)     
    for i in range(len(error)):
        print('{0:<18}{1:<18}{3:<12}{2:<20}'.format(yans[i],error[i][0],error[i][1],error[i][2]))
    print('答錯' + str(len(error)) + '題')

def choose(fun):
    global word,wordlen,rannums,rannuml,testnum
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
        num = randint(rannums,rannuml)
        try:
            while(topic.index(num) >= 0):
                num = randint(rannums,rannuml)
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
            Options[str(cosn)] = word[randint(rannums,rannuml)][1]
            while(1):
                if(Options[str(cosn)] == word[num][1]):
                    Options[str(cosn)] = word[randint(rannums,rannuml)][1]
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
        clear_screen(os_name)
    for err in error:
        print('{0:<18}{2:<12}{1:<20}'.format(err[0],err[1],err[2]))
    print('答錯' + str(len(error)) + '題')
    
def test():
    while(1):
        mod = int(input('0.設定, 1.拼字無聲, 2.拼字有聲, 3.選字無聲, 4.選字有聲, 5.練習無聲, 6.練習有聲：'))
        clear_screen(os_name)
        if(mod == 1):
            Pinyin(0)
        elif(mod == 2):
            Pinyin(1)
        elif(mod == 3):
            choose(0)
        elif(mod == 4):
            choose(1)
        elif(mod == 5):
            typewd(0)
        elif(mod == 6):
            typewd(1)
        elif(mod == 0):
            settung()
        else:
            break;

if(__name__ == '__main__'):
    test()