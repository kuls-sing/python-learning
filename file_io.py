# with open("my_notes.txt", "w") as f:
#     f.write("Hi, may name is Kulwant\n")
#     f.write("I live in Bangalore\n")
#     f.write("Bangalore is the IT Hub of India!")
    
# with open("my_notes.txt", "r") as f:
#     print(f.read())
# with open("my_notes.txt", "a") as f:
#     f.write("\nThis is the 4th line appended")
# with open("my_notes.txt", "r") as f:
#     for line in f:
#         print(line.strip())

device_list =["Roku Express", "Roku Ultra", "Roku TV", "Roku Streambar"]

with open("devices.txt", "w") as f:
    for device in device_list:
        f.write(device + "\n")
with open("devices.txt", "r") as f:
    for i, line in enumerate(f, start=1):
        print(f"{i}. {line.strip()}")