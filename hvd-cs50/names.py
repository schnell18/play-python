# names = []
# for _ in range(3):
#     name = input("What's your name? ")
#     names.append(name)

# file = open("names.txt", "a")
# for name in sorted(names):
#     file.write(f"Hello, {name}\n")
#     print(f"Hello, {name}")
# file.close()

# with open("names.txt", "a") as file:
#     for name in sorted(names):
#         file.write(f"Hello, {name}\n")
#         print(f"Hello, {name}")

with open("names.txt", "r") as file:
    for line in file:
        print("Hello,", line.rstrip())
