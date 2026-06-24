class Contact:
    def __init__(self, name, phone, email):
        self.name = name
        self.phone = phone
        self.email = email
        
    def dsiplay(self):
        print(f"Name: {self.name} | Phone: {self.phone} | Email: {self.email}")
    def update_phone(self, phone):
        self.phone = phone
    def __str__(self):
      return f"Name: {self.name} | Phone: {self.phone} | Email: {self.email}"
        
        
c1 = Contact("abc", "1234", "abc@email.com")
c2 = Contact("def", "5678", "def@email.com")

print(c1.name)
print(c1.email)
c1.dsiplay()

print(c2.name)
print(c2.email)
c2.dsiplay()

c1.update_phone("9999")
c1.dsiplay()
print(c1)