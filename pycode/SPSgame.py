#!/usr/bin/python3

import time,random,os
 
t = time.localtime(time.time())
localtime = time.asctime(t)
str = "Current Time:" + time.asctime(t)
 
print(str)
li=['rock',"paper","scissors"]
is_run=True
while is_run:
    is_running=True
    print("Enter your choice")
    print("1.rock\n2.paper\n3.scissors\n4.Exit\n\n")
    op=input('enter : ')
    os.system('clear')
    print()
    py=random.choice(li)
    if op=="1":
        u="rock" 
    elif op=="2":
        u="paper"
    elif op=="3":
        u="scissors"
    elif op=="4":
        print("   Exiting from the game")
        print("   ☺️ Have a nice day ☺️")
        print("        Thank you")
        break
    else:
        print(f"😵 Invalid choice please try again 😵\n\n") 
        is_running=False
    if  is_running:    
          print(f"\n⭐⭐⭐⭐⭐\nYour choice : {u}")       
          print(f"Python choice: {py}\n⭐⭐⭐⭐⭐\n")      
          if (py==u) :
                 print("😑 Tie  the match 😑\n\n" )   
          elif (u=="rock" and py=="scissors")  or   (u=="paper" and py=="rock") or (u=="scissors" and py=="paper"):
                 print("🥳 win the match 🥳\n\n")
          else:
                  print("😞 loose the match 😞\n\n")    
    
    