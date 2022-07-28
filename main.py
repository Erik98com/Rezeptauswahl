'''
Aufgabe1: return in getRecipeNames()
Task2: grafische Oberfläche hinzufügen
'''

import recipes as rc
import random
import webbrowser
import tkinter as tk

# Rezepte von recipes.py holen als Objekte
getRecipes = [rc.recipe1, rc.recipe2, rc.recipe3, rc.recipe4, rc.recipe5, rc.recipe6, rc.recipe7,
              rc.recipe8, rc.recipe9, rc.recipe10, rc.recipe11]


# Nummmern und Namen aller Rezepte laden
def getRecipeNames():
    for actLoopRecipe in getRecipes:
        print(getattr(actLoopRecipe, "nummer"), ": ", getattr(actLoopRecipe, "name"))  # in dict. speichern für return


#
def selectionA():
    print("Von welchem Rezept möchten Sie sich die Zutaten anzeigen lassen?")
    userInput = int(input("Bitte geben Sie die Rezeptnummer ein!: "))
    if userInput < 50:
        for actLoopRecipe in getRecipes:
            loopRecipeNumber = (getattr(actLoopRecipe, "nummer"))
            if loopRecipeNumber == userInput:
                return actLoopRecipe.outputIngredients()


def selectionB():
    randomRecipes = []
    userInput = int(input("Wie viele Rezepte möchten Sie auswählen?: "))
    list = random.sample(getRecipes, k=userInput)
    for x in list:
        randomRecipes.append(x.name)
    return randomRecipes


def selectionC():
    print("Von welchem Rezept möchten Sie sich die Rezeptbeschreibung anzeigen lassen?")
    userInput = int(input("Bitte geben Sie die Rezeptnummer ein!: "))
    if userInput < 50:
        for x in getRecipes:
            actLoopQuery = (getattr(x, "nummer"))
            if actLoopQuery == userInput:
                return x.link


print("Folgende Rezepte stehen zur Auswahl:")
getRecipeNames()
print("Was möchten sie tun?")
print("Drücken Sie zur Auswahl den entsprechenden Buchstaben: ")
print("a: Anzeige der Zutaten!")
print("b: Wähle zufällige Rezepte aus!")
print("c: Lassen Sie sich die Rezeptbeschreibung zu einem Ihrer Rezepte geben!")
selectOptionInput = str(input())

if selectOptionInput == "a":  # Zutatenanzeige
    ingredientsList = selectionA()
    print(ingredientsList)

elif selectOptionInput == "b":  # zufällige Rezeptwahl
    randomRecipes = selectionB()
    print(randomRecipes)

elif selectOptionInput == "c":  # Rezeptbeschreibungen nzeigen lassen
    link = selectionC()
    webbrowser.open_new_tab(link)
else:
    print("Eingabe fehlerhaft")
