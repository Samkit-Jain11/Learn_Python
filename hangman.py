# in hangman evey one guess effects the whole round
'''
# part 1 -
# create a greeting 
# create your word list
# randomly choose a word from the list you have created 
# ask the user to guess a letter . (only one time )
# bonus make the program to take the input from user and make it lowercase
# check if the letter is in the word 

import random

print("Hello , Welcome to the Hangman Challenge !")

word = ['chatgpt' , 'nvidia' , 'oracle' , 'nestle']

secret_word = random.choice(word)

guess = input("Guess a alphabet ").lower()

for letter in secret_word:
    if letter == guess:
        print("Present")
    else:
        print("Absent") 

'''

'''
part 2 - 
# create an empty list 
# for each letter in secret word add a "_" that will be printed in the console 
# example if the letter is mango then print should be "_","_","_","_","_"
# if the input letter from user is in word replace "_" with the letter 

import random 

print ("Welcome to the hangman challenge ! ")

word = ['chatgpt' , 'nvidia' , 'oracle' , 'nestle']
secret_word = random.choice(word)

guess = input("Enter an alphabet :").lower()
empty = []

for letter in secret_word:
    if letter == guess:
        empty += letter 
    else:
        empty += "_"


print(empty)

'''

'''
part 3 - 
# use while loop to keep gaming moving until all of the guess are made 

import random
print("Welcome to the hangman challenge ! ")

word = ['chatgpt' , 'nvidia' , 'oracle' , 'nestle']
secret_word = random.choice(word)

game_over = False
guessess = []

while not game_over:
    empty = [] 

    guess = input("Enter an alphabet : ")
    guessess += guess 

    for letter in secret_word:
        if letter in guessess:
            empty += letter
        else :
            empty += "_"
    print (empty)

    if "_" not in empty:
        print("game over , you win ")
        game_over = True 

#logic - 
# the reason we created guessess = [] is to store unput from users
# game_over = False means we are assuming its false
# while not game_over means the condition is run till the game_over becomes true 
#we created empty = [] to store the correct guessess 
# guess takes value of user input 
# guessess += guess (most important) this will store the value of guess 
#for letter in secret_words it means letter will have values of secret_words 
# if letter in guessess : 
# this means the letter what we got from the range if it exist in guessess which is the storage of all input of user 
# empty += letter : sinnce the letter is in guessess it will add that letter in empty 
# else - it will add "_"
# print(empty) means to see the empty list again and agin 
# to break while loop 
# if "_" not in empty : this means the _ should not be there in the list 
# game_over = True : this will break the loop 
'''
'''
# part 4 - add number of attempts used 

import random 
print("Welcome to the hangman challenge ! ")

word = ['chatgpt' , 'nvidia' , 'oracle' , 'nestle']
secret_word = random.choice(word)

game_over = False 
guessess = []
attempt = 0

while not game_over:
    empty = []
    guess = input("Enter an alphabet")
    guessess += guess # this so we can store the guess made by user somewhere it cant get tempered 
    attempt += 1
    for letter in secret_word:
        if letter in guessess :
            empty += letter
            
        else : 
            empty += "_"
             
    
    print(empty)

    if "_" not in empty:
        print("Game over , you win ")
        print (f"Attempt used {attempt}")
        game_over = True
'''
'''
part 5 - add fied numeber of attempts 
'''