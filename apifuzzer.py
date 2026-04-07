import requests # this will allow us to send http request 
import sys # it provides access to variables and functions that incteract closely with interpreter and runtime environment 

'''# step 1 - first we need to send http request to the url ( we will be storing that request in res u can name it anything)

res = requests.get(url=f"http://localhost:3000/rest/products/search?q=") # got this api from owasp juice-shop
print(res) # this give <Response [200]> this means the endpoint is valid 

# step 2 - to get data from the endpoint we wil create a storage name data first to store , since we are trying to get .json so we use 

data =  res.json() # here res is the response variable and .json is the type od data we are trying to get 
print(data)

# this will print the data , so now we need to insert our list to check specific things '''

# step 4 - the loop 

for letter in sys.stdin: # sys.stdin means input from user (here for test we were using words.txt)
    letter = letter.strip()
    res = requests.get(url=f"http://localhost:3000/rest/products/search?q={letter}")
    print(res)
    data = res.json()
    print(data)