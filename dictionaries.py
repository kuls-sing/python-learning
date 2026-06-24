# phone = {"brand": "Samsung", "model":"S26", "price": 1000, "in_stock": True}
# print(phone["brand"])
# phone["price"] = 1500
# phone["color"] = "red"

# for key in phone:
#     print(phone[key])

# student = {"name": "Kulwant", "grade": "A", "score": 95}
# for key, value in student.items():
#     print(f"{key} : {value}")

classroom ={"students":['Amit', 'Sara', 'Raj'], "scores": [85, 92, 78]}
for i in classroom["students"]:
    print(i)
print(max(classroom["scores"]))