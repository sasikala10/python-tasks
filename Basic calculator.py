# writing a python program for simple calculator
print("choose an number from 1 to 4 to perform the operation")
print("1.Add")
print("2.subtraction")
print("3.multiplication")
print("4.division")
print("5.factorial")
value =int(input("enter your option:"))


if(value in [1,2,3,4,5]):

    num1 = int(input("enter first number"))
    num2 = int(input("enter second number"))
    if(value ==1):
     result=num1+num2
     print(result)

    elif(value ==2):
     
     result=num1-num2
     print(result)

    elif(value ==3):
     result=num1*num2
     print(result)
    elif(value ==4):
     result=num1//num2
     print(result)
    
    elif(value ==5):
     s=1
     for i in range(1,num1+1):
       s=s*i
    print(s)
     
else: 
    print("you have not chosen from 1 to 5")      


   

    

