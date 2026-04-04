# create a greeting 
# create your word list randomly choose a word from the list you have created 
# ask the user to guess a letter 
# bonus make the program to take the input from user and make it lowercase
# check if the letter is in the word 

import random 

print("Welcome to the hangman challenge ! ")

word = ['apple' , 'mango' , 'banana' , 'strawberry' ]

secret_word = random.choice(word) # here .choice is a function provided my random module which will allow us to get a random word choice from the list 
print(secret_word)
guess = input("Guess a letter : ").lower() # here the the letter we guess will be convertet lower case because of .lower() 
print(guess)

for letter in secret_word: # since we are required to check the inpput from user in radom word thats why we used secret_word 
    if letter==guess: # lets assume the secret_word is mango so the loop will use m , a , n , g , o as a letter to try in this loops 
        print("Right")
    else:
        print("wrong")