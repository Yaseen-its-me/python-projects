#!/usr/bin/python3

import time
 
t = time.localtime(time.time())
localtime = time.asctime(t)
str = "Current Time:" + time.asctime(t)
 
print(str)
def show_balance(balance):
    print("Your balance is : rupees ",balance)
def deposit():
    amount=float(input('Enter a amount to be deposited: '))
    if amount<0:
        print("That's not a valid amount")   
        return 0
    else:
        return amount
def withdraw(balance) :
    amount=float(input('Enter amount to be withdrawn: '))   
    if amount> balance:
        print('Insufficient funds')  
        return 0
    elif amount<0:
        print('Amount must be greater than zero: ')
        return 0
    else:
        return amount
def main()  :
    balance=0
    is_running=True
    while is_running:
        print("-----------------\nBanking program\n---------------") 
        print("1. show balance\n2. Deposit\n3. Withdraw\n4. Exit\n--------------------")    
        choice= input("Enter your choice (1-4): ")     
        if choice =="1":
            show_balance(balance)
        elif choice=="2" :
            balance+=deposit()   
        elif choice=="3":
            balance-=withdraw(balance)   
        elif choice=="4":
            is_running=False
        else:
            print("That is not a valid choice")   
    print("Thank you ! Have a nice day")              
if __name__=="__main__" :
    main()        