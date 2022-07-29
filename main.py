'''
Tasks1: Rezepte anpassen und suchen, Links aktualisieren
Task2: Tag hinzufügen, um bestimmt Rezepte auszusuchen
'''

import random
import webbrowser
import json
import tkinter as tk

import recipes as rc

calculation = "Anzeige der Zutaten"
# Rezepte von recipes.py holen als Objekte
getRecipes = [rc.recipe1, rc.recipe2, rc.recipe3, rc.recipe4, rc.recipe5, rc.recipe6, rc.recipe7,
              rc.recipe8, rc.recipe9, rc.recipe10, rc.recipe11]


def callback(selection):
    global calculation
    calculation = selection


# Nummmern und Namen aller Rezepte laden
def getRecipeNames():
    dictRecipes = {}
    for actLoopRecipe in getRecipes:  # Erstellt Dictionary
        dictRecipes[getattr(actLoopRecipe, "number")] = getattr(actLoopRecipe, "name")
    dictAsString = json.dumps(dictRecipes)  # Dictionary in String
    outputString = dictAsString.replace(",", "\n")  # Zeilenumbruch statt Komma
    showRecipes.config(text=outputString)


def inputCheck(val1):
    try:
        val1 = int(val1)
    except:
        val1 = 100
    return val1

def selectionA():
    val1 = input1.get()
    val1 = inputCheck(val1)

    if val1 < len(getRecipes):
        for actLoopRecipe in getRecipes:
            loopRecipeNumber = (getattr(actLoopRecipe, "number"))  # holt Rezeptnummern aus Liste und vergleicht
            if loopRecipeNumber == val1:
                listAllIngredients = actLoopRecipe.outputIngredients()
                listAsString = "\n".join(listAllIngredients)# Liste als String
                output.config(text=listAsString)


def selectionB():
    global listAsString
    randomRecipes = []
    val1 = input1.get()
    val1 = inputCheck(val1)
    list = random.sample(getRecipes, k=val1)  # speichert zufällige Rezepte, k = Anzahl, speichert als Objekt

    for recipeObject in list:  # holt Namen aus Rezept
        randomRecipes.append(recipeObject.name)
        listAsString = "\n".join(randomRecipes)
    output.config(text=listAsString)


def selectionC():
    val1 = input1.get()
    val1 = inputCheck(val1)

    if val1 < len(getRecipes):
        for getNumber in getRecipes:
            actLoopQuery = (getattr(getNumber, "number"))
            if actLoopQuery == val1:
                webbrowser.open_new_tab(getNumber.link)


def result():
    if calculation == "Anzeige der Zutaten":
        selectionA()
    elif calculation == "zufällige Rezepte":
        selectionB()
    elif calculation == "Rezeptbeschreibungen":
        selectionC()


showRecipeWindow = tk.Tk()
showRecipeWindow.geometry("500x350")

windows = tk.Tk()
windows.geometry("1000x700")

options = ["Anzeige der Zutaten", "zufällige Rezepte", "Rezeptbeschreibungen"]

pasteAsString = tk.StringVar(windows)
pasteAsString.set(options[0])  # Standardauswahl

userSelection = tk.OptionMenu(windows, pasteAsString, *options, command=callback)  # Verweis auf callback()
userSelection.config(font=('Helvetica', 12))
userSelection.grid(row=0, column=0)

label1 = tk.Label(windows, text="Welches Rezept/ wie viele?: ")
label1.grid(row=0, column=1)

input1 = tk.Entry(windows)
input1.grid(row=0, column=2)

output = tk.Label(windows)
output.grid(row=0, column=0)
output.place(relx=0.0, rely=0.5, anchor="sw")

btShowRecipes = tk.Button(windows, text='Ausführen', command=result)
btShowRecipes.grid(row=2, column=1)

btShowRecipes = tk.Button(showRecipeWindow, text='Show Recipes', command=getRecipeNames)
btShowRecipes.grid(row=0, column=0)

showRecipes = tk.Label(showRecipeWindow)
showRecipes.grid(row=1, column=1)

windows.mainloop()
