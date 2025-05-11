#Converting Temperatures between celsius,fahrenheit and kelvin
print("choose option from 1 to 4")
print("1.celsius to fahrenheit")
print("2.fahrenheit to celsius")
print("3.celsius to kelvin")
print("4.kelvin to celsius")
print("5.Fahrenheit to kelvin")
print("6.Kelvin to Fahrenheit")
option=int(input("Enter your option: "))
if(option in [1,2,3,4,5,6]):
    #converting celsius to fahrenheit
    if(option==1):
        celsius=int(input("Enter celsius:"))
        f=(celsius*9/5)+32
        print("converting", celsius,"C to fahrenheit is:",f,"F")
        #converting fahrenheit to celsius
    elif(option==2):
        fahrenheit=float(input("Enter fahrenheit value:"))
        c=(fahrenheit-32)*5/9
        print("converting",fahrenheit,"F to celsius is: ",c,"C")
        #converting celsius to kelvin
    elif(option==3):
     celsius=int(input("Enter celsius value: "))
     k=celsius+273.15
     print("converting",celsius,"C to kelvin is:",k,"K")
     #converting kelvin to celsius
    elif(option==4):
       kelvin=int(input("Enter kelvin value: "))
       c=kelvin-273.15
       print("converting",kelvin,"K to celsius is: ",c,"C")
       #converting fahrenheit to kelvin
    elif(option==5):
       fahrenheit=float(input("Enter fahrenheit value: "))  
       k=(fahrenheit-32)*5/9+273.15
       print("converting",fahrenheit,"F to kelvin is: ",k,"K")
       #converting kelvin to fahrenheit
    elif(option==6):
       kelvin=int(input("Enter kelvin value: "))   
       f=(kelvin-273.15)*9/5+32
       print("converting",kelvin,"K to fahrenheit is: ",f,"F")

else:
  print("Invalid number")
