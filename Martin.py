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
        print("ok")

#****************   App 3   ****************
elif Choice_Number == "3":
    print("ok")

#****************   App 4   ****************
elif Choice_Number == "4":
    print("ok")

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