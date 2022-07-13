# with open(r"C:\Users\Acer\Desktop\Python\working-with-data/champions.csv") as file:
#     contents = file.readlines()
#     print(contents)

# import csv

# with open(r"./working-with-data/champions.csv") as data_file:
#     data = csv.reader(data_file)
#     names = []
#     for row in data:
#         print(row)
#         names.append(row[0])
    
#     print(names)

# from unicodedata import name
import pandas

data = pandas.read_csv("./working-with-data/champions.csv")
# print(data)


# getting data in coloumn
# print(data["pokemon"])

# data_dict = data.to_dict()
# print(data_dict)

# name_list = data["name"].to_list()
# print(name_list)


# Get data in row
# print(data[data.name == 'baen'])

# baen = data[data.name == 'baen']

# print((baen))

#Creating Data Frame from scratch

# data_dict = {
#     "students" : ["Amy", "James", "Angela"],
#     "scores": [76,64,96]
# }

# data = pandas.DataFrame(data_dict)
# data.to_csv("./working-with-data/new-data.csv")

for (key,row) in data.iterrows():
    print(row.name)