#### Describe each datatype below:(4 marks)

## 4         = integer (whole number)
## 5.7       = float (decimal number)
## True      = boolean (True or false)
## Good Luck = string (Words or numbers)

#### Which datatype would be useful for storing someone's height? (1 mark)
## Answer - integer

#### Which datatype would be useful for storing someone's hair colour?(1 mark)
## Answer - string


####Create a variable tha will store the users name.(1 mark)
name = input("Enter name: ")
print("Hello", name)

####Create a print statement that will print the first 4 characters of the person's name.(3 marks)
name = input("Enter name: ")
str(name)
print(name[0:4])

####Convert the user's name to all uppercase characters and print the result
name = input("Enter name: ")
print(name.upper())

####Find out how many times the letter A occurs in the user's name
name = input("Enter name: ")
print(name.count("a"))

#### Create a conditional statement to ask a user to enter their age. If they are older than 18 they receive a message saying they can enter the competition, if they are under 18, they receive a message saying they cannot enter the competition.
age = int(input("Please enter your age: "))
if age > 18:
  print("Competition access granted")
elif age < 18:
  print("Competition access denied")

#### Create an empty list called squareNumbers (3 marks)
squareNumbers = []

#### Square numbers are the solutions to a number being multiplied by itself( example 1 is a square number because 1 X 1 = 1, 4 is a square number because 2 X 2 = 4 ). 
###Calculate the first 20 square numbers and put them in the list called squareNumbers. (With loop and .append 10 marks, without, Max 6 marks).
for num in range(21):
  square = num * num
  squareNumbers.append(square)

####Print your list (1 mark)
print(squareNumbers)

####Create a variable called userSquare that asks the user for their favourite square number
userSquare = input("Enter your favourite square number: ")


#### Add this variable to the end of your list called SquareNumbers
squareNumbers.append(userSquare)
print(squareNumbers)

### Create a variable called choice. This variable should choose a random element from your list. Print the variable called choice.(3 marks)
import random
choice = squareNumbers[random.randint(0, 22)]
print(choice)

####Create another print statement that prints tha following output: The random square number is: XX, where XX is where the random square number chosen by the computer.(4 marks)
print("The random square number is", choice, "where", choice, "is the random square number chosen by the computer")