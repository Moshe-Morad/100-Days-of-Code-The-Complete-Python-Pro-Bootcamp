# with open("weather_data.csv") as weather_data:
#     data = weather_data.readlines()
#     print(data)

# import csv
#
# with open("weather_data.csv") as weather_data:
#     data = csv.reader(weather_data)
#     temperatures = []
#     # print(data)
#     for row in data:
#         if row[1] != "temp":
#             temperatures.append(int(row[1]))
#     print(temperatures)

import pandas

# data = pandas.read_csv("weather_data.csv")
# print(type(data))
# print(data["temp"])

# data_dict = data.to_dict()
# print(data_dict)

# temp_list = data["temp"].tolist()
# sum_of_temp = 0
# for temp in temp_list:
#     sum_of_temp += temp
# avg = sum_of_temp / len(temp_list)
# print(avg)

# avg = sum(temp_list) / len(temp_list)
# print(avg)
# avg = data["temp"].mean()
# print(avg)
#
# biggest = data["temp"].max()
# print(biggest)

# Get Data in Columns from DataFrame
# print(data["condition"])
# print(data.condition)

# Get Data in Row from DataFrame
# print(data[data.day == "Monday"])
# print(data[data.temp == data.temp.max()])

# monday = data[data.day == "Monday"]
# print(monday.condition)
# monday_temp_F = monday.temp * (9 / 5) + 32
# print(monday_temp_F)

# Create a DataFrame From Scratch
# data_dict = {
#     "students": ["Amy", "James", "Angela"],
#     "scores": [76, 56, 65]
# }
# data = pandas.DataFrame(data_dict)
# data.to_csv("new_data.csv")

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data_20240904.csv")
# My Way
# temp_list = data["Primary Fur Color"].value_counts()
# df = pandas.DataFrame(temp_list)
# df.to_csv("squirrel_count.csv")
# print(temp_list)

# Course Way
gray_squirrel_count = len(data[data["Primary Fur Color"] == "Gray"])
red_squirrel_count = len(data[data["Primary Fur Color"] == "Cinnamon"])
black_squirrel_count = len(data[data["Primary Fur Color"] == "Black"])

print(gray_squirrel_count)
print(red_squirrel_count)
print(black_squirrel_count)

data_dict = {
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "Count": [gray_squirrel_count, red_squirrel_count, black_squirrel_count]
}

df = pandas.DataFrame(data_dict)
df.to_csv("squirrel_count.csv")




