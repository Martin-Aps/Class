#***************************   Welcome Message&Tabel of Contents   ***************************

print("***Welcome to MARTIN's App***\n")
Content=['Multiplication Table','Prime Number','Guess','URL','Max,Min,Average','Rock paper scissors','Stopwatch']
for Line_Number in range(len(Content)):
    print(Line_Number+1, Content[Line_Number])
Choice_Number = input("\nEnter desired number: ")

#***************************   Main Code   ***************************

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
if Choice_Number == "2":
    print("ok")

#****************   App 3   ****************
if Choice_Number == "3":
    print("ok")

#****************   App 4   ****************
if Choice_Number == "4":
    print("ok")

#****************   App 5   ****************
if Choice_Number == "5":
    print("ok")

#****************   App 6   ****************
if Choice_Number == "6":
    print("ok")

#****************   App 7   ****************
if Choice_Number == "7":
    print("ok")    