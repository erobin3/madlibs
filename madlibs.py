"""
Description: This program will prompt the user to input nouns, adjectives, and more in order to complete the story.
Author:  Erika Robinson
"""

# The template for the story

story = "This morning %s woke up feeling %s. 'It is going to be a %s day!' Outside, a bunch of %s's were protesting to keep %s in stores. They began to %s to the rhythm of the %s, which made all the %s's very %s. Concerned, %s texted %s, who flew %s to %s and dropped %s in a puddle of frozen %s. %s woke up in the year %s, in a world where %s's ruled the world."

#Tell the user the mad lib is starting
print ("The Mad Lib has started")

#Ask user to input a name for the story
name = input("Enter a name: ")

#Ask user to input 3 adjectives for the story
adj1 = input("Enter an adjective: ")
adj2 = input("Enter a second adjective: ")
adj3 = input("Enter one more adjective: ")

#Ask user to input a verb
verb = input("Enter a verb: ")

#Ask user to input 2 nouns
noun1 = input("Enter in a noun: ")
noun2 = input("Enter in another noun: ")

#Ask the user to input one of each of the following: animal, food, fruit, superhero, countru, dessert, and year.

animal = input("Enter an animal: ")
food = input("Enter a food item: ")
fruit = input("Enter a fruit: ")
hero = input("Enter a superhero: ")
country = input("Enter a country: ")
dessert = input("Enter a dessert: ")
year = input("Enter a year: ")

#Print where the user inputs will go into the story
print (story % (name, adj1, adj2, animal, food, verb, noun1, fruit, adj3, name, hero, name, country, name, dessert, name, year, noun2))