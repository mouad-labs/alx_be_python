import random
secret_number = random.randint(1, 100)
guess = False
attempts = 0


while guess == False:
 guess = int(input("I'm thinking of a number between 1 and 100. Can you guess it?"))
 match guess:
    case guess if guess < secret_number:
        print ("Nope, your guess is a bit low. Give it another shot!")
        guess = False
    case guess if guess > secret_number:
        print ("Oops, your guess is a bit high. Try again!")
        guess = False
    case guess if guess == secret_number:
     print ("Congratulations, you guessed it!")  
     guess = True 



 
    



    
          