num_1 = float(input("enter the number:-"))
choice = input("Enter the operation: ")#### + - * 
num_2 = float(input("enter the another number:-"))
if choice == "+":
    sum = num_1 + num_2
    print("The sum is ",sum)
elif choice =="-":
    diff = num_1 - num_2
    print("The difference is ",diff)
elif choice =="*":
    mul = num_1 * num_2
    print("The product is ",mul)
elif choice =="/":
    div = num_1 / num_2
    print("The difference is ",div)
else:
    print("Invalid choice")

