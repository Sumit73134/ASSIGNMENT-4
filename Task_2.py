#step 1:

data= input("Enter text to write to the file: ")
with open("output.txt", "w") as file:
    file.write(data + "\n")

#step 2:

extra_data = input('Enter additional text to append: ')
with open("output.txt", "a") as file:
    file.write(extra_data +"\n")


# step 3:

print("\nFinal content of output.txt:")
with open("output.txt", "r") as file:
    content = file.read()
    print(content)