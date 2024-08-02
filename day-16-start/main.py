#from turtle import Turtle, Screen

#timmy = Turtle()
#my_screen = Screen()

#timmy.shape('turtle')
#timmy.color("DeepSkyBlue")

#timmy.forward(100)

#my_screen.exitonclick()

from prettytable import PrettyTable

table = PrettyTable()
table.align = "l"
table.field_names = ["Pokemon Name", "Type"] 

table.add_rows(
    [
        ["Pikachu", "Electric"],
        ["Squirtle", "Water"],
        ["Charmander", "Fire"]
    ]
)

print(table)