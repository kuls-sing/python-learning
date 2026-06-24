# favorite_foods = ["pizza", "biryani", "Burger", "chocolate", "Jiuce"]

# for item in favorite_foods:
#     print(f"I like {item}")
    
city = ["Bangalore", "Delhi", "London"]
city.append("New York")
print(len(city))
if "London" in city:
    print("True")
    
cities = ["Bangalore", "Delhi", "London", "New York"]
print(cities[0])      # Bangalore  (first item)
print(cities[-1])     # New York   (last item)
print(cities[1:3])