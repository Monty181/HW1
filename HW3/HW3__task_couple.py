# Write a program that will find a couple.
# On the start program have to create a list of 10 random people male and female.
# Every person have three fields name, age, sex
# Program asks a user to enter a name and a desired age for search
# Matching rule
# Couple can match if users age difference not more than 5 years and both names has at least same two letters
# If match is found program should print - Congrats there is a matching pair Name1 + Name2!
# It no match - just print Sorry, no match! =(
import random
from faker import Faker


class People:

    def __init__(self, name, age, sex):
        self.name = name
        self.age = age
        self.sex = sex

    def get_person_age(self):
        return self.age

    def get_person_name(self):
        return self.name

    def __repr__(self):
        return repr((self.name, self.age, self.sex))


def generate_person(amount):
    i = 0
    fake = Faker()

    while i < amount:
        name = fake.name()
        age = random.randint(18, 100)
        sex = random.choice(["female", "male"])
        yield People(name, age, sex)
        i += 1


people_list = list(generate_person(11))
print(*people_list)

input_name = str(input("Enter the name please: "))
input_age = int(input("Enter the age please: "))
match_list = []

for i in people_list:
    if abs(People.get_person_age(i) - input_age) < 6 and \
            len(set(input_name).intersection(set(People.get_person_name(i)))) > 1:
        match_list.append(True)
        print(f"Congrats there is a matching pair {People.get_person_name(i)} + {input_name}")
    else:
        match_list.append(False)

if True not in match_list:
    print("Sorry, no match!")





