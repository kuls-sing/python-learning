cities = []
for i in range(3):
    cities.append(input("Enter City name:"))

with open("user_cities.txt", "w") as f:
    for city in cities:
        f.write(city + "\n")

with open("user_cities.txt", "r") as f:
    for i, line in enumerate(f, start=1):
        print(f"{i}. {line.strip()}")
        
# OR

with open("user_cities.txt", "w") as f:
    for i in range(3):
        city = input("Enter city name: ")
        f.write(city + "\n")

with open("user_cities.txt", "r") as f:
    for i, line in enumerate(f, start=1):
        print(f"{i}. {line.strip()}")