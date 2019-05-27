from veryprettytable import VeryPrettyTable

table = VeryPrettyTable(["animal", "ferocity"])

table.add_row(["wolverine", 100])
table.add_row(["grizzly", 87])
table.add_row(["cat", -1])
table.add_row(["dolphin", 63])

print(table)

#auf "pycharm" klicken, dann unter "Preferences" gehen, beim "Project Interpreter" "+" die jeweilige pip auswählen und installieren