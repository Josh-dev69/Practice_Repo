name = input("Enter Your Name: ")

with open("filename.txt", "w") as file:
    file.write(name)

with open("filename.txt", "r") as file:
    for line in file:
        print(f"Your file has {len(line)} character")