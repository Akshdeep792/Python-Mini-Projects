import pandas

data = pandas.read_csv("./working-with-data/Squirel/squirel-data.csv")



gray_count = len(data[data["Primary Fur Color"] == 'Gray'])
black_count = len(data[data["Primary Fur Color"] == 'Black'])
cinnamon_count = len(data[data["Primary Fur Color"] == 'Cinnamon'])

print(gray_count)
print(black_count)
print(cinnamon_count)

data_dict = {
    "Colors" : ["Gray", "Black", "Cinnamon"],
    "scores": [gray_count, black_count, cinnamon_count]
}

data = pandas.DataFrame(data_dict)

data.to_csv("./working-with-data/Squirel/color_count.csv")