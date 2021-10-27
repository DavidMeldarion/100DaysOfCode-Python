import turtle

from prettytable import PrettyTable

table = PrettyTable()

table.add_column("Pokemon", ["Chespin", "Pancham", "Doduo"])
table.add_column("Type",["Grass", "Fighting", "Flying"])
table.align = "l"

print(table)

# timmy = turtle.Turtle()
# timmy.shape("turtle")
# timmy.color("gold1")
# timmy.forward(100)

# timmy.color('red', 'yellow')
# timmy.begin_fill()
# while True:
#     timmy.forward(200)
#     timmy.left(170)
#     if abs(timmy.pos()) < 1:
#         break
# timmy.end_fill()

# my_screen = turtle.Screen()
# my_screen.exitonclick()
