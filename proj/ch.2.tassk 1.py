# Task 1 == Ask user to input 3 numbers and you havr to print average of 3 number
#using string formatting
#Bonous=Try to take all three comma separate inputs in one line
num1=input("print the first number=")
num2=input("print the second number=")
num3=input("print the third number=")
num1,num2,num3 =input("enter three number comma separated:").split(",") 
      #(int(num1)+int(num2)+int(num3))/3
print(f"average of three number : {(int(num1) + int(num2) + int(num3)) / 3}")