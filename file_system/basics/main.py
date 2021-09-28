# This way you have to remember to close the file
file=open("myFile.txt")
contents=file.read()
print(contents)
file.close()

# A better way :
with open("myFile.txt", mode="r") as file:
    contents_2=file.read()
    print(contents_2)
# once you escape indentation the file closes automatically

with open("myFile.txt", mode="a") as file:
    file.write("\n and Tom Brady is the goat")

with open("myFile.txt", mode="r") as file:
    print(file.read())

with open("newFile.txt", mode="a")as new_file:
    new_file.write("this is a new line in a document that did not exist")
