class recipes:
    def __init__(self, name, number, link, ingredient1="None", ingredient2="None", ingredient3="None",
                 ingredient4="None", ingredient5="None", ingredient6="None", ingredient7="None", ingredient8="None",
                 ingredient9="None", ingredient10="None", ingredient11="None", ingredient12="None", ingredient13="None",
                 ingredient14="None", ingredient15="None"):
        self.name = name
        self.number = number
        self.link = link
        self.ingredient1 = ingredient1
        self.ingredient2 = ingredient2
        self.ingredient3 = ingredient3
        self.ingredient4 = ingredient4
        self.ingredient5 = ingredient5
        self.ingredient6 = ingredient6
        self.ingredient7 = ingredient7
        self.ingredient8 = ingredient8
        self.ingredient9 = ingredient9
        self.ingredient10 = ingredient10
        self.ingredient11 = ingredient11
        self.ingredient12 = ingredient12
        self.ingredient13 = ingredient13
        self.ingredient14 = ingredient14
        self.ingredient15 = ingredient15

    def outputIngredients(self):
        ingredientList = [
            self.ingredient1, self.ingredient2, self.ingredient3, self.ingredient4, self.ingredient5,
            self.ingredient6, self.ingredient7, self.ingredient8, self.ingredient9, self.ingredient10,
            self.ingredient11, self.ingredient12, self.ingredient13, self.ingredient14, self.ingredient15
        ]
        while "None" in ingredientList:
            ingredientList.remove("None")
        return ingredientList


recipe1 = recipes("Schweinelachssteak mit Bohnengemuese", 1,
                  "https://www.hellofresh.de/recipes/schweinelachssteak-mit-bohnengemuse-6088ef23ea839124067e8909?isMegaAddonsEnabled=false&subscriptionId=2033884",
                  "Kartoffeln", "Schweinelachssteak", "Buschbohnen",
                  "1 Knoblauchzehe", "Petersilie", "Thymian")

recipe2 = recipes("Schweinefilet mit Honig-Thymian-Sosse", 2,
                  "https://www.hellofresh.de/recipes/schweinefilet-mit-honig-thymian-sosze-607685f116bd96129062106f?isMegaAddonsEnabled=false&subscriptionId=2033884",
                  "Schweinefilet", "1 Suesskartoffel", "Buschbohnen",
                  "1 Knoblauchzehe", "1-2 Zwiebeln", "Thymian", "Honig", "Gemuesebruehe")

recipe3 = recipes("Koenigsberger Klopse", 3,
                  "https://www.hellofresh.de/recipes/konigsberger-klopse-606c3bec1f54574ed636390d?isMegaAddonsEnabled=false&subscriptionId=2033884",
                  "gemischtes Hackfleisch", "Worcester Sauce", "Zwiebel",
                  "mittelscharfer Senf", "Semmelbrösel", "Kochsahne", "Kapern", "Brokkoli", "festk. Kartoffeln",
                  "Rinderbruehe")

recipe4 = recipes("Haehnchen-Reis-Pfanne", 4,
                  "https://www.rewe.de/rezepte/haehnchen-reis-pfanne/",
                  "Jasminreis", "Mandeln", "rote Zwiebel", "Karotte", "Fruehlingszwiebel"
                  "Haehnchenbrustfilet", "Huehnerbruehe", "TK- Erbsen", "Zitrone", "Zaziki")

recipe5 = recipes("Haehnchenbrustfilet in Honig- Zitronen- Marinade", 5,
                  "https://www.hellofresh.de/recipes/hahnchenfilet-in-honig-zitronen-marinade-609135ba6a1e732a0450aed6?isMegaAddonsEnabled=false&subscriptionId=2033884",
                  "Buschbohnen", "Knoblauchzehe", "Honig", "Kartoffeln", "Zitrone",
                  "Sahnejoghurt")

