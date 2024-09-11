my_dict = {"Сергей": 2003, "Алина": 2004, "Андрей": 2002}
print(my_dict)
print(my_dict["Сергей"])
print(my_dict.get("Алексей"))
my_dict.update({"Алексей": 1997,
               "Антон": 1985})
print(my_dict)
a = my_dict.pop("Андрей")
print(a)
print(my_dict)

my_set = {True, 11, 58.1, 11, "pain", True, "pain"}
print(my_set)
my_set.add("ramen" and 12)
my_set.discard("pain")
print(my_set)