import pandas

data = pandas.read_csv("../basic/weather_data.csv")
data_dict = data.to_dict()
print(data_dict)
temp_list = data["temp"].to_list()
print(temp_list)

print("\nmethods to the pandas_package Series data type\n")

print(data["temp"].mean())
print(data.temp.median())  # with pandas_package you can access like an object

print('\n ACCESS A ROW THROUGH A CONDITION\n ')

row = data[data.day == 'Monday']
print(row)
row = data[data.temp == data.temp.max()]
print(row)

print('\n MAKE DATA AS A DATAFRAME IN PANDAS AND CREATE FILES\n')

data={
    "students":["Amy","tom","Ben"],
    "scores":[80,90,100]
}
data_frame=pandas.DataFrame(data)
print(data_frame)
data_frame.to_csv("./csv_from_code")



