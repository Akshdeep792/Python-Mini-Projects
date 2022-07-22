

try:
    file = open("./errorhandling/data.txt")
    a_dict = {"name":"Baen"}
    print(a_dict["name"])
except FileNotFoundError:
    file = open("./errorhandling/data.txt", "w")
    file.write("Something")

except KeyError as error_msg:
    print(f"The key {error_msg} does not exist")

# except IndexError
else:
   content = file.read()
   print(content)

finally:
    file.close()
    print("File is closed")

# height = float(input("Height: "))
# weight = int(input("Weight: "))

# if height > 3:
#     raise ValueError("Height should be less than 3 meters")

# bmi = height / weight*weight

# print(bmi)