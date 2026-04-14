'''def hello():
    print("Hello World")

hello() '''

'''name = input("Enter your name : ")

def n_print(name):
    print(f"Hello , {name}")

n_print(name)'''

'''ip = input("Enter the ip of the target : ")

def attack(ip):
    print(f"Attacking {ip}")

attack(ip )'''

'''# ip = "10.10.10.10"

def attack (i , d):
    print(f'ip is {i} and domain is {d}')

#attack(ip) # here we are calling attack function with the parameters ip 
# even if the ip initially is not defined we can define it later when we are calling attack 

ip = '10.10.10.10'
url = "domain.com"

attack(ip , url)'''

# print paramter of a rectangle or sqaure using functions 

def formula(l,b):
    answer = l*b
    print(f'the parameter is {answer}')

a = int(input("Enter the length "))
b = int(input("Enter the bredth "))

formula(a,b)