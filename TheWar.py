import random as r
import time as t
s="Ready to battle"
dchance=5
coins=0
def multiplayer():
    sta=[]
    playernumber=2
    for letter in s:
        print(letter,end='')
        t.sleep(0.04)
    print()
    while True:
        print("number of players?")
        playernumber=int(input())
        if playernumber<=1 or playernumber>=5:
            print("INVALID!")
        else:
            break
    playerhealth=[100,100,100,100,100]
    playersp=[True,True,True,True,True]
    done=False
    while done==False:
        for i in range(playernumber):
            if(playerhealth[i]<=0):
                continue
            crichance=[5,5,5,5,5]
            print("Player ",end='')
            print(i+1,end='')
            print("'s turn")
            print("Does Player ",end='')
            print(i+1,end=' ')
            print("believes in his/her luck?(y/n)")
            luck=input()
            if(luck=="y"):
                num=int(input("Guess a number(0,100):"))
                ans=r.randint(0,100)
                comc=r.randint(0,100)
                print("Computer chooses ",end='')
                print(comc)
                comc=abs(comc-ans)
                num=abs(num-ans)
                print("The answer was",end='')
                print(ans)
                if comc==num:
                    print("Nothing happens.")
                elif comc<num:
                    print("No chance of critical hit")
                    crichance[i]=0
                else:
                    print("+%5 chance of critical hit")
                    crichance[i]+=5
            print("1.repair(5% chance of +20hp,otherwise +5hp)")
            print("2.normal attack(computer -10hp, critical hit -15hp)")
            print("3.Superpower(can only use one time, damage varies randomly from 5 to 30)")
            choice=int(input())
            if(choice<1 or choice>3):
                print("INVALID! SINCE YOU ENTERED THE WRONG NUMBER INTENSIONALLY, THE GAME IS OVER. YOU ALL LOSE!")
                return;
            if choice==1:
                randn=r.randint(1,100)
                if(randn>=1 and randn<=5):
                    playerhealth[i]+=20
                else:
                    playerhealth[i]+=5
                print("Player ",end='')
                print(i+1,end="'s health: ")
                print(playerhealth[i])
            elif(choice==2):
                print("Who do you want to hit?")
                for i in range(playernumber):
                    print(i+1,end='.')
                    print("Player",end='')
                    print(i+1,end='')
                    print("HP: ",end='')
                    print(playerhealth[i])
                hitplayer=int(input())
                if(hitplayer<=0 or hitplayer>playernumber):
                    print("INVALID! SINCE YOU ENTERED THE WRONG NUMBER INTENSIONALLY, THE GAME IS OVER. YOU ALL LOSE!")
                    return;
                hitplayer=hitplayer-1
                randn=r.randint(1,100)
                if(randn>=1 and randn<=crichance[i]):
                    playerhealth[hitplayer]-=15
                    print("CRITICAL HIT!!!")
                else:
                    playerhealth[hitplayer]-=10
                print("Player ",end='')
                print(hitplayer+1,end="'s health: ")
                print(playerhealth[hitplayer])
            else:
                if(playersp[i]==False):
                    print("What did I say earlier? You wasted you turn.")
                    continue
                playersp[i]=False
                randn=r.randint(5,30)
                print("Who do you want to hit?")
                for i in range(playernumber):
                    print(i+1,end='.')
                    print("Player",end='')
                    print(i+1,end='')
                    print("HP: ",end='')
                    print(playerhealth[i])
                hitplayer=int(input())
                if(hitplayer<=0 or hitplayer>playernumber):
                    print("INVALID! SINCE YOU ENTERED THE WRONG NUMBER INTENSIONALLY, THE GAME IS OVER. YOU ALL LOSE!")
                    return;
                hitplayer-=1
                playerhealth[hitplayer]-=randn
                print("You did ",end='')
                print(randn,end=" damage.\n")
                print("Player ",end='')
                print(hitplayer+1,end="'s health: ")
                print(playerhealth[hitplayer])
            peopleAlive=False
            First=False
            people=0
            person=1
            for i in range(playernumber):
                if(playerhealth[i]<=0):
                    print("Player ",end='')
                    print(i+1,end=" is dead.\n")
                    sta.append(i+1)
                    if First==True:
                        peopleAlive=True
                    else:
                        First=True
                        person=i
                else:
                    people+=1
            if people==1:
                done=True
                sta.append(person+1)
                break
    for i in range(playernumber):
        if playerhealth[i+1]>0:
            print("Player "+str(i)+" wins!")
