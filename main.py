import random
# userReply = input("Do you need to ship a package? (Enter yes or no) ")
# if userReply == "yes":
#     print("We can help you ship that package!")
# else:
#     print("Please come back when you need to ship a package. Thank you.")

# userReply = input("Would you like to buy stamps, buy an envelope, or make a copy? (Enter stamps, envelope, or copy) ")
# if userReply == "stamps":
#     print("We have many stamp designs to choose from.")
# elif userReply == "envelope":
#     print("We have many envelope sizes to choose from.")
# elif userReply == "copy":
#     copies = input("How many copies would you like? (Enter a number) ")
#     print("Here are {} copies.".format(copies))
# else:
#     print("Thank you, please come again.")

number = random.randint(1,10)
isGuessRight = False
print("-> ",str(number))
while isGuessRight != True:
    guess = input("Guess a number between 1 and 10: ")
    if int(guess) == number:
        print("You guessed {}. That is correct! You win!".format(guess))
        isGuessRight = True
    else:
        print("You guessed {}. Sorry, that isn’t it. Try again.".format(guess))

