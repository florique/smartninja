some_number = 3
float_number = 4.56
string_text = "hallo"
boolean = True

#das sind die 4 primitiven Datentypen

number_list = [2, 4, 1, 7, 8]

print (number_list[3])

#man kann auf jedes einzelne Element in der Liste mit der [] eckigen Klammer zugreifen siehe Beispiel
# oben dann wirft es die 7 aus (es wird gezählt 0, 1, 2, 3...)

#einen gewissen Bereich kann man auch auswerfen lassen z.B. mit [1:-1]

auto_list = ["audi", "tesla", "vw", "tesla"]
print (auto_list[2])

auto_list.append("Honda")
print (auto_list)

auto_list[4] = "Opel"
print (auto_list)

#mit [..] kann man einen Wert auch überschreiben siehe das Opel Beispiel obendrüber

number_list.sort()
print (number_list)

#mit dem .sort kann man eine Liste sortieren lassen

for item in auto_list:
        item = "bla"
        print(item)


shopping_list = {   "milk": 2,
                    "bread": 3,
                    "eggs": 10,
                    "dict": {
                        "c++": 5,
                        "java": 3,
                        "python": 1,
                    },
                    "list": [1, 2, 3, 4, 5]
                    }

print(shopping_list["list"])

