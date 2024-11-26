"""
Day 3 Challenge:

👉 Day 3 Challenge

The Ultimate Wacky Recipe Maker

We have learned enough skills for a simple, but cool, project!

Remember when you were a kid and thought the ideal dinner would just be all your favorite things mixed in a bowl? How did that Nutella Mac & Cheese taste? Well - let's come up with a recipe generator to build us an amazing dish for today's evening meal!

You will need to:

Create these as a variable:
A type of food
A type of plant
A method of cooking
A word to describe burned food
A household item
2. Output a nice looking Recipe page that *concatenates* a dish in this format:
cooking food with burned plant on a bed of item
Example (No Peeking the Solution Yet):

Name a food > Mac & Cheese
Name a type of plant > Cactus
Name a method of cooking > Saute        
What word describes burned food? > Ruined
Name a DIY item > Hammer
MENU
Saute Mac & Cheese with Ruined Cactus on a bed of Hammers
EXTRA: Remix your recipe to include more variables and a wackier type of dish.

Why not step it up and create a recipe for a starter, main course and dessert?

"""

#Step_1 let's create the variables

food = "Mac & Cheese"
plant = "Cactus"
cooking_method = "Saute"
syn_burned = "Ruined"
hh_tool = "Hammers"
pie = "Apple Pie"
#Extra: I'm going to use apple pie as a dessert. 


print("MENU\n", cooking_method, food,"with",syn_burned, plant,"on a bed of",hh_tool, "and for dessert we have", pie, "or we can order you a pizza, if that's to your liking")

#The Actual Solution - I was trying to mimic the output and not use the input function as described in the lesson. 

food = input("Name a type of food: ")
plant = input("Name a plant: ")
cookingType = input("What is a way to cook something? ")
burntFood = input("How do you describe burnt food? ")
householdItem = input("Name something in your house: ")

print()
print("Tonight's dinner:")

print("For dinner you should make", cookingType, food, "with", burntFood, plant, "on a plate of", householdItem)