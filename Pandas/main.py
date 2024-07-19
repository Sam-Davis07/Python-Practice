import pandas

data = pandas.read_csv("Test.csv")

grey_squ = len(data[data["PrimaryFurColor"] == "Gray"])
Cinnamon_squ = len(data[data["PrimaryFurColor"] == "Cinnamon"])
black_squ = len(data[data["PrimaryFurColor"] == "Black"])

print(grey_squ)
print(Cinnamon_squ)
print(black_squ)


data_dict = {
    "Fur Color" : ["Grey","Cinnamon","Black"],
    "Count" : [grey_squ,Cinnamon_squ,black_squ]
}


df = pandas.DataFrame(data_dict)

df.to_csv("new_data.csv")
