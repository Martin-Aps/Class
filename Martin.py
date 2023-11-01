#***************************   Welcome Message&Tabel of Contents   ***************************

print("***Welcome to MARTIN's App***\n")
Content=['Multiplication Table','Prime Number','Guess','URL','Max,Min,Average','Rock paper scissor','Stopwatch']
for Line_Number in range(len(Content)):
    print(Line_Number+1, Content[Line_Number])
Choice_Number = input("\nEnter desired number: ")

#***************************   Main Code   ***************************
from statistics import mean
import random

#****************   App 1   ****************
if Choice_Number == "1":
    num1=1
    while num1<11:
        num2=1
        while num2<11:
            print(num1*num2 , end='\t')
            num2 +=1
        print()
        num1 +=1
    
#****************   App 2   ****************    
elif Choice_Number == "2":
        
    try:
        Numbers=[]
        Max_num=int(input("Please Enter Max Number: "))
        for n in range(2,Max_num+1):
            is_prime=True
            for m in range(2,n):
                if n % m ==0:
                    is_prime=False
                    break
            if is_prime:
                Numbers.append(n)
        print(Numbers)
    
    except:
        print("Make a Mistake ") 

#****************   App 3   ****************
elif Choice_Number == "3":
    try:
        Number=int(input("Select a Number from 100 to 10.000: "))
        Score=1000
        if 100<=Number<=10000 :
            while Score>0:
                Guess=random.randint(100,10001)
                print(Guess)
                if Guess > Number:
                    print("boro pain")
                    Score -=1
                    print(Score)
                if Guess < Number:
                    print("boro bala")
                    Score -=1
                    print(Score)
                if Guess==Number:
                    print("ok")
                    break
        else:
            print("add dorost")
    except:
        print("Dorost")

#****************   App 4   ****************
elif Choice_Number == "4":
    URL=input('URL: ')
    Url_Split=URL.split(":")

    print(f'Schem: {Url_Split[0]}')
    URL=URL.replace('http://',"").replace('https://',"")
    URL=URL.replace('www.',"")
    Url_Split=URL.split(".")
    print(f'Domain: {Url_Split[0]}')
    print(f'Extention: {Url_Split[1]}')

#****************   App 5   ****************
elif Choice_Number == "5":
    User_input=int(input('Please Enter Numbers (-1 at End): '))
    Numbers_List=[User_input]
    while True:
        if User_input>0:
            User_input=int(input('Please Enter Numbers (-1 at End): '))
            Numbers_List.append(User_input)
        elif User_input<0 :
            Numbers_List.remove(-1)
            break
    print(f'Max of Numbers: {max(Numbers_List)} \nMin of Numbers: {min(Numbers_List)} \nAverage of Numbers: {mean(Numbers_List)}')


#****************   App 6   ****************
elif Choice_Number == "6":
    Game_List=['Stone','Paper','Scissor']
    Comp_Choice=random.choice(Game_List)
    User_Choice=input("Please Select from Stone Papaer Scissor: ").capitalize()
    print(f'You Choice--->{User_Choice}')
    print(f'Comp Choice--->{Comp_Choice}')
    if User_Choice in Game_List:
        if User_Choice == Game_List[0] and Comp_Choice == Game_List[0]:
            print('****Tie!****')
        elif User_Choice==Game_List[0] and Comp_Choice==Game_List[1]:
            print('****Comp Win!****')
        elif User_Choice==Game_List[0] and Comp_Choice==Game_List[2]:
            print('****You Win!****')
        elif User_Choice==Game_List[1] and Comp_Choice==Game_List[0]:
            print('****You Win!****')
        elif User_Choice==Game_List[1] and Comp_Choice==Game_List[1]:
            print('****Tie!****')
        elif User_Choice==Game_List[1] and Comp_Choice==Game_List[2]:
            print('****Comp Win!****')
        elif User_Choice==Game_List[2] and Comp_Choice==Game_List[0]:
            print('****Comp Win!****')
        elif User_Choice==Game_List[2] and Comp_Choice==Game_List[1]:
            print('****You Win!****')
        elif User_Choice==Game_List[2] and Comp_Choice==Game_List[2]:
            print('****Tie!****')
    else:
        print('Make a Mikstake!')
        

#****************   App 7   ****************
elif Choice_Number == "7":
    print("Under Construction! :)))))")    