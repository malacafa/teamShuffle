import random
from time import sleep
import turtle as t

#intro
print("GSA_자연탐사_조배정 made by 2211 윤성훈 \n\n\n 각자 숫자를 하나씩 말씀(입력)해 주시길 바랍니다.")

#get file info
stu = open("stulist.txt","r")
stub = open("boy.txt","r")
stug = open("girl.txt","r")
output = open("finallist.txt","w")

studentlist = []
studentblist = []
studentglist = []
display = []

for x in stu:
    a,b=x.split(".")
    studentlist.append(b[:-1])

for x in stub:
    a,b=x.split(".")
    studentblist.append(b[:-1])

for x in stug:
    a,b=x.split(".")
    studentglist.append(b[:-1])
    
#get seed
seedinput=0
for x in range(1,7):
    k=int(input("%d : "%x))
    seedinput+=k

#random
random.seed(seedinput)
random.shuffle(studentlist)
random.shuffle(studentblist)
random.shuffle(studentglist)

#set seat for girls
girlseat = [0]*24
i=0
while True:
    girlseat[i]=random.choice([0,2])
    i +=1
    if i==23:
        if sum(girlseat,0.0) == 24:
            break
        else:
            i=0

#make a list name display
gcnt=0
bcnt=0
for x in range(1,24):
    string = "%02d조: "%x
    for _ in range(girlseat[x-1]):
        string +="\t%s"%studentglist[gcnt]
        gcnt+=1
    for _ in range(4-girlseat[x-1]):
        string +="\t%s"%studentblist[bcnt]
        bcnt+=1
    display.append(string)
string = "%02d조: "%24
for _ in range(girlseat[23]):
    string +="\t%s"%studentglist[gcnt]
    gcnt+=1
for cnt in range(73-bcnt):
    string +="\t%s"%studentblist[cnt+bcnt]
display.append(string)
    
#file write
for s in display:
    output.write(s+"\n")
output.close()

# turtle setting
t.title("GSA 2학년 자연탐사 조 뽑기")
t.hideturtle()
t.penup()
t.bgcolor("black")
t.color("red")
t.goto(-400,300)
t.write("GSA 2학년 자연탐사 조 뽑기(" + str(seedinput) + ")",True,"left",("궁서체",25,"bold"))
t.color("white")
t.write("by 2211",False,"left",("궁서체",10,"bold"))
t.goto(-400,280)
t.write("Full screen please. 바로 시작합니다!",False,"left",("궁서체",10,"bold"))

#dynamic effect
def dynamic(x):
    gcnt=0;bcnt=0
    for _ in range(x):
        gcnt+=girlseat[_]
    bcnt=4*(x+1)-gcnt
    sec=0.01
    t.penup()
    t.goto(-400,260+(x)*(-28))
    t.goto(-400,260+(x+1)*(-28))
    t.pendown()
    if x!=23:
        for _ in range(40):
            string = "%02d조: "%(x+1)
            for _ in range(girlseat[x]):
                string +="\t%s"%studentglist[random.randrange(gcnt,24)]
            for _ in range(4-girlseat[x]):
                string +="\t%s"%studentblist[random.randrange(bcnt,73)]
            t.write(string,False,"left",("나눔고딕",20,"bold"))
            t.undo()
            sleep(sec)
            sec+=0.0005
    else:
        t.write("\t\t마지막 24조는 !!!",False,"left",("나눔고딕",20,"bold"))
        t.undo()
        for a in range(5,0,-1):
            sleep(1)
            t.undo()
            t.write("\t\t%d"%a,False,"left",("나눔고딕",20,"bold"))
        sleep(1)
        t.undo()
    
t.undo()
t.undo()
for x in range(24):
    dynamic(x)
    sleep(0.1)
    t.write(display[x],False,"left",("나눔고딕",20,"bold"))
    sleep(0.5)


