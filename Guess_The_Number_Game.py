import random
import os

while True:
    ans = random.randint(1,100)
    moves = 0
    Total_moves = 10
    flag = 0
    print("\n\t\t***Guess The Number Game***\n\n")
    print("RULES :")
    print("\n1. You have to Guess the Number which lies between 1 to 100 both inclusive.")
    print("2. At Each Wrong Guess, Game gives you a hint to Guess the Number.")
    print("3. You have only " + str(Total_moves) + " Moves to Find The Correct Number.")
    print("4. You have to find the Number in Minimum Possible Moves.\n\n")

    for i in range(1 , Total_moves + 1):
        guess = int(input("\nTry number " + str(i) + "  :: Guess The Number : "))
        moves += 1
        if guess == ans:
            print("Congratulations, You Won! Your Guess is Correct Number and You have a Genius Mind!!!")
            print("You have Guessed the Number is just " + str(moves) + " Moves.")
            flag = 1
            break

        elif guess > ans:
            print("Hint : The Correct Number is smaller than Your Guess( " + str(guess) + " ).")
            print("Try again!")

        elif guess < ans:
            print("Hint : The Correct Number is larger than Your Guess( " + str(guess) + " ).")
            print("Try again!")

    if flag == 0:
        print("Ohh,You Lost!")

    while True:
        var = input("\n\n   Do You want to play one more game. <y/n>:")
        if var != 'y' and var != 'Y' and var != 'n' and var != 'N':
            print("Invalid choice! choose again.")
        else:
            break

    if var == 'n' or var == 'N':
        break
    else:
        os.system('cls')


print("\n\n   Okh Bye Bye! See you again.")
