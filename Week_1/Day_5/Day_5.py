#Day 5 - If statements
"""
slide_1


If Statements

These statements are a bit like asking a question. You are telling the computer: 
if something is true, then do this specific block of code. 
Double equals (==) is asking the computer to compare if these two things are exactly the same.

 

In the code below, I am asking if the variable myName is the same as the string David.

myName = input("What's your name?: ")
if myName == "David":
But that doesn't print anything?

To create a print statement related to the input from the if statement, 
you must go to the next line and indent once (Luckily, Replit does this for you, 
but be careful!) so it is all a part of the code we run.

👉 Copy this code and see what happens.

myName = input("What's your name?: ")
if myName == "David":
  print("Welcome Dude!")
What is else?

If the condition is not met with the if statement, then we want the computer to do the else part 
instead. Likewise, if the condition is met in the if statement, 
then the else bit is ignored by the computer. 
The else statement must be the first thing unindented after the if statement and in 
line with it (Replit helps you out here too!)

👉 Copy this code and give it a go. Watch those indents!

myName = input("What's your name?: ")
if myName == "David":
 print("Welcome Dude!")
 print("You're just the baldest dude I've ever seen")
else:
 print("Who on earth are you?!")

"""

"""
slide_2

Common Errors

First, delete any other code in your main.py file. 
Copy each code snippet below into main.py by clicking the copy 
icon in the top right of each code box. Then, hit run and see what errors occur. 
Fix the errors and press run again until you are error free. 
Click on the 👀 Answer to compare your code to the correct code.

Syntax Error

👉 What is wrong with this code below?

catsOrDogs = input("Are you a cat person? Or a dog person?: ")
if catsOrDogs = "cat":
  print("Meow")
else:
  print("Woof")
Syntax Error...again

👉 What is wrong with this code?

catsOrDogs = input("Are you a cat person? Or a dog person?: ")
if catsOrDogs == "cat"
  print("Meow")
else:
  print("Woof")
Indentation Error

👉 Do you see the error here?

catsOrDogs = input("Are you a cat person? Or a dog person?: ")
if catsOrDogs == "cat":
  print("Meow")
else:
print("Woof")

"""
"""
slide 3

Fix My Code

👉 Try and fix this code which is full of errors.

First, delete any other code in your main.py file. 
Copy each code snippet below into main.py by clicking the copy icon in the top right of each code box.
 Then, hit run and see what errors occur. 
 Fix the errors and press run again until you are error free. 
 Click on the 👀 Answer to compare your code to the correct code.

drink = input("Do you prefer coffee or tea?)
if drink = "coffee"
  print("Tea is better.")
    else:
  print("Excellent choice.")
"""

"""
slide_4

 👉 Day 5 Challenge

"Which character are you?" Generator

You will need to:

Ask your users a series of questions that identify if they're one of the characters 
in the world you have created.
Add multiple if statements to check the result of each question.
Make sure to have a final print if they haven't selected any of the characters so far.
Example

Marvel Movie Character Creator
--
Do you like 'hanging around'?: No
Then you're not Spider-man
Do you have a 'gravelly' voice?: No
Aww, then you're not Korg
Do you often feel 'Marvelous'?: Yes
Aha! You're Captain Marvel! Hi!


"""

#Marvel Character Creator

# My Solution
spider = input("Do you like hanging around? (Yes/No): ")
if spider == "Yes":
    print("Then you are Spider-Man!")
else:
    korg = input("Do you have a gravelly voice? (Yes/No): ")
    if korg == "Yes":
        print("Then you are Korg!")
    else:
        captain = input("Do you feel marvelous? (Yes/No): ")
        if captain == "Yes":
            print("Then you are Captain Marvel!")
        else:
            print("You Suck!")


#Replit Solution

"""
print("Which character are you from 'Avengers?'")
print()
print("Answer these questions and let's find out.")
print()
print("Please use Y or N for yes and no.")

likeGreen = input("Do you like the color green?: ")
if likeGreen == "Y":
  print("You must be the Hulk!")
IronIsCool = input("Do you think building robots is cool?: ")  
if IronIsCool == "Y":
  print("You must be Iron Man. Cool suit!")
TimeTravel = input("Do you like traveling through time?: ")  
if TimeTravel == "Y":
  print("You must be Captain America!")
Strong = input("Are you super strong?: ")
if Strong == "Y":
  print("You have got to be Thor!")
else:
  print("I guess you are not like anyone from 'Avengers.'")
"""