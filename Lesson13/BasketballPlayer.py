class Player():
    def __init__(self, first_name, last_name, height_cm, weight_kg):
        self.first_name = first_name
        self.last_name = last_name
        self.height_cm = height_cm
        self.weight_kg = weight_kg

class BasketballPlayer(Player):
    def __init__(self, first_name, last_name, height_cm, weight_kg, points, rebounds, assists):
        super().__init__(first_name, last_name, height_cm, weight_kg)
        self.points = points
        self.rebounds = rebounds
        self.assists = assists


    def set_points(self, points):
        self.points = points


class FootballPlayer(Player):
    def __init__(self, first_name, last_name, height_cm, weight_kg, goals, yellow_cards, red_cards):
        super().__init__(first_name, last_name, height_cm, weight_kg)
        self.goals = goals
        self.yellow_cards = yellow_cards
        self.red_cards = red_cards

if __name__ == "__main__":
    j = BasketballPlayer("Michael", "Jordan", 205, 87, 208903, 1, 1)
    n = BasketballPlayer("Dirk", "Nowitzki", 235, 90, 0, 1, 1)

    ronaldo = FootballPlayer("Cristiano", "Ronaldo", 184, 79, 586, 95, 11)
    messi = FootballPlayer("Lionel", "Messi", 170, 67, 575, 67, 0)

    n.set_points(900)

    player = [j, n]
    player2 = [ronaldo]

## wichtig: Listen nicht mit Datensätzen mit unterschiedlichen Attributen mischen! (ich kann für die Basketballspieler keine Werte
## abfragen, die nur ein Fußballspieler hat.)

    for item in player:
        print(item.first_name)
        print(item.height_cm)

    for item in player2:
        print(item.first_name)
        print(item.goals)