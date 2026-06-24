# for i in range(1, 6):
#     print(i)

# names = ["Kulwant", "Amit", "Sara"]
# for name in names:
#     print(f"Hello {name}!")

# for i in range(1, 6):
#     print(f"{i} x 2 = {i * 2}")

# count = 5
# while count>0:
#     print(f"Count: {count}")
#     count -= 1
# print("Done!")

# for i in range(1,11):
#     print(f"3 X {i} = {3*i}")
    
Correct_number = False

while (not Correct_number):
    guess = int(input("Try to guess the Correct_number: "))
    if guess == 7:
        print("Correct!")
        Correct_number = True