recipe6 = recipes("Haehnchenpfanne suess-sauer", 6,
                  "https://www.hellofresh.de/recipes/hahnchenpfanne-suszsauer-6076862cd41e9264426be050?isMegaAddonsEnabled=false&subscriptionId=2033884",
                  "Jasminreis", "Frühlingszwiebel", "Zwiebel", "Sesam", "Ketchup", "rote Paprika",
                  "Sojasoße", "Rotweinessig", "Maisstärke", "Aprikosenchutney", "Gemüsebrühe", "Honig")

recipe7 = recipes("Lachsfilet in Teriyakisosse", 7,
                  "https://www.hellofresh.de/recipes/lachsfilet-in-teriyakisosze-606c3c5a04bcb70c26451f39?isMegaAddonsEnabled=false&subscriptionId=2033884",
                  "Lachsfilet", "Frühlingszwiebel", "Teriyakisoße", "Basmatireis",
                  "Limette", "Babyspinat", "Sesam", "Avocado")

recipe8 = recipes("Gebratene Schweinemedaillons in Zwiebelsosse", 8,
                  "https://www.hellofresh.de/recipes/gebratene-schweinemedaillons-60522dbfab52603be9783a78?isMegaAddonsEnabled=false&subscriptionId=2033884",
                  "Schweinefilet", "rote Zwiebel", "Kartoffeln",
                  "Kochsahne", "Honig", "Karotte", "Rinderbrühe", "Schnittlauch")

recipe9 = recipes("Seelachsfilet in Kraeutermarinade", 9,
                  "https://www.hellofresh.de/recipes/pikantes-seelachsfilet-an-krautermarinade-6050db7f9606d85bfb3260d0?isMegaAddonsEnabled=false&subscriptionId=2033884",
                  "Seelachs", "Gewürzmischung Grünzeug", "Zucchini",
                  "Sonnenblumenkerne", "Kartoffeln", "Aioli", "Joghurt", "Frühlingszwiebel", "rote Chillischote")

recipe10 = recipes("Schwedische Frikadellen mit Kartoffelstampf", 10,
                   "https://www.hellofresh.de/recipes/schwedische-frikadellen-mit-kartoffelstampf-6033e641817ff1395b66b77e?isMegaAddonsEnabled=false&subscriptionId=2033884",
                   "Karotte", "mehligk. Kartoffeln", "Zwiebeln",
                   "Rinderhackfleisch", "Wildpreiselbeermarmelade", "Muskatnusspulver", "Rinderbrühe",
                   "mittelscharfer Senf", "Semmelbrösel")

recipe11 = recipes("Schnitzel in Zwiebel- Pfeffer- Sosse", 11,
                   "https://www.hellofresh.de/recipes/schnitzel-mit-zwiebel-pfeffer-sosze-6023a4553b5d0c6f07440634?isMegaAddonsEnabled=false&subscriptionId=2033884",
                   "Schweineschnitzel", "Semmelbrösel", "Kampot Pfeffer",
                   "Brokkoli", "Zwiebel", "festk. Kortoffeln", "Hühnerbrühe", "Kochsahne", "Mayonnaise")

recipe12 = recipes("Hack-Reis_pfanne", 12, "https://www.rewe.de/rezepte/hack-reis-pfanne/",
                   "Langkornreis", "Paprikaschoten", "Gurke",
                   "Lauchzwiebeln", "Weißweinessig", "Hackfleisch")

recipe13 = recipes("Pizzabroetchen", 13, "https://www.rewe.de/rezepte/schnelle-pizzabroetchen/",
                   "Aufbackbroetchen", "Paprika", "zwiebel",
                   "Salami- Sticks", "geriebener Kaese")

recipe14 = recipes("Zwiebel- Sahne- Haehnchen", 14, "https://www.rewe.de/rezepte/zwiebel-sahne-haehnchen/",
                   "Knoblauchzehe", "Zwiebel", "Sahne", "Gemuesebruehe", "Haehnchenbrustfilet")

recipe15 = recipes("Spaghetti- Bolognese", 15, "https://www.rewe.de/rezepte/spaghetti-bolognesesosse/",
                   "Spaghetti", "Zwiebel", "Moehren", "Bolognese Sauce")



