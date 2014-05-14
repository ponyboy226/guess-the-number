import random
# Count the number of guess you have taken
guessLeft = 1
guessesTaken=0
totguess=5

print'Hello! What is your name?'
myName=raw_input()

# Generate a random number
number=random.randint(1,20)
print'Guess which number I\'m thinking of....1 to 20.\n\
You only have 5 tries so make them good!\n\
What number do you feel lucky with?'
    
while totguess > 0:
    totguess -= 1
    guess = raw_input()
    guess = int(guess)
        
    if guess < number:
        totguess = str(totguess)
        print'I guess it wasn\'t that lucky, you have ' + totguess + ' more guesses'
        totguess = int(totguess)        
        print'\t*Hint*  You\'re number is too low'
        guessLeft += 1
        
    if guess > number:
        totguess = str(totguess)
        print'I guess it wasn\'t that lucky, you have ' + totguess + ' more guesses'
        totguess = int(totguess)        
        print'\t*Hint*  You\'re number is too high'
        guessLeft += 1
        
    if guess == number:
        break            

if guess == number:
    number = str(number)
    guessLeft = str(guessLeft)
    print'That\'s it, '+myName +'!  How did you know I was thinking of ' + number +'? It only took ' + guessLeft + ' guesses too'
else:
    guessesTaken = str(guessesTaken)
    number = str(number)
    print myName + ', you dumbass.  You have ' + guessesTaken + ' guesses left.  Which means I win.\ I was thinking of the number ' + number   
