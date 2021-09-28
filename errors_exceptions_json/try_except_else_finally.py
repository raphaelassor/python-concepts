# FILE NOT FOUND
# with open("file.txt") as file:
#     file.read()

# KEY ERROR
# a={}
# n=a["keyname"]

# AND SO ON ....

try:
    file = open("data.json")
    a={"key":0}
    num=a["sssddd"]
except FileNotFoundError:
    # always specify the error.
    # it is PEP 8 guidelines and forces you to write precise code
    print("there was an error")
    file = open("data.json", "w")
except KeyError as err_msg:
    print(f"the key {err_msg} does not exist")
else:
    file.write("after exception catching")
finally:
    file.close()
    print("file was closed")
