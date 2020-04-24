#importing the time  module
import time


#welcoming the user
name =input(" Enter name of the Player : \n")

print ("Hello, " + name, "Time to play hangman!")

print ("")

#wait for 1 second
time.sleep(1)
print("")

print(" _____   ")
print("|     |  ")
print("|     O  ")
print("|    /|\  " )
print("|    / \  " )
print("|   ______ ")
print("|  HANGMAN ")

time.sleep(1.5)

print("Select Difficulty Level : \n")
print("1. Easy \n")
print("2. Medium \n")
print("3. Difficult \n")
choice=int(input())

if choice==1 :
#Hint for the word to guess
    print("Word Hint :- Most commonly used coding language")

    #here we set the word for hint
    word="python"
                           
elif choice==2:
    print("Word Hint :- Name of the Player who is known as 'God of Cricket' ")
    #here we set the word for hint
    word="sachin"

elif choice==3:
    print("Word Hint :- The first person from India to have 50 million followers on Instagram ")
    #here we set the word for hint
    word="viratkohli"

time.sleep(2.0)
print("")
print("So Here you Go.....!!!!")


print ("Start guessing...")
time.sleep(0.5)

               

#creates an variable with an empty value
guesses = ''

#determine the number of turns
turns =len(word)

# Create a while loop

#check if the turns are more than zero
while turns > 0:         

    # make a counter that starts with zero
    failed = 0             

    # for every character in secret_word    
    for char in word:      

    # see if the character is in the players guess
        if char in guesses:    
    
        # print then out the character
            print (char,end=' '),    

        else:
    
        # if not found, print a dash
            print ("_",end=' '),     
       
        # and increase the failed counter with one
            failed += 1    

    # if failed is equal to zero

    # print You Won
    if failed == 0:
        time.sleep(1)
        print('')
        
        print ("You won")

        print(" _____   ")
        print("|     |  ")
        print("|        ")
        print("|     O  ")
        print("|    /|\ ")
        print("|____/_\______  " )
        print("  YOU SAVED ME "+name)

    # exit the script
        break              
    print('')

    # ask the user go guess a character
    guess =input("guess a character: ") 

    # set the players guess to guesses
    guesses += guess                    

    # if the guess is not found in the secret word
    if guess not in word:  
 
     # turns counter decreases with 1 (now 9)
        turns -= 1        
 
    # print wrong
        print ("Oops..!! Wrong")    
 
    # how many turns are left
        print ("You have", + turns, 'more guesses') 
 
    # if the turns are equal to zero
        if turns == 0:           
    
        # print "You Lose" 
            
            print(" ______   ")
            print("|      |  ")
            print("|      O  ")
            print("|    /|\  " )
            print("|    | |  " )
            print("|__________ ")
            print ("You Killed me "+name,"\n Looser !!!!" ) 
