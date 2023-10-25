def rps(n1,n2,b1,b2):
    p1=int(n1[b1])%3
    p2=int(n2[b2])%3
    if pl1[p1]==pl2[p2]:
        print("Draw")
    elif pl1[p1]=='r' and pl2[p2]=='s':
        print("Player 1 Wins")
    elif pl1[p1]=='p' and pl2[p2]=='r':
        print("Player 1 Wins")
    elif pl1[p1]=='s' and pl2[p2]=='p':
        print("Player 1 Wins")
    elif pl1[p1]=='r' and pl2[p2]=='s':
        print("Player 2 Wins")
    elif pl1[p1]=='r' and pl2[p2]=='p':
        print("Player 2 Wins")
    elif pl1[p1]=='p' and pl2[p2]=='s':
        print("Player 2 Wins")    
    
pl1={0:'r',1:'p',2:'s'}
pl2={0:'p',1:'r',2:'s'}
while(1):
    n1=input("Player 1 Enter Number String Choice : ")
    n2=input("Player 2 Enter Number String Choice : ")
    bit1=int(input("Player 1, Enter Secret Bit Position : "))
    bit2=int(input("Player 2, Enter Secret Bit Position : "))
    rps(n1,n2,bit1,bit2)
    ch=input("Do you Want to Continue [y/n] : ")
    if (ch=='n'):
        break