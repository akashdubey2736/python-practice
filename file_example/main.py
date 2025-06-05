file=open("my_file.txt")
contents=file.read()
print(contents)
file.close()


#alternative way
with open("my_file.txt") as file:
    contents=file.read()
    print(contents)

with open("my_file_to_write.txt","w") as file:
    file.write("Writing test is success")