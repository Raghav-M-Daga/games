# Guess the number
print("This number is between 0 and 100")
import random
ran = int(random.randint(0,100))
print("You need to guess the number")
g1 = int(input('What is your guess: ' ))
loopcount = 0

while (g1 != ran and loopcount != 10):
 loopcount = loopcount + 1

 if g1 > ran:
   print("Your guess is greater than the number")
   g1 = int(input("What is your next guess: "))

 elif g1 < ran:
   print("Your guess is lesser than the number ")
   g1 = int(input("What is your next guess: "))


if loopcount < 10:
  print("You have guessed correctly!")
  print("The number was",ran)
  print("You made only",loopcount,"guesses")
else:
    print("You have lost the game. You made more than 10 guesses")
    print("The number was",ran)
    print("Better luck next time")
