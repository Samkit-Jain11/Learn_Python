# if the number is divisible by 3 , print fizz 
# if the number is divisible by 5 , print buzz 
# if the number is divisible by both , print fizzbuzz 

'''
when user enter a number :
a = int(input("Enter your number : "))

if a%3==0 and  a%5!=0:
    print("fizz")
elif a%3!=0 and  a%5==0:
    print('buzz')
elif a%3==0 and  a%5==0:
    print('fizzbuzz')
else: 
    print("not divisible by both ")
'''

'''
method 2 
for i in range(1,101):
    if i%3==0 and i%5==0:
        print("fizzbuzz")
    elif i%3==0:
        print('fizz')
    elif i%5==0:
        print('buzz')
    else:
        print(i)'''