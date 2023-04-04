######  Q no -----1
num = int(input('Enter a number:-'))
if num % 2 == 0:
    print('Number is divisible by 2')
elif num % 3 == 0:
    print('Number is divisible by 3')
elif num % 5 == 0:
    print ('Number is divisible by 3')
else:
    print('Number is not divisible by 2 & 3 or 5')

num = int(input('Enter a number:-'))
if num % 2 == 0 and num % 3 == 0:
    print('Both number is divisible by 2 & 3')
elif num % 2== 0 and  num % 5 == 0:
    print ('Both number is divisible by 2 & 5')

elif num % 3== 0 and  num % 5 == 0:
    print ('Both number is divisible by 3 & 5')

elif num % 2== 0 and  num % 3 == 0 and num % 5 == 0:
    print ('Both number is divisible by 2 & 3 & 5')