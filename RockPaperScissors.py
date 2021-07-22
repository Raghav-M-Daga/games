#rock paper scissors by Raghav M Daga
import random
list = ["r","p","s"]
comp = 0
player = 0
print("This is  a game of Rock-Paper-Scissors")
print("Type 'r' for rock, 'p' for paper and 's' for scissors")

while (comp != 5 and player != 5):
 var = int(random.randint(0, 2))
 x = input("What do you choose: ")
 y = list[var]
 print("The computer has chosen",y)
 if x == y:
     print("No one has won the point")
 elif x == 'r' and y == 's':
     print("You have won the point")
     player = player + 1
 elif y == 'r' and x == 's':
     print("Computer has won the point")
     comp = comp + 1
 elif x == 'p' and y == 's':
     print("Computer has won the point")
     comp = comp + 1
 elif y == 'p' and x == 's':
     print("You have won the point")
     player = player + 1
 elif x == 'p' and y == 'r':
     print("You have won the point")
     player = player + 1
 elif y == 'p' and x == 'r':
     print("Computer has won the point")
     comp = comp + 1
 else:
     print("Sorry, wrong input. Please type in only 'p', 's', 'r'")
 print("Computer", comp)
 print("Player:", player)
if comp > player:
   print("Sorry you have lost. The computer has beaten you. Better luck next time")
else:
    print("Congratulations! You have won the game")
