"""Squirrel Census"""
import pandas

squirrel_data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

gray = len(squirrel_data[squirrel_data["Primary Fur Color"] == "Gray"])
black = len(squirrel_data[squirrel_data["Primary Fur Color"] == "Black"])
cinnamon = len(squirrel_data[squirrel_data["Primary Fur Color"] == "Cinnamon"])

print(f"Gray: {gray}, Black: {black}, Cinnamon: {cinnamon}")

squirrel_data_dict = {
    "Fur Color": ["Gray", "Black", "Cinnamon"],
    "Count" : [gray, black, cinnamon],
}

squirrel_dataframe = pandas.DataFrame(squirrel_data_dict)

squirrel_dataframe.to_csv("fur_color.csv")
