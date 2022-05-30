# Write a program that will create a list of people with name, age, height, and weight
# Sort the list of people by age
class People:
    common_list = []

    def __init__(self, name, age, height, weight):
        self.name = name
        self.age = age
        self.height = height
        self.weight = weight
        self.common_list.append(self)

    def __repr__(self):
        return repr((self.name, self.age, self.height, self.weight))


person1 = People("Mike", 18, 182, 89)
person2 = People("Ron", 32, 177, 92)
person3 = People("Grace", 25, 168, 56)
person4 = People("Nikol", 19, 170, 58)
person5 = People("Lily", 65, 155, 60)

print(sorted(People.common_list, key=lambda person: person.age))