def singlePlayer(dchancperc):
    global coins
    global dchance
    name=input("Name:")
    for letter in s:
        print(letter,end='')
        t.sleep(0.04)
    for i in range(1,4):
        print('.',end='')
        t.sleep(0.1)
    print('.')
    computer=100
    player=100
    supow=False
    while True:
        chancperc=dchancperc
        ch=input("Do you believe in your luck?(y/n)")
        if(ch=='y' or ch=='Y'):
            choice=input("Rock, paper, or scissors?")
            comchoice=r.randint(1,3)
            if(comchoice==1):
                print("computer chooses rock")
                if(choice.lower()=="paper"):
                    print("+10% chance of critical hit.")
                    chancperc+=10
                elif(choice.lower()=="scissors"):
                    print("no chance of critical hit.")
                    chancperc=0
                else:
                    print("Nothing happens.")
            elif(comchoice==2):
                print("computer chooses paper")
                if(choice.lower()=="scissors"):
                    print("+10% chance of critical hit.")
                    chancperc+=10
                elif(choice.lower()=="rock"):
                    print("no chance of critical hit.")
                    chancperc=0
                else:
                    print("Nothing happens.")
            else:
                print("computer chooses scissors")
                if(choice.lower()=="rock"):
                    print("+10% chance of critical hit.")
                    chancperc+=10
                elif(choice.lower()=="paper"):
                    print("no chance of critical hit.")
                    chancperc=0
                else:
                    print("Nothing happens.")
        print("YOUR TURN")
        print("1.repair(5% chance of +20hp,otherwise +5hp)")
        print("2.normal attack(computer -10hp, critical hit -15hp)")
        print("3.Super power(can only use one time, damage varies randomly from 5 to 30)")
        atachoice=int(input("What do you chose(1,2,3)?: "))
        if(atachoice==2):
            randn=r.randint(1,100)
            if(randn>=1 and randn<=chancperc):
                computer-=15
                print("CRITICAL HIT!!!")
            else:
                computer-=10
        elif(atachoice==1):
            randn=r.randint(1,100)
            if(randn>=1 and randn<=5):
                player+=20
            else:
                player+=5
        else:
            if(supow==False):
                computer-=r.randint(5,30)
                supow=True
            else:
                print("What did I say earlier? You wasted you turn.")
        if(computer<=0):
            print("YOU WIN")
            coins+=player
            break
        print(name,"hp:",player)
        print("computer hp:",computer)
        print("COMPUTER'S TURN")
        if(computer<=50):
            randn=r.randint(1,100)
            if(randn<=50):
                randn=r.randint(1,5)
                if(randn<=5):
                    computer+=20
                else:
                    computer+=5
        else:
            randn=r.randint(1,100)
            if(randn<=80):
                randn=r.randint(1,100)
                if(randn<=5):
                    player-=20
                else:
                    player-=10
            else:
                player-=r.randint(5,30)
        if(player<=0):
            print("YOU LOSE")
            coins-=computer
            if(coins<0):
                coins=0
            break
        print(name,"hp:",player)
        print("computer hp:",computer)


def shop():
    global coins
    global dchance
    print("SHOP   You have $",end='')
    print(coins)
    print("1. More chance to critical hit(cost $100)")
    print("2.exit")
    print("More stuff coming soon!")
    choice=int(input("Your choice: "))
    if(choice==1):
        if(coins>=100):
            coins-=100
            dchance+=5
            print()
        else:
            print("You don't have enough money!")
            home()
            print("\n")
        shop()
    elif(choice==2):
        home()
        print()
    else:
        print("INVALID!!!")
        print()
        shop()
def home():
    t.sleep(1)
    print("\n")
    global coins
    global dchance
    if(coins<0):
        coins=0
    print("Your load code:")
    print(coins,end='.')
    print(r.randint(1000,9999))
    print(dchance,end='.')
    print(r.randint(1000,9999))
    print("1. Singleplayer")
    print("2. Multiplayer")
    print("3. Shop")
    print("4. Load Game")
    print("5. Exit Game:")
    print("tip: if you find a bug, tell me!\nbut, if you're not sure it's a bug, it may not be a bug.")
    choice=int(input("Your choice(1,2,3,4,5): "))
    if(choice==1):
        singlePlayer(dchance)
    elif choice==3:
        shop()
    elif choice==2:
        multiplayer()
    elif choice==4:
        code=float(input("code (copy EXACTLY what it printed out) : "))
        codet=float(input())
        dchance=int(codet)
        coins=int(code)
    elif choice==5:
        sure=input("Are you sure you want to exit? (y/n) ")
        if sure=='y':
            exit()
        if sure!='n':
            print("INVALID!!!")
    home()
home()
