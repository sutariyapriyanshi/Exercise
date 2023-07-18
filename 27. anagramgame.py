import random # for taking random word from the words and also doing scrambling of the words in random manner
words=["ironman","thor","hawkeye","wanda","vision","keyword","married","blindly","mission","space","desktop","hoverboard"]
word=random.choice(words) # here word is the variable choosing any random word from the words
# print(word) 

jumble="".join(random.sample(word,len(word))) # to jumble means to scramble the word  this is used
# it is empty taking the random letter from the desire word till the length is complete
# print(jumble)

chances=5 # you are having 5 chances
print(" -----------------------------------------------------------------------------------------------------------------------------------------")
print("|                                                       Anagram Game                                                                     |")
print(" -----------------------------------------------------------------------------------------------------------------------------------------")
while (chances!=0): # iterate this loop until your chance is 0
    print("\nThe word is",jumble) # print the scrable word here
    guess=input("\nEnter your guess word: ").lower() # it will taking user input and convert into the lower case
    if (guess==word): # if the your guess and word is both are equal then you will win
        print("\nCorrect guess !!\n\nYou won!")
        quit() # and quit after that
    else: 
        chances-=1 # otherwise decrease the chanv=ce of the player with 1 
        print("\nIncorrect guess!!") 
        print("\nRemaining chances are:", chances) # also print the remaing chance so user be aware
else:
    print("All your chances are exhausted!!") # if the none of the guess is the right then print this
    print("You lost!!")
    print("\nThe correct word is",word)

print("\nThank you")
