words = ["hi", "hello", "ok", "python", "yes", "world"]
new_list = [i for i in words if len(i)>3]
print(new_list)
###############################################################################
squars_grater_than_50 = [i*i for i in range(1,11) if i*i > 50]
print(squars_grater_than_50)
###############################################################################
celsius = [0, 20, 37, 100]
temperature_in_Fahrenheit = [(i*9/5 +32) for i in celsius]
print(temperature_in_Fahrenheit)
###############################################################################
sentence = "Hello World Python"
uppercase_letters_only =[i for i in sentence if i.isupper() is True]
print(uppercase_letters_only)