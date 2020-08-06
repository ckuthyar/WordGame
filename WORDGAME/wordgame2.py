from flask import Flask, render_template, request, redirect
wordgame2=Flask(__name__)
import random
import time as t
from datetime import time, datetime, timedelta
global playwords
global starttimelist
wordList1=[]
wordList2=[]
compwords=[]
playwords=[]
wordCount2=[]
alphabets=[]
gameWords1=[]
gameScore1=[]
starttimelist=[]
flag="SUCCESS"
playwords.append("____")
for i in range(97,97+26,1):
    alphabets.append(chr(i))


f1=open("EN1.txt", "r")
for i in range(1,18000,1):
    wordList1.append(f1.readline().replace("\n",""))
leng1=len(wordList1)


for j in range(0,26,1):
    words_char=[]
    for i in range(0,leng1,1):
        temp=wordList1[i]
        if(temp[0]==alphabets[j]):
            words_char.append(temp)
    leng2=len(words_char)
    wordCount2.append(leng2)
    wordList2.append(words_char)

@wordgame2.route("/play")
def displaypage():
    return render_template("startgame.html")


@wordgame2.route("/playen", methods=["POST", "GET"])
def displayengame():
    return render_template("ENgame.html")


@wordgame2.route("/playlive", methods=["POST", "GET"])
def displaywordgame():
    global chosen
    global comp
    global flag
    if request.method=="POST":
        form1 = request.form
        status1="LIVE"
        if status1 =="Hello World":
            return redirect('http://127.0.0.1:5000/playend')
        repeatlist=[]
        for j in range(0,2,1):
            """F1"""
            """print(compwords, "$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
            if(i!=0 and firstLetter!=gameWords1[-1][0][0]):
                flag="FAILURE1"
                print(firstLetter, chosen[-1], "Failure1 encountered###########################################################")
                status1="GAME OVER"
                break"""
            
            """F2 Time"""
            global starttime
            global endtime
            global diff
            global end
            global start
            time1 = '%H:%M:%S'
            player="___"
            print(player)
            chosen=""
            end=""
            
            for i in range (0,1,1):
                player=form1.get("s1")
                if player != playwords[0]:
                    endtime1=t.time()
                    print(endtime1)
                    starttime1=t.time()
                    starttimelist.append(starttime1)
                    print(starttime1)
                    if len(starttimelist)>0:
                        eltime=endtime1-starttimelist[-1]
                        eltime=int(eltime)
                        if eltime>=10:
                            print("WOWOWOWOWOWOWOWOWOW")
            
            """for i in range (0,1,1):
                player=form1.get("s1")
                if player != playwords[0]:
                    endtime1=datetime.now()
                    if len(starttimelist)>=1:
                        eltime=str(endtime1-starttimelist[-1])
                        eltime1=eltime[5:]
                        print(eltime1, "WOWOWOWOWOWOWO")"""
            """if int(eltime) >= 0o01000:
                print("ewhbfiywgvfbyrfugbreylvgbyhgvbjhyvbefhygvbjebj****dsjlbnejnvhjkuvnudenvbukij")
                print(endtime1)
            print(player)
            starttime1=datetime.now()
            starttimelist.append(starttime1)
            print(starttime1, "start5")"""

            """endtime=time(00, 00, 10)
            starttime=time()
            for i in range(0, 10, 1):
                endtime=time(00, 00, 10-i)
                t.sleep(1)
                print(endtime)
                player=form1.get("s1")
                if player!= playwords[-1]:
                    break
                elif endtime==starttime:
                    flag="FAILURE2"
                return redirect("http://127.0.0.1:5000/playend")     
                
                start = starttime.strftime(time1)
                end = endtime.strftime(time1)
                print(start, ",", end)"""
                
            
            """..."""
            thisRoundWords=[]
            thisRoundScore=[]
            firstLetter=player[0]
            lastLetter=player[-1]

            
            """F3"""
            position=alphabets.index(lastLetter)
            sizeList=len(wordList2[position])
            if(sizeList==0):
                flag="FAILURE3"
                break

            usedWord=""
            if player in wordList2:
                usedWord=player
                wordList2.remove(usedWord)

            if player not in repeatlist:
                repeatlist.append(player)
                continue
            elif player in repeatlist:
                flag="FAILURE4"
                """print("FAILURE4 *************************************")
                break"""
            randomn=random.randint(0,sizeList)
            chosen=wordList2[position][randomn]
            wordList2[position].remove(chosen)
            

            thisRoundWords.append(player)
            thisRoundWords.append(chosen)
            playwords.append(player)
            compwords.append(chosen)
            gameWords1.append(thisRoundWords)
            thisRoundScore.append(len(player))
            thisRoundScore.append(len(chosen))
            gameScore1.append(thisRoundScore)
    return render_template("ENgame.html",message=player, message1=chosen, seconds=end)
        


@wordgame2.route("/playend")
def displayend():

    playerScore=0
    computScore=0
    if (flag=="SUCCESS"):
        error1="Well Played."
    if (flag=="FAILURE1"):
        error1="Player word is incorrect. Game over. Computer wins"
    if (flag=="FAILURE2"):
        error1="Timeout 30 seconds. Game over. Computer wins"
    if (flag=="FAILURE3"):
        error1="Computer has run out of words. Game over. Player wins"
    if (flag=="FAILURE4"):
        error1="Player has repeated. Game Over. Computer Wins"
    error01=error1
    for i in range(0,len(gameScore1),1):
        playerScore=playerScore+gameScore1[i][0]
        computScore=computScore+gameScore1[i][1]
    finalmessage = "Congrats to both of you-", "Player:",playerScore, "Computer",computScore
    finalwords = gameWords1
    finalscore = gameScore1

    
    return render_template("endgame.html", error=error01, message=finalmessage, words=finalwords, score= finalscore)


if __name__== '__main__':
    wordgame2.run(debug=True)